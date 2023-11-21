import re
import logging
import glob
import subprocess
import pytest

import debugpy

from pathlib import Path
from os.path import exists
from sys import exit

# Pulled from https://gist.github.com/zodman/d8d3ede4b1f1e050caaf890424d04ee8

NUMBER_FINDER = re.compile(r"\d+")


directory = Path.resolve(Path(__file__)).parent


def get_output_filename(input_filename):
    return (
        str(directory)
        + "/output/output%s.txt" % NUMBER_FINDER.findall(input_filename)[0]
    )


def test_solution():
    INPUT_FOLDER = directory / "input/"
    OUTPUT_FOLDER = directory / "output/"
    SOLUTION_FILE = directory / "solution.py"

    WRONG_PLACE_TO_RUN_MSG = (
        "You have to run this program under, downloaded inputs and outputs."
    )

    REQUIRED_FOLDERS = [INPUT_FOLDER, OUTPUT_FOLDER]
    wrong_place_to_run = False
    for folder in REQUIRED_FOLDERS:
        if not exists(folder):
            print("Folder '%s' does not exists. " % folder)
            wrong_place_to_run = True

    if wrong_place_to_run:
        raise Exception(WRONG_PLACE_TO_RUN_MSG)

    if not exists(SOLUTION_FILE):
        raise Exception(
            "Solution must be inside solution.py, put your solution to there "
            + "and run this command again."
        )

    input_files = glob.glob(str(INPUT_FOLDER) + "/*.txt")
    print(input_files)
    assert len(input_files) > 0

    passing = False

    for input_file in input_files:
        print("Running for ", input_file)
        output_file = get_output_filename(input_file)
        result_file = (
            "/home/developer/hackerrank-python/climbing_the_leaderboards/result.txt"
        )
        cmd = f"OUTPUT_PATH={result_file} python {directory}/solution.py"

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True,
        )

        with open(input_file, "rb") as f:
            input_data = f.read()

        with open(output_file, "rb") as f:
            output_data = f.read()

        err = None
        out, err = process.communicate(input_data)

        with open(result_file, "rb") as f:
            out = f.read()

        if err:
            print("Error happened when executing your solution:")
            print("--------------------------------------------")
            print(err)
            raise Exception(err.decode())

        out = out[:-1]
        assert out.decode() == output_data.decode()
        if out == output_data:
            passing = True
            print("%s: SUCCESS" % input_file)
        else:
            passing = False
            pytest.fail(out.decode() + " should be the same as ")
            print("%s: FAIL" % input_file)
            print("EXPECTED: \n", output_data.decode())
        print("-------OUTPUT------")
        print(out.decode())
    logging.warning("passing is: ")
    assert passing

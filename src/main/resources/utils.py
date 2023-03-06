import csv
import os
import zipfile
from typing import Literal


class JarUtils(object):
    """
    Class for reading files from a jar
    """
    current_dir = __file__.replace("/" + os.path.basename(__file__), "")

    def __init__(self, mode: Literal["r", "w", "x", "a"] = 'r'):
        self.zip_file = zipfile.ZipFile(self.current_dir, mode)

    def read(self, file_name):
        """
        Reads a file from the jar
        :param file_name: the name of the file to read
        :return: the contents of the file
        """
        return self.zip_file.read(file_name)

    def write(self, file_name, data):
        """
        Writes data to a file in the jar
        :param file_name: the name of the file to write to
        :param data: the data to write to the file
        :return:
        """
        if self.zip_file.mode == "r":
            raise Exception("Zip file is in read-only mode")
        self.zip_file.writestr(file_name, data)

    def __del__(self):
        """
        Closes the zip file when the object is deleted because that's what ZipFile specifies you should do,
        and there's no other surefire and clean way to close every time an action is completed  (even though using
        __del__ isn't recommended).
        https://docs.python.org/3/library/atexit.html may also be of use
        :return:
        """
        self.zip_file.close()

    # def close(self):
    #     self.zip_file.close()


def get_csv(file_name):
    return csv.reader(JarUtils().read(file_name).decode("utf-8").splitlines())

def rps_winner_check(player1, player2):
    """
    Checks which player won rock paper scissors
    """
    # todo: make this match-case
    if player1 == player2:
        return "tie"
    else:
        match player1:
            case "rock":
                if player2 == "scissors":
                    return "player1"
                else:
                    return "player2"
            case "paper":
                if player2 == "rock":
                    return "player1"
                else:
                    return "player2"
            case "scissors":
                if player2 == "paper":
                    return "player1"
                else:
                    return "player2"

def tax_calculator(amount):
    """
    Calculates tax paid, accounting for New Zealand's tax brackets
    """

    # Tax variable
    tax = 0
    amount_adjusted = amount

#!/usr/bin/env python
"""
TODO: huge cleanups - stuff to do is also in comments so do those too
oh yeah also i should set up something that just updates the jar instead of maven building every single time
i wanna run python)
"""
import warnings
import zipfile, os, argparse, csv, sys, io, secrets
from typing import Literal
import sentry_sdk

import utils

sentry_sdk.init(
    dsn = "https://27252358513746979bf5efeb097b181d@o317122.ingest.sentry.io/4504799572983808",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate = 1.0,
    send_default_pii = True,
    release = "dtschallenges@v1.1.3",
    _experiments = {
        "profiles_sample_rate": 1.0,
    }
)

# print(__name__)
#
# print(sys.argv[1], sys.argv[2])
#
# # sys.argv[1] needs to match os.getpgid(0) just to mitigate people trying from trying to run the
# # script from the command line (it's just a small check for pids, not a security measure)
# # but we should use argparse not argv
#
# print(os.getpid.__name__, os.getpid())
# print(os.getpgid.__name__, os.getpgid(0))
# print(os.getsid.__name__, os.getsid(0))
# print(os.getppid.__name__, os.getppid())  # this one isn't related but was suggested so i'll look into this ig


# will clean up later
def challenge2():
    """
    Gets the first and third columns of the mockData.csv file
    :return:
    """

    csv_data = utils.get_csv("mockData.csv")

    # ask the user if they would like to read the csv file
    read = input("Would you like to read the csv file? ('y' for yes, other for skip) ")
    if read == "y":
        print("Reading the csv file...")
        for row in utils.get_csv("validData.csv"):
            print(row)
        return None
    del read

    # there is some weird quirk in this program where it'll print the whole file occasionally, though i suspect
    # that's more of a java issue than a python issue

    invalid_data: dict = dict()  # initialising the dictionary via the dict() call to avoid ambiguity between empty
    # set and empty dict
    print("Valid usernames and emails: ")

    # This is to skip the header row
    itercsv_data = iter(csv_data)
    next(itercsv_data)
    valid_data = io.StringIO(str(utils.JarUtils().read("validData.csv")), newline = '')
    writer = csv.writer(valid_data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    for row in itercsv_data:
        checked = (row[0], row[3] if "@" in row[3] and "." in row[3] else invalid_data.update({row[0]: row[3]}))
        if None not in checked:
            print(checked[0], checked[1])

            # check if the user email pair is already in the csv
            # if it is, don't add it again
            reader = csv.reader(valid_data.getvalue().splitlines())
            itercsv_data = iter(reader)
            next(itercsv_data)
            in_csv = False
            for line in itercsv_data:
                if line is checked:
                    print("Already in the CSV")
                    in_csv = True
                    break
            if not in_csv:
                writer.writerow((checked[0], checked[1]))

    # TODO: https://www.pythontutorial.net/python-basics/python-write-csv-file/  # despite program being complete
    #  this is still usable for optimizing the csv with writing data in bulk/using a dict.
    #  this spec doc also remains useful https://docs.python.org/3/library/zipfile.html
    print("Invalid emails: ")
    if len(invalid_data) == 0:
        print("No invalid emails to report :)")
    else:
        for key, value in invalid_data.items():
            print(key, value)

    # ask the user if they would like to add more usernames and emails
    adding = True
    while adding:
        add = input("Would you like to add more usernames and emails? (y/n) ")
        if add == "y":
            new_username = input("Enter a new username: ")
            new_email = input("Enter a new email: ")
            if "@" in new_email and "." in new_email:
                print("Valid email")
                writer.writerow((new_username, new_email))
            else:
                print("Invalid email")
        elif add == "n":
            adding = False

    # suppress duplicate name warning
    warnings.filterwarnings("ignore", category = UserWarning, module = 'zipfile')
    utils.JarUtils(mode = "a").write("validData.csv", valid_data.getvalue())  # this is a terrible solution and it
    # may be
    # better to just use the .open() method of ZipFile so we don't have to suppress the warning


def challenge3():
    """
    rock paper scissors against computer using python secrets library (as opposed to random)
    """
    weapons = ["rock", "paper", "scissors"]
    while True:
        # generate a random weapon for the computer
        computer_choice = secrets.choice(weapons)
        # ask the user for their weapon - this input getting code is untidy but it doesn't matter
        user_choice = input("Choose your weapon: ")
        # check if the user input is valid
        checking_input = True
        while checking_input:
            if user_choice in weapons:
                checking_input = False
            else:
                user_choice = input("Invalid input. Choose your weapon: ")
        print("Computer chose", computer_choice)
        # check if the user won
        result = utils.rps_winner_check(user_choice, computer_choice)

        if result == "player1":
            print("You win!")
        elif result == "player2":
            print("You lose!")
        else:
            print("Draw!")
        # ask the user if they want to play again
        play_again = input("Play again? (y/n) ")
        if play_again == "y":
            continue
        elif play_again == "n":
            break
        else:
            print("Invalid input")

def challenge4():
    """
    Calculates the amount of tax paid for a given yearly pay, using New Zealand tax brackets
    """
    # get the user's yearly pay
    yearly_pay = float(input("Enter your yearly pay: "))
    # calculate the tax paid
    tax_paid = utils.tax_calculator(yearly_pay)
    # print the tax paid
    print("Tax paid: $", tax_paid)


match int(sys.argv[2]):
    case 2:
        challenge2()
    case 3:
        challenge3()
    case 4:
        challenge4()

# This prevents instant killing of the program after the challenge runs - more of a testing thing but I'll keep it here
input("Execution of challenge finished. Press enter to exit...")

"""
TODO: huge cleanups - stuff to do is also in comments so do those too
oh yeah also i should set up something that just updates the jar instead of maven building every single time
i wanna run python)
"""
import warnings
import zipfile, os, argparse, csv, sys, io
from typing import Literal


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


# will clean up later
def challenge1():
    """
    Gets the first and third columns of the mockData.csv file
    :return:
    """

    csv_data = get_csv("mockData.csv")

    # ask the user if they would like to read the csv file
    read = input("Would you like to read the csv file? ('y' for yes, other for skip) ")
    if read == "y":
        print("Reading the csv file...")
        for row in get_csv("validData.csv"):
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
    valid_data = io.StringIO(str(JarUtils().read("validData.csv")), newline = '')
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
    JarUtils(mode = "a").write("validData.csv", valid_data.getvalue())  # this is a terrible solution and it may be
    # better to just use the .open() method of ZipFile so we don't have to suppress the warning


challenge1()
input("Execution of challenge finished. Press enter to exit...")

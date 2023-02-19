"""
TODO: huge cleanups - stuff to do is also in comments so do those too
oh yeah also i should set up something that just updates the jar instead of maven building every single time
i wanna run python)
"""

import zipfile, os, argparse, csv, sys


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

    def __init__(self):
        self.zip_file = zipfile.ZipFile(self.current_dir)

    def read(self, file_name):
        return self.zip_file.read(file_name)

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


print(dir(JarUtils()))


def get_csv(file_name):
    return csv.reader(JarUtils().read(file_name).decode("utf-8").splitlines())


print(get_csv("mockData.csv"))


# will clean up later
def challenge1():
    """
    Gets the first and third columns of the mockData.csv file
    :return:
    """
    csv_data = get_csv("mockData.csv")
    invalid_data: dict = dict()  # initialising the dictionary via the dict() call to avoid ambiguity between empty
    # set and empty dict
    print("Valid usernames and emails: ")

    # This is to skip the header row
    itercsv_data = iter(csv_data)
    next(itercsv_data)
    for row in itercsv_data:
        print(row[0], [row[3] if "@" in row[3] and "." in row[3] else invalid_data.update({row[0]: row[3]})][0])  #
        # add a note saying email values with None are invalid and aren't written to csv
        # TODO: https://www.pythontutorial.net/python-basics/python-write-csv-file/
        # TODO: https://docs.python.org/3/library/zipfile.html
    print("Invalid emails: ")
    if len(invalid_data) is 0:
        print("No invalid emails to report :)")
    else:
        for key, value in invalid_data.items():
            print(key, value)


challenge1()

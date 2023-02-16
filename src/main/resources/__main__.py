import zipfile, os, argparse, csv


print(__name__)

print(os.getpid.__name__, os.getpid())
print(os.getpgid.__name__, os.getpgid(0))
print(os.getsid.__name__, os.getsid(0))

current_dir = __file__.replace("/" + os.path.basename(__file__), "")
with zipfile.ZipFile(current_dir, "r") as archive:
    #print(archive.read("mockData.csv"))
    pass


def challeng():
    pass

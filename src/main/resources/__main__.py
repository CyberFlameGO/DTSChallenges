import zipfile, os, argparse, csv, sys


print(__name__)

print(sys.argv[1], sys.argv[2])

#sys.argv[1] needs to match os.getpgid(0) just to mitigate people trying from trying to run the
#script from the command line (it's just a small check for pids, not a security measure)
# but we should use argparse not argv

print(os.getpid.__name__, os.getpid())
print(os.getpgid.__name__, os.getpgid(0))
print(os.getsid.__name__, os.getsid(0))

current_dir = __file__.replace("/" + os.path.basename(__file__), "")
with zipfile.ZipFile(current_dir, "r") as archive:
    #print(archive.read("mockData.csv"))
    pass


def challeng():
    pass

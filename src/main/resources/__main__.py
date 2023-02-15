import zipfile, os

print("hi")
current_dir = __file__.replace("/" + os.path.basename(__file__), "")
archive = zipfile.ZipFile(current_dir, "r")
print(archive.read("mockData.csv"))

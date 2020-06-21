import os
from datetime import datetime

print(os.getcwd())

# os.chdir("/Users/Anonymous/Public/")
#
# print(os.getcwd())
# # os.removedirs("/Users/Anonymous/Public/New/creation/hahaha")
# print(os.listdir())
#
# stats = os.stat("Python3").st_mtime
#
#
# print(datetime.fromtimestamp(stats))
#
# for dirpath, dirname, filename in os.walk("/Users/Anonymous/Public/"):
#     print("Current Path:", dirpath, "Directory Name:",
#           dirname, "FileName:", filename, sep='\n')
#     print()

path_values = os.path.join(os.environ.get("HOME"), "narendra.txt")

# print(os.listdir(os.environ.get("HOME")))
print(path_values)

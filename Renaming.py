import os
import sys

print(sys.executable)

print(os.getcwd())

os.chdir("/Users/Anonymous/Public/video_files")
# print(os.listdir())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    # print(f_name, f_ext)
    f_planet, f_ini, f_num = f_name.split("-")

    # f_planet = f_planet.strip()
    # f_ext = f_ext.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_file = "{}-{}{}".format(f_num, f_planet, f_ext)

    os.rename(f, new_file)

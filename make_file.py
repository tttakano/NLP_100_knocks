import sys
import os

args = sys.argv
folder_name = "NLP_" + str(int(args[1]) * 10) + "~" + str((int(args[1])+1)*10)
os.mkdir(folder_name)
os.chdir(folder_name)
for i in range(10):
    f = open("NLP_" + str(int(args[1]) * 10 + i) + ".py", "w")

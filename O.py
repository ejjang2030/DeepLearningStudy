import os


def setOS():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def installPip(command):
    os.system(command)
    lst = command.split(" ")
    lst= lst[2].split("==")
    print(f"Python Package Installed : {lst[0]} version = {lst[1]}")

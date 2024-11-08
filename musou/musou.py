import ctypes
import sys
import argparse

if not ctypes.windll.shell32.IsUserAnAdmin():
    # sys.exit(-1)
    pass

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--genshin")
parser.add_argument("-m", "--migoto")

args = parser.parse_args()
print(args)
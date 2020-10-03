from pip._internal import main #main was moved to internal in pip 
import os

def redundancy_check(pkg_name):
	try:
		__import__(pkg_name)
	except ImportError:
		print("Missing package :- " , pkg_name,  "\nInstallling...")
	
		main(['install', pkg_name])

pkgs=[]
path = os.path.realpath(__file__)[:-8]
#removes last 8 chars, ie, setup.py to give running path.
os.chdir(path)


reqs = open("prerequisites.txt" , "r")
for line in reqs:
	redundancy_check(line.rstrip())
	

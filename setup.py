from pip._internal import main 
#main was moved to internal in pip 

def redundancy_check(pkg_name):
	try:
		__import__(pkg_name)
	except ImportError:
		print("Missing package :- " , pkg_name,  "\nInstallling...")
	
	main(['install', pkg_name])

redundancy_check("keyboard")
redundancy_check("mss")

	

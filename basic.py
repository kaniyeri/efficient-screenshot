import keyboard
from mss import mss
import datetime
import os
print("Press Ctrl to take a screenshot.\nThe screenshot will be saved to the folder where the script exists.\nPress Esc to close this application.\nCurrent Date and Time:- ",datetime.datetime.today(),"\n")
count = 0
partial_filename = str(datetime.datetime.now())

path_file = os.path.realpath(__file__)
path_file = path_file[:-8]

datetime_now = (((str(datetime.datetime.today()))[:-7]).replace(" ","--")).replace(":","-")

final_path = os.path.join(path_file,datetime_now)

os.makedirs(final_path)


os.chdir(final_path)




for item in ["." , " " ,":"]:
	partial_filename=partial_filename.replace(item , "")
	

while keyboard.is_pressed('Esc')==False:
	if keyboard.is_pressed('Ctrl'):
		with mss() as sct:
			name = str(partial_filename+str(count)+".png")
			
			filename = sct.shot(mon=-1, output=name)
			print(filename)
			count+=1
            
            

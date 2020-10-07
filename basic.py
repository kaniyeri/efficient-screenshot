import keyboard
from mss import mss
import datetime

count = 0
partial_filename = str(datetime.datetime.now())
for item in ["." , " " ,":"]:
	partial_filename=partial_filename.replace(item , "")
	
#partial_filename=partial_filename.replace("." , "")
#partial_filename=partial_filename.replace(" " , "")
#partial_filename=partial_filename.replace(":" , "")
while keyboard.is_pressed('Esc')==False:
	if keyboard.is_pressed('Ctrl'):
		with mss() as sct:
			name = str(partial_filename+str(count)+".png")
			
			filename = sct.shot(mon=-1, output=name)
			print(filename)
			count+=1

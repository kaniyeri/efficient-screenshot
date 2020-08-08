import keyboard
from mss import mss
while keyboard.is_pressed('Esc')==False:
	if keyboard.is_pressed('Ctrl'):
		with mss() as sct:
			sct.shot()

	

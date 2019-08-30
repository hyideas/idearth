#path setting
import sys
sys.path.insert(0, "/home/pi/remote_control_new/remote_control/remote_control")
from driver import camera, stream, wheels,esc_1060

#initialization
db_file = "/home/pi/remote_control/remote_control/driver/config"

esc = esc_1060.ESC(1, 0x40,60, 10, 11)

##################################################################3######




SPEED = 100

key = 0

#input command
esc.set_speed(4)
while key != 'q':
	key = raw_input("give command : ")
	print "input key : [" + key + "]"

	#move forward
	if key == "w":
		print "[forward]\n"

		#TODO



		debug = "speed =", SPEED

	#move backward
	elif key == 's':
		print "[backward]\n"

		#TODO




	#turn left
	elif key == 'a':
		print "[turn left]\n"

		#TODO



	#turn right
	elif key == 'd':
		print "[turn right]\n"

		#TODO


	#exit
	elif key == 'q':
		print "[stop] entered\n"

		#TODO


		sys.exit()

	#wrong input
	else :
		print "Wrong Input Command\n"

import random #for random testing only
import time #about time :)
import serial #for serial port
import logging #for data logger
from pathlib import Path
import os

#Random Type Testing
bottle_type_list = ['A', 'B', 'C'] #for random testing only

#Serial Preparation
homePath = os.path.join(str(Path.home()))
tempHomePath = homePath.split('/')[-1]

# .sh path
command4 = str(os.path.abspath(os.getcwd()))+"/recheck.sh"

# command recheck moxa usbcore & usbserial 
# command1 = 'sudo lsmod | grep mxu11x0 > lsmod_output.txt'
# command2 = 'sudo dmesg | grep usbcore | grep mxu11x0 > dmseg_usbcore.txt'
# command3 = 'sudo dmesg | grep usbserial | grep MOXA > dmseg_usbserial.txt'

if tempHomePath == "oracle_tbr_bangban_1":
    port = '/dev/pts/2'
elif tempHomePath == "oracle_tbr_bangban_2":
    port = '/dev/pts/2'

else:
    port = '/dev/pts/2'
ser = serial.Serial()

ser.baudrate = 9600
ser.port = port
isConnected = False

while ( not isConnected ):
    try:
        print(not isConnected )
        ser.open() #Change serial port and baud rate here!!!
        isConnected = True
        print('here ')
        msg = 'PLC Connected'
        print(msg)
        logging.info(msg)

    except Exception as e:
        print("error:", e)
        ser.close()
        
        # reinstall - reload moxa
        os.system(command4)

        # recheck and collect result usbserial usbcore - moxa
        # os.system(command1)
        # os.system(command2)
        # os.system(command3)
        
        time.sleep(5)

i = 0
def dataLog_and_Send(output):
    logging.basicConfig(filename='SerialSender.log', filemode='w', format= '%(asctime)s - %(message)s')
    #print(bottle_type) #for testing only

    #In real system. Instead of print, You will send a logic to Microcontroller before PLC lol
    bottle_type = output
    if bottle_type == 'A':
        # logging.warning('Type_A => Ignore...')
        # print('Type_A => Ignore...') #for testing only
        ser.write(b'A') #for real system
    if bottle_type == 'B':
        # print("B")
        # logging.warning('Type_B => Reject with Pusher_1')
        # print(time.time())
        # print('Type_B => Reject with Pusher_1') #for testing only
        ser.write(b'B') #for real system
    if bottle_type == 'C':
        # logging.warning('Type_C => Reject with Pusher_2')
        # print('Type_C => Reject with Pusher_2') #for testing only
        ser.write(b'C') #for real system

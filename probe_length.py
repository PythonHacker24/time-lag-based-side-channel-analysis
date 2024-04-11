# #!/usr/share/python3 
#
# import serial 
# import time 
#
# import matplotlib.pyplot as plt 
# import numpy as np 
#
# serial_port = '/dev/cu.usbserial-0001'
# baud_rate = 9600 
#
# ser = serial.Serial(serial_port, baud_rate)
#
# maxLength = 10
#
# logger = []
# try:
#     print("In here")
#     for i in range(1, maxLength + 1):
#         payload = "a" * i 
#         print(payload)
#         startTime = time.time()
#         ser.write(payload.encode('utf-8') + b'\n')
#
#         try:
#             data = ser.readline().decode()
#             print("waiting")
#             endTime = time.time()
#
#             elapsedTime = endTime - startTime
#             logger.append(elapsedTime)
#
#         except UnicodeDecodeError as error: 
#             ser.write(payload.encode('utf-8') + b'\n')
#             data = ser.readline().decode()
#             logger.append(0.0)
#     time.sleep(1)
#
# except KeyboardInterrupt:
#     print("Keyboard Interrupt Detected. Exiting .... ")
#     ser.close()
#     exit()
#
# lengthList = []
#
# for i in range(0, maxLength):
#     lengthList.append(i)
#
# plt.plot(lengthList, logger, marker='o', linestyle='-')
#
# plt.title('Time vs Length')
# plt.xlabel('Length')
# plt.ylabel('Time Measurement')
#
# plt.grid(True)
# plt.show()
#
import serial 
import time 
import matplotlib.pyplot as plt 

serial_port = '/dev/cu.usbserial-0001'
baud_rate = 9600 

ser = serial.Serial(serial_port, baud_rate)

maxLength = 10
logger = []

try:
    print("In here")
    for i in range(1, maxLength + 1):
        payload = "a" * i 
        print("Sending payload:", payload)
        startTime = time.time()
        ser.write(payload.encode('utf-8') + b'\n')

        # Wait for response (adjust timeout as needed)
        try:
            ser.timeout = 1
            data = ser.readline().decode()
            print("Received data:", data)
            endTime = time.time()

            elapsedTime = endTime - startTime
            logger.append(elapsedTime)
    
        except UnicodeDecodeError as error: 
            ser.write("a".encode('utf-8') + b'\n')
            data = ser.readline().decode()
            logger.append(0.0)

except KeyboardInterrupt:
    print("Keyboard Interrupt Detected. Exiting .... ")
    ser.close()
    exit()

lengthList = [len("a" * i) for i in range(1, maxLength + 1)]

plt.plot(lengthList, logger, marker='o', linestyle='-')

plt.title('Time vs Length')
plt.xlabel('Length')
plt.ylabel('Time Measurement')

plt.grid(True)
plt.show()


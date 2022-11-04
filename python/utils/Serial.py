# Importing Libraries
# -*- coding: utf-8 -*-
import serial
import time

class Serial:
    def __init__(self, port, baudrate=19200):
        self.port = port
        self.baudrate = baudrate
        self.arduino = None
    
    # connect arduino
    def connect(self):
        max_try = 10
        now_try = 1
        try:
            while(now_try < max_try) :
                print("connecting... {}".format(now_try))
                self.arduino = serial.Serial(port=self.port, baudrate=self.baudrate)
                if self.arduino is not None : 
                    print("connect to {} port".format(self.port))
                    break
            if self.arduino is not None:
                return True
            else: 
                return False
        except:
            if not (self.arduino is None):
                self.arduino.close()
                self.arduino = None
                print("Disconnecting")
            else:
                print("No Connection")

    # read serial print and write file
    def save_data(self, data_type, start = 0, max_count=50, save_dir="./../data"):
        data_list = []
        now_count = -1
        start_message = "start new record"

        self.arduino.readline()
        self.arduino.readline()
        
        print("\nPress the Reset button to start importing samples...")
        while(now_count < max_count):
            if self.arduino.readable():
                try :
                    data = self.arduino.readline().decode('utf-8').strip()
                except :
                    data = self.arduino.readline().decode('utf-8').strip()
                if data == start_message: 
                    # flush dummy data
                    if now_count == -1:
                        data_list = []
                        now_count += 1
                    else :
                        with open(save_dir+'/'+data_type+"_sample_"+str(start+now_count)+'.txt', 'w') as file:
                            file.writelines(data_list[1:-1])
                            data_list = []
                            print("save {} {} data".format(data_type, now_count))
                            now_count += 1
                else :
                    data_list.append(data+"\n")
        
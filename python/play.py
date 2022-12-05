import samples, sys
import joblib
from utils import Serial
from collections import deque
from playsound import playsound

max_deque_size = 35

def yeolchae(serial): 
    data = ""
    check_data_list = deque()
    clf = joblib.load('model.pkl')
    
    while(True):
        try :
            data = serial.arduino.readline().decode('utf-8').strip()
        except :
            data = serial.arduino.readline().decode('utf-8').strip()
        
        # queue에 데이터 삽입
        if len(check_data_list) >= max_deque_size :
            check_data_list.popleft()
            check_data_list.append(list(map(float, data.strip('\n').split(" "))))
        
        else :
            check_data_list.append(list(map(float, data.strip('\n').split(" "))))

        # predict
        if(len(check_data_list) >= 15):
            diff = check_data_list[len(check_data_list)-1][3] - check_data_list[len(check_data_list)-2][3]
            if (diff > 10000):
                test_sample = samples.Sample.load_from_list(check_data_list)
                linearized_sample = test_sample.get_linearized(reshape=True)

                play_type = clf.predict(linearized_sample)

                if (play_type[0] == 0) :
                    if diff > 55000:
                        playsound('./sound/dda_strength_3.wav', block = False)
                        print("강 따")
                    elif diff > 40000:
                        playsound('./sound/dda_strength_2.wav', block = False)
                        print("중 따")
                    else :
                        playsound('./sound/dda_strength_1.wav', block = False)
                        print("소 따")

                else :
                    if diff > 55000:
                        playsound('./sound/duck_strength_3.wav', block = False)
                        print("강 덕")
                    elif diff > 40000:
                        playsound('./sound/duck_strength_2.wav', block = False)
                        print("중 덕")
                    else :
                        playsound('./sound/duck_strength_1.wav', block = False)
                        print("소 덕")

                # 다시 원래에 자리로 돌아오기 위해 일부 데이터를 버린다.
                count = 0
                while(count < 30):
                    count += 1
                    try :
                        data = serial.arduino.readline().decode('utf-8').strip()
                    except :
                        data = serial.arduino.readline().decode('utf-8').strip()

                # clear queue
                check_data_list = deque()

def gungchae(serial):
    data = ""
    check_data_list = deque()
    
    while(True):
        try :
            data = serial.arduino.readline().decode('utf-8').strip()
        except :
            data = serial.arduino.readline().decode('utf-8').strip()
        
        # queue에 데이터 삽입
        if len(check_data_list) >= max_deque_size :
            check_data_list.popleft()
            check_data_list.append(list(map(float, data.strip('\n').split(" "))))
        
        else :
            check_data_list.append(list(map(float, data.strip('\n').split(" "))))

        # predict
        if(len(check_data_list) >= 15):
            diff = check_data_list[len(check_data_list)-1][3] - check_data_list[len(check_data_list)-2][3]
            if (diff > 10000):
                if diff > 55000:
                    playsound('./sound/dda_strength_3.wav', block = False)
                    print("강 궁")
                elif diff > 40000:
                    playsound('./sound/dda_strength_2.wav', block = False)
                    print("중 궁")
                else :
                    playsound('./sound/dda_strength_1.wav', block = False)
                    print("소 궁")

                
                # 다시 원래에 자리로 돌아오기 위해 일부 데이터를 버린다.
                count = 0
                while(count < 30):
                    count += 1
                    try :
                        data = serial.arduino.readline().decode('utf-8').strip()
                    except :
                        data = serial.arduino.readline().decode('utf-8').strip()

                # clear queue
                check_data_list = deque()

if __name__ == '__main__':
# save mpu6050 AcX, AcY, AcZ GyX, GyY, GyZ data
    serial = Serial(*sys.argv[1:])
    if serial.connect() :
        stick_type = int(input("1. 궁채 2. 열채"))
        if stick_type == 2 :
            yeolchae(serial)
        else :
            gungchae(serial)
    


import sys
from utils import Serial

def main():
    # save mpu6050 AcX, AcY, AcZ GyX, GyY, GyZ data
    serial = Serial(*sys.argv[1:])
    if serial.connect():
        sample_type = input("input sample type: ")
        start = int(input("input sample file name start number: "))
        max_count = int(input("input how many sample: : "))
        serial.save_data(sample_type, start=start, max_count=max_count)



if __name__ == '__main__':
    main()
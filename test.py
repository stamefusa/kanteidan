import serial
import time

def main():
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=10)
    ser2 = serial.Serial("/dev/ttyACM1", 9600, timeout=10)
    time.sleep(3)
    ser.write(b"a;")
    ser2.write(b"a;")
    time.sleep(3)
    ser.write(b"b;")
    ser2.write(b"b;")
    time.sleep(0.5)
    ser.close()
    ser2.close()

if __name__=='__main__':
    main()

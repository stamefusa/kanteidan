import serial
import time

def main():
    ser_l = serial.Serial("/dev/ttyACM0", 9600, timeout=10)
    ser_r = serial.Serial("/dev/ttyACM1", 9600, timeout=10)
    time.sleep(3)
    ser_l.write(b"a;")
    ser_r.write(b"a;")
    time.sleep(3)
    ser_r.write(b"---0;")
    time.sleep(1)
    ser_r.write(b"--00;")
    time.sleep(1)
    ser_r.write(b"-000;")
    time.sleep(1)
    ser_r.write(b"0000;")
    time.sleep(1)
    ser_l.write(b"---0;")
    time.sleep(1)
    ser_l.write(b"--00;")
    time.sleep(1)
    ser_l.write(b"-000;")
    time.sleep(1)
    ser_l.write(b"1000;")
    time.sleep(1)
    ser_l.write(b"b;")
    ser_r.write(b"b;")
    time.sleep(0.5)
    ser_l.close()
    ser_r.close()

if __name__=='__main__':
    main()

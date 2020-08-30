import serial
import RPi.GPIO as GPIO
import random
import time

# 最大8桁の数字から左右の7セグそれぞれの点灯パターンのリストを返却
# in_valは文字列
def calc(in_val):
    in_val_len = len(in_val)
    dst_list = []
    for i in range(in_val_len+1):
        in_val_substr = "{:->8}".format(in_val[in_val_len-i:in_val_len])
        list_val = [in_val_substr[:4], in_val_substr[4:]]
        #print("list:"+str(list_val))
        dst_list.append(list_val)
    else:
        finish_val = "{:*>8}".format(in_val)
        finish_val_list = [finish_val[:4], finish_val[4:]]
        #print("finish:"+str(finish_val_list))
        dst_list.append(finish_val_list)
    return dst_list

def getPrice():
    seed = round(random.uniform(1.0, 9.9), 1)
    digit_list = [1000, 10000, 10000, 10000, 100000, 100000, 100000, 100000, 100000, 1000000, 1000000, 1000000, 1000000, 10000000]
    random.shuffle(digit_list)
    return int(digit_list[0]*seed)

def main():
    # BCMの番号でピンアサイン
    # $ gpio readall で確認出来る
    GPIO.setmode(GPIO.BCM)
    # BCM17(GPIO-0)をプルアップ抵抗を有効にして入力ピンに設定
    # スイッチのもう一方はGNDにつなぐ
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # シリアルポート設定
    ser_l = serial.Serial("/dev/ttyACM0", 9600, timeout=10)
    ser_r = serial.Serial("/dev/ttyACM1", 9600, timeout=10)
    time.sleep(3)
    print("ready")

    switch_val = GPIO.LOW
    old_switch_val = GPIO.LOW

    try:
        while True:
            switch_val = GPIO.input(17)
            if switch_val == GPIO.HIGH and old_switch_val == GPIO.LOW:
                print("switch on")
                ser_l.write(b"a;")
                ser_r.write(b"a;")
            elif switch_val == GPIO.LOW and old_switch_val == GPIO.HIGH:
                print("switch off")
                price = str(getPrice())
                print("Price:"+price)
                led_pattern = calc(price)
                for p in led_pattern:
                    time.sleep(1)
                    ser_l.write((p[0]+";").encode())
                    ser_r.write((p[1]+";").encode())
                    #print("left:"+p[0]+";")
                    #print("right:"+p[1]+";")
                else:
                    time.sleep(5)
                    ser_l.write(b"b;")
                    ser_r.write(b"b;")
                    time.sleep(0.5)
            old_switch_val = switch_val
            time.sleep(0.1)
    except KeyboardInterrupt:
        ser_l.write(b"b;")
        ser_r.write(b"b;")
        time.sleep(0.5)
        GPIO.cleanup()
        ser_l.close()
        ser_r.close()

if __name__=='__main__':
    main()

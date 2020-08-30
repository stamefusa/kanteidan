import RPi.GPIO as GPIO
import time

# BCMの番号でピンアサイン
# $ gpio readall で確認出来る
GPIO.setmode(GPIO.BCM)
# BCM17(GPIO-0)をプルアップ抵抗を有効にして入力ピンに設定
# スイッチのもう一方はGNDにつなぐ
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(17) == GPIO.LOW:
            print("low")
        else:
            print("high")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()


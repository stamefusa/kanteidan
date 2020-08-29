#define STATE_STOP 0
#define STATE_RANDOM 1
#define STATE_NUMBER 2

// ピンと光る7セグの対応
// 右下：6 左下：7 下：8 中央：9 左上：10 右上：11 上：12
boolean num_array[10][7] = {
  {0, 0, 0, 1, 0, 0, 0}, // 0ok
  {0, 1, 1, 1, 1, 0, 1}, // 1ok
  {1, 0, 0, 0, 1, 0, 0}, // 2ok
  {0, 1, 0, 0, 1, 0, 0}, // 3ok
  {0, 1, 1, 0, 0, 0, 1}, // 4ok
  {0, 1, 0, 0, 0, 1, 0}, // 5ok
  {0, 0, 0, 0, 0, 1, 0}, // 6ok
  {0, 1, 1, 1, 0, 0, 0}, // 7ok
  {0, 0, 0, 0, 0, 0, 0}, // 8ok
  {0, 1, 0, 0, 0, 0, 0} // 9ok
};

int digit_1 = 5; // 1の桁
int digit_10 = 4; // 10の桁
int digit_100 = 3; // 100の桁
int digit_1000 = 2; // 1000の桁

int del = 3; // ディレイ

int count = 0;
int digit_1_num = 0; // 1の桁で表示する数
int digit_10_num = 0; // 10の桁で表示する数
int digit_100_num = 0; // 100の桁で表示する数
int digit_1000_num = 0; // 1000の桁で表示する数

String digit_chars[4] = {"-", "-", "-", "-"};

int state = STATE_STOP;
String key = "";

void numPrint(int num) {
  for (int j = 0; j <= 6; j++) {
    digitalWrite(j + 6, num_array[num][j]);
  }
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10); // SerialでのString受信のタイムアウト設定（ms）

  pinMode(digit_1, OUTPUT); // 光る桁
  pinMode(digit_10, OUTPUT); // 光る桁
  pinMode(digit_100, OUTPUT); // 光る桁
  pinMode(digit_1000, OUTPUT); // 光る桁
  for (int i = 6; i <= 12; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    key = Serial.readStringUntil(';');
    key.trim();
    Serial.print("receive : ");
    Serial.println(key);

    if (key == "a") {
      state = STATE_RANDOM;
    } else if (key == "b") {
      state = STATE_STOP;
    } else {
      if (key.length() == 4) {
        state = STATE_NUMBER;
        for (int k = 0; k < 4; k++) {
          digit_chars[k] = key.charAt(k);
        }
      }
    }
  }

  //Serial.println(state);
  if (state == STATE_STOP) {
    dispInit();
  } else if (state == STATE_RANDOM) {
    dispRandom();
  } else if (state == STATE_NUMBER) {
    dispNumbers(digit_chars[3], digit_chars[2], digit_chars[1], digit_chars[0]);
  }
}

// 全LED消灯
void dispInit() {
  digitalWrite(digit_1, 0);
  digitalWrite(digit_10, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 0);
  delay(100);
}

// 指定の数字を桁ごとに表示
// "-"はランダムの数値を表示する
void dispNumbers(String digit_1_char, String digit_10_char, String digit_100_char, String digit_1000_char) {
  // 1の桁
  digitalWrite(digit_10, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 0);
  digitalWrite(digit_1, 1);
  digit_1_num = convertNum(digit_1_char, digit_1_num, count);
  numPrint(digit_1_num);
  delay(del);

  // 10の桁
  digitalWrite(digit_1, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 0);
  digitalWrite(digit_10, 1);
  digit_10_num = convertNum(digit_10_char, digit_10_num, count);
  numPrint(digit_10_num);
  delay(del);

  // 100の桁
  digitalWrite(digit_1, 0);
  digitalWrite(digit_10, 0);
  digitalWrite(digit_1000, 0);
  digitalWrite(digit_100, 1);
  digit_100_num = convertNum(digit_100_char, digit_100_num, count);
  numPrint(digit_100_num);
  delay(del);

  // 1000の桁
  digitalWrite(digit_1, 0);
  digitalWrite(digit_10, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 1);
  digit_1000_num = convertNum(digit_1000_char, digit_1000_num, count);
  numPrint(digit_1000_num);
  delay(del);

  count = (count + 1) % 5;
}

// 全LEDを0～9の中からランダムで表示
void dispRandom() {
  if (count == 0) {
    digit_1_num = random(9);
    digit_10_num = random(9);
    digit_100_num = random(9);
    digit_1000_num = random(9);
  }

  // 1の桁
  digitalWrite(digit_10, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 0);
  digitalWrite(digit_1, 1);
  numPrint(digit_1_num);
  delay(del);

  // 10の桁
  digitalWrite(digit_1, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 0);
  digitalWrite(digit_10, 1);
  numPrint(digit_10_num);
  delay(del);

  // 100の桁
  digitalWrite(digit_1, 0);
  digitalWrite(digit_10, 0);
  digitalWrite(digit_1000, 0);
  digitalWrite(digit_100, 1);
  numPrint(digit_100_num);
  delay(del);

  // 1000の桁
  digitalWrite(digit_1, 0);
  digitalWrite(digit_10, 0);
  digitalWrite(digit_100, 0);
  digitalWrite(digit_1000, 1);
  numPrint(digit_1000_num);
  delay(del);

  count = (count + 1) % 5;
}

// 桁ごとのシリアル送信値から表示する数字への変換
int convertNum(String s, int now_num, int c) {
  int n = now_num;
  // -はランダム表示
  if (s == "-") {
    // タイミングがあったときだけランダム値に
    if (c == 0) {
      n = random(9);
    }
  // それ以外は数字が来る
  } else {
    n = s.toInt();
    if (n < 0 || n > 9) {
      n = 0;
    }
  }
  return n;
}

import random

seed = round(random.uniform(1.0, 9.9), 1)
digit_list = [1000, 10000, 10000, 10000, 100000, 100000, 100000, 100000, 100000, 1000000, 1000000, 1000000, 1000000]
random.shuffle(digit_list)
print(int(digit_list[0]*seed))

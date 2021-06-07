import os
import time
pauza = 0
f_s = 0
s_s = 0
f_m = 0
s_m = 0
f_h = 0
s_h = 0


while True:
    os.system('clear')
    f_s = f_s + 1
    if f_s == 10:
        f_s = 0
        s_s = s_s+1
    if s_s == 6:
        f_s = 0
        s_s = 0
        f_m = f_m+1
    if f_m == 10:
        f_s = 0
        s_s = 0
        f_m = 0
        s_m = s_m+1
    if s_m == 6:
        f_s = 0
        s_s = 0
        f_m = 0
        s_m = 0
        f_h = f_h + 1
    if f_h == 10:
        f_s = 0
        s_s = 0
        f_m = 0
        s_m = 0
        f_h = 0
        s_h = s_h + 1
    print(f"{s_h}{f_h}:{s_m}{f_m}:{s_s}{f_s}")
    time.sleep(0.00001)

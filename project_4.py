#  @OLLIT_DEV

import threading
import time
fayl="bitiklar.txt"
tekst=""

def read_files():
    global fayl,tekst

    while True:
        with open("bitiklar.txt","r") as f:
            tekst= f.read()

def repetition():
    for x in range(8):
        print(tekst)
        time.sleep(1)


t1=threading.Thread(target=read_files)
t2=threading.Thread(target=repetition)
t1.start()
t2.start()

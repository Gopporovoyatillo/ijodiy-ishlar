# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:12:33 2021

@author: Admin
"""

import random
def sontop(x=10):
    tasodifiy_son=random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi?")
    hatakat=0
    while True:
        hatakat+=1
        taxmin=int(input(">>>"))
        if taxmin<tasodifiy_son:
            print(f"Xato men o'ylagan son {taxmin} dan  kattaroq")
        elif taxmin>tasodifiy_son:
            print(f"Xato men o'ylagan son {taxmin} dan  kichikroq")
        else:
            break
    print(f"Tabriklayman siz {hatakat} ta urunishda topdingiz!!!")
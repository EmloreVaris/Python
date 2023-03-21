import math
import time
import random
import os
import sys

def t(phrase, wait=.03):
    for letter in phrase:
        print(letter, end="")
        if not letter == phrase[-1]:
            time.sleep(wait)
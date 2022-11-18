import random
from scripts.blocks import *
class generator:
    def gen():
        for i in range(16):
            y, x = random.randint(0,20), random.randint(0,20)
            for dx in range(random.randint(0,10)):
                for dy in range(random.randint(0,10)):
                    
                    block(x*250+dx*25,y*250+dy*25,"blue")
            ly, lx = random.randint(0,20), random.randint(0,20)
            for rx in range(random.randint(0,10)):
                for ry in range(random.randint(0,10)):
                    
                    block(lx*250+rx*25,ly*250+ry*25,"gold")
            
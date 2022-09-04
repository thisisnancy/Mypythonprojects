# water - 3 litre water (9 am to 5 pm)-EVERY 40 MIN
# eyes- every 30 min-doneey
# exercise - every 45 min -doneex
# use python module (PYGAME MODULE) FOR SOUND 

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a= input()
        if a==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open ("logs.py","a") as op:
        op.write(f"{msg} {datetime.now()} \n")

if __name__=='__main__':
    # musiconloop("water.wav","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watertime=40*60
    eyestime=30*60
    exercisetime=45*60

    while True:
        if time()-init_water>watertime:
            print("pani peelo")
            musiconloop("water.wav","pi liya")
            init_water=time()
            log_now("pani piya hai")

        if time()-init_eyes>eyestime:
            print("ankhe ghumao")
            musiconloop("eyes.wav","ghuma li")
            init_eyes=time()
            log_now("ghumali hai")
        if time()-init_exercise>exercisetime:
            print("hath paer chalao")
            musiconloop("exercise.wav","chala liye")
            init_eyes=time()
            log_now("hath paer chalaye")
   

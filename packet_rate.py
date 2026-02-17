#Jesse France
#2/16/2026
#Sends a fake packet to a function and tracks the rate

import random

packet1 = {
    "status": True,
}
packet2 = {
    "status": False,
}

fails = 0
passes = 0
rate = 0

def choosePacketType(packet: dict, packet1: dict)-> bool:
    num = random.random()

    if num > .5:
        return packet1["status"]
    else:
        return packet["status"]
    
def trackRate(rate: int)-> list:
    global passes, fails
    packetToGet = choosePacketType(packet1, packet2)
    if packetToGet is True:
        passes += 1
    else:
        fails += 1
    rate += 1
    return [passes, fails, rate]

passed = False   
while True:
    if passed == False:
        rate = 0
        passed = True
    get = random.random()
    if get < .5:
        if rate == 0:
            continue
        else:
            rate -= 1
        continue
    else:
        tracked = trackRate(rate)
        rate = tracked[2]
        print(tracked)
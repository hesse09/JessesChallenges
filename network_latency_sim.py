import random 
import time

dropped = 0
passed = 0
throttled = 0
total = 0

class OutputColors:
    Red = "\033[91m"
    Green = "\033[92m"
    Yellow = "\033[93m"
    Reset = "\033[0m"

p = True
while p == True:
    print("Hello! Configure your network!")
    try:
        wifiSpeed = int(input("Enter your wifi speed you wish to simulate (Mbps, capped at 10GB): "))
        fiber = input("Do you wish to simulate fiber? (y/n): ").lower()
    except:
        print(f"{OutputColors.Red} Enter a valid number! {OutputColors.Reset}")
        continue
    numberShifterAm = 1200
    if fiber == "y":
        numberShifterAm -= 100
    elif fiber == "n":
        pass
    else:
        print(f"{OutputColors.Red} Enter a valid fiber response! {OutputColors.Reset}")
        continue

    if wifiSpeed > 10000:
     print("That is too high, capping at 10GB")
     continue

    wifiSpeed = (wifiSpeed / 10000) * (1200 / numberShifterAm)
    p = False
    
def network_simulation()-> int:
    if random.random() < wifiSpeed:
        return random.randrange(0, 100)
    else:
        return random.randrange(100, 500)
    
def check_for_lag(latency: int)-> dict:
    global dropped, passed, throttled, total
    waitTime = latency / 1000
    packetStatus = None
    if latency <= 100:
        time.sleep(waitTime) #mimic latency
        passed += 1
        packetStatus = "Passed"
    elif latency > 100 and latency <= 300:
        waitTime = .10 + waitTime #add a throttle
        time.sleep(waitTime) #mimic latency
        throttled += 1
        packetStatus = "Throttled"
    elif latency > 300:
        dropped += 1
        packetStatus = "Dropped"
    total += 1
    return {
        "status": packetStatus,
        "Packet Latency": f"{waitTime:.3f}ms",
        "Passed Packets": passed,
        "Throttled Packets": throttled,
        "Dropped Packets": dropped,
        "Total Packets": total,
    }

while True:
    try:
        num = network_simulation()
        data = check_for_lag(num)
        if num <= 100:
            clr = OutputColors.Green
        elif num <= 300:
            clr = OutputColors.Yellow
        else:
            clr = OutputColors.Red
            
        print(f"{clr}{data['status']:<10} | Latency: {data['Packet Latency']:<8} | P: {data['Passed Packets']:<5} T: {data['Throttled Packets']:<5} D: {data['Dropped Packets']:<5}{OutputColors.Reset}")
    except KeyboardInterrupt:
        print(f"\n{OutputColors.Reset}Ending...")
        break

inputList:list = [4, 4, 1, 6, 1, 6, 6, 2]
freq:dict = {}

def freqCounter(inputList: list, frequency: dict)-> dict:

    if len(inputList) == 0:
        return "Please enter a valid list"
    
    for i in inputList:
        if i  in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return frequency

def freqToList(freq:dict)-> list:
    sortedList: list = []
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    for k, v in sorted_items:
        for i in range(v):
            sortedList.append(k)
    
    return sortedList




freq = freqCounter(inputList, freq)
print(freqToList(freq))




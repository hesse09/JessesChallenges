def frequency_counter(text: str) -> dict:
    tokens: str = text.split(" ")
    frequency: dict = {}
    for t in tokens:
        if t in frequency:
            frequency[t] += 1
        else:
            frequency[t] = 1
    return frequency


while True:
    try:
        text = str(input("Enter some text: "))
        frequncey_table = frequency_counter(text)
        print(frequncey_table)
        for k, v in frequncey_table.items():
            print("There is", v, "of", k, "in your sentence.")
    except KeyboardInterrupt:
        print("exiting")
        exit()

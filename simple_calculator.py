print("Welcome to Jesses calculator!\n"
      "Use [M] to quit")


while True:
    var = input("Enter a number (or exit code): ")
    if var == "m" or var == "M":
      print("Exiting...")
      break
    try:
     var = int(var)
     var2 = int(input("Input another number: "))
    except:
      print("That is not a number, try again!")
      continue
    operator = input ("Enter an operator (+, -, *, /): ").strip()
    if operator == "+":
      output = var + var2
    elif operator == "-":
      output = var - var2
    elif operator == "*":
      output = var * var2
    elif operator == "/":
      if var2 == 0:
        print("You can not divide by 0")
        continue
      output = var / var2

    print(output)
      

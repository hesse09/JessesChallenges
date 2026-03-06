#Jesse France
#3/6/26
#Converts base 10 to binary

#VARS
userNum: int = 0
#HELPERS
def binary_conversion(num: int)-> tuple[bool, str]:
    if num < 0:
        return (False, "Enter a positive number")
    final: str = ""
    while num > 0:
        valueToAdd: str = num % 2
        final = str(valueToAdd) + final
        num = num // 2
    return (True, final)
#RUN
print("Please enter the integer to convert to binary: ", end='')
userNum = int(input())

success, binary = binary_conversion(userNum)
if not success:
    print("Error: %s!" % binary)
    
print("The value of %d in binary is %s!" % (userNum, binary))

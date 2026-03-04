#Jesse France
#3/4/26


def max(num1: int, num2: int)-> tuple[int, str]:
    final: int
    maxP: str
    if num1 > num2:
        final = num1
        maxP =  "num1"
    elif num1 == num2:
        final = num1
        maxP = "a tie"
    else:
        final = num2
        maxP =  "num2"
        
    return (final, maxP)

print("Enter first number: ", end='');
a = eval(input())
print("Enter second number: ", end='');
b = eval(input())

maxNum = max(a,b)
print("The max number was %s, with a value of %d!" % (maxNum[1], maxNum[0]))

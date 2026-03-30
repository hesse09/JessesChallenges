#VARS
user_input: str = ""
user_key: int = 0

#HELPERS
def encrypt(plain_text: str, cipher_key: int)-> bool | str:
    output_text: str = ""
    for indx in range(0, len(plain_text)):
        singleChar = plain_text[indx].upper()
        
        if singleChar >= "A" and singleChar <= "Z":
            singleChar = chr(ord(singleChar) - cipher_key)
            
            if singleChar < "A":
                singleChar = chr(ord(singleChar) + 26)
            
        output_text = output_text + singleChar
        
            
    return True, output_text

#MAIN

print("Please enter your message you which to encrypt:", end="")
user_input = input()

print("Please enter your key:", end="")
user_key = int(input())

success, encrypted = encrypt(user_input, user_key)

if success:
    print("Your message is: %s" % encrypted)
else:
    print("ERROR: %s" % encrypted)

from werkzeug.security import generate_password_hash, check_password_hash

dataStore: dict = {}
usernameIndex: dict = {}

def register(req_username, req_password):
    if req_username in usernameIndex:
        return {"status": False, "issue": "Username taken"}
            
    userId = len(dataStore) + 1
    if len(req_username) < 3 or len(req_username) > 12:
        return {"status": False, "issue": "Username too small/long"}
    
    if len(req_password) < 6:
        return {"status": False, "issue": "Please enter a valid password"}
    
    usernameIndex[req_username] = userId
    finalPassword = generate_password_hash(req_password)
    payload = dataStore[userId] = {
        "username": req_username,
        "password": finalPassword,
    }

    return {"status": True}
    

def login(username, password):
    if username not in usernameIndex:
        return {"status": False, "issue": "No username found"}
    userId = usernameIndex[username]
    if check_password_hash(dataStore[userId]["password"], password):
        return {"status": True}
    else:
        return {"status": False, "issue": "Failed to auth"}
    
print("Hello! Make an account!\n\n\Ctrl+C to exit code.")
while True:
    try:
        print("Would you like to sign up or login? [s/l]")
        mode = input(":")
        if mode == "s":
            username = input("Enter your username (min3,max12):")
            password = input("Please enter your password (min8):")
            success = register(username, password)
            if success["status"] == True:
                print("Signed up now try and login!\n\n ")
                continue
            else:
                print(success["issue"])
                continue
        elif mode == "l":
            username = input("Enter your username (min3,max12):")
            password = input("Please enter your password (min8):")
            success = login(username, password)
            if success["status"] == True:
                print("Logged in successful!\n\n ")
            else:
                print(success["issue"])
        else:
            print("ERROR: ENTER A VALID MODE")
    except KeyboardInterrupt:
        print("Exiting")
        exit()

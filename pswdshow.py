names = ["desmond", "caden", "temitope", "donovan", "vincent", "rawlin"]
passwordDeb = ["group1"]
passwordUbun = ["desmond", "caden", "temitope", "donovan", "vincent", "rawlin"]

while True:
    try:
        askOs = int(input("Debian (1) or Ubuntu (2)? : "))
        if askOs == 1:
            try:
                userNameAsk = input("Enter a username: ")
                print("Password for user is: ", passwordDeb[0])
            except:
                print("Make sure username is valid...")
        if askOs == 2:
            try:
                userNameAsk = input("Enter a username: ")
                if userNameAsk == "desmond":
                    print("Password for user is: ", passwordUbun[0])
                if userNameAsk == "caden":
                    print("Password for user is: ", passwordUbun[1])
                if userNameAsk == "temitope":
                    print("Password for user is: ", passwordUbun[2])
                if userNameAsk == "ddonovan":
                    print("Password for user is: ", passwordUbun[3])
                if userNameAsk == "vincent":
                    print("Password for user is: ", passwordUbun[4])
                if userNameAsk == "rawlin":
                    print("Password for user is: ", passwordUbun[5])
            except:
                print("Make sure username is valid...")
    except:
        print("Make sure input is valid...")

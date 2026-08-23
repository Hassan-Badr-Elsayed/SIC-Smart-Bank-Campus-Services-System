Deposit = "0"
Withdraw = "1"
Transfer = "2"
Transaction_history = "3"
Reports = "4"
Branch_ATM_status = "5"
Update_personal_info = "6"
Exit = "7"

target_user = "no one"



users = [
    {
        "id": 1,
        "profile": {
            "name": "Ahmed",
            "password": "1233",
            "phone": "01011111111",
            "email": "example@gmail.com",
            "gender": "Male",
            "age": 20,
            "city": "Fayoum",
            "account type": "Savings"
        },
        "wallet": {
            "balance" : 0,
            "currency" : "EGP"
        },
        "hestory" :[]      
    },
    {
        "id": 2,
        "profile": {
            "name": "Mohamed",
            "password": "124",
            "phone": "01011111112",
            "email": "Mohmaed@gmail.com",
            "gender": "Male",
            "age": 20,
            "city": "cairo",
            "account type": "Savings"
        },
        "wallet": {
            "balance" : 0,
            "currency" : "EGP"
        },
        "hestory" :[]      
    }
]

# The beginning of the program
while True:
    print("\n******** SIC SMART BANK SYSTEM ********")
    print("""If you already have an account, enter login
If you do not have an account, enter register
To close the system, enter exit
    """)
    
    option = input("> ").lower()

    if option == "register":
        print("=====REGISTER=====")
        name = input("Please enter your name: ")
        while not name:
            print("Empty Field !")
            name = input("Please enter your name: ")

        # Password field
        password = input("Please enter your password: ")
        while not password:
            print("Empty Field !")
            password = input("Please enter your password: ")
        
        # Phone 
        while True: 
            phone = input("Please enter your phone: ")
            phone_check = False
            
            # Phone Check 
            for u in users:
                if u["profile"]["phone"] == phone:
                    phone_check = True
                    break
        
            if phone_check:
                print("Sorry! This Number already exists in the system.")
            elif not phone:
                print("Phone Number is Empty!")
            else:
                break

        # Email
        while True:
            email = input("Please enter your Email: ")
            email_check = False
            
            # Email Check
            for u in users:
                if u["profile"]["email"] == email:
                    email_check = True
                    break
            
            if email_check:
                print("Sorry! This Email already exists in the system.")
            elif not email:
                print("Email is Empty!")
            else:
                break

        # Other fields          
        gender = input("Please enter your gender (Male/Female): ")

        # Age
        age = -1
        while age < 0:
            age_input = input("Please enter your age: ")
            if age_input.isdigit():
                age = int(age_input)
                if age < 0:
                    print("Invalid age input!")
            else:
                print("Invalid age input! Numbers only.")

        city = input("Please enter your city: ")
        account_type = input("Please enter your account type: ")

        # ID User (Find max ID first, then add 1 once)
        max_id = 0
        for u in users:
            if u["id"] > max_id:
                max_id = u["id"]
        new_id = max_id + 1

        new_user = {
            "id": new_id,
            "profile": {
                "name": name,
                "password": password,
                "phone": phone,
                "email": email,
                "gender": gender,
                "age": age,
                "city": city,
                "account type": account_type
            },
            "wallet": {
                "balance" : 0,
                "currency" : "EGP"
        },
            "hestory" :[]      
        }

        users.append(new_user)
        print(f"Sign up successful. Your ID is {new_id}")

    # Login Page
    elif option == "login":
        print("=====LOGIN PAGE=====")
        
        # ID Check
        ID_check = False
        cureent_user = None

        while not ID_check:
            id_input = input("Please enter your ID: ")
            if not id_input.isdigit():
                print("Invalid ID format!")
                continue

            user_id = int(id_input)

            for u in users:
                if u["id"] == user_id:
                    cureent_user = u
                    ID_check = True
                    break
            
            if cureent_user is None:
                print("Invalid ID")

        # Password Verification
        attemp = 3
        login_success = False

        while attemp > 0:
            password = input(f"Please enter your password ({attemp} attempts left): ")
            
            if cureent_user["profile"]["password"] == password:
                n = cureent_user["profile"]["name"]  
                print(f"\nHello {n}! Welcome back.")
                login_success = True
                break
            else:
                attemp -= 1
                print("Wrong password.")

        if not login_success:
            print("Maximum failed attempts reached. Returning to main menu...\n")
        else:
            # ===================== AFTER THIS PAGE: OPERATION MENU ===================
            print(f"\n--- User Menu for {cureent_user['profile']['name']} ---")
    ######################################Hassan###########################################################
            while True:

                print(f"*************** Welcome back {cureent_user["profile"]["name"]} ***************")
                print("[0] Deposit")
                print("[1] Withdraw")
                print("[2] Transfer")
                print("[3] Transaction history")
                print("[4] Reports")
                print("[5] Branch/ATM status")
                print("[6] Update personal info")
                print("[7] Exit")
                

                user_input = input("please enter what do you want to do: ")
                    

                if (user_input == Deposit):
                    deposit_value,currency = input("please enter amount and currency: ").split()
                    if(deposit_value.isdigit()):
                        deposit_value = int(deposit_value)

                        if (deposit_value <= 0 and (currency != "EGP" and currency != "SAR" and currency != "USD")):
                            print("Invalid value and currency")
                            continue
                        elif (deposit_value <= 0):
                            print("Invalid value")
                            continue
                        elif (currency != "EGP" and currency != "SAR" and currency != "USD"):
                            print("Invalid value")
                            continue

                        if (currency == "SAR" or currency == "USD" or currency == "EGP"):
                            if(currency == "SAR"):
                                cureent_user["wallet"][currency] = "SAR"
                                amount_in_egp = deposit_value *9
                                transaction_msg = f"Deposit: {deposit_value} {currency} (+{amount_in_egp} EGP)"
                                cureent_user["hestory"].append(transaction_msg)
                                cureent_user["wallet"]["balance"] = amount_in_egp


                            elif (currency == "USD"):
                                cureent_user["wallet"][currency] = "USD"
                                amount_in_egp = deposit_value *30
                                transaction_msg = f"Deposit: {deposit_value} {currency} (+{amount_in_egp} EGP)"
                                cureent_user["hestory"].append(transaction_msg)
                                cureent_user["wallet"]["balance"] = amount_in_egp

                            else:
                                cureent_user["wallet"][currency] = "EGP"
                                amount_in_egp = deposit_value
                                transaction_msg = f"Deposit: {deposit_value} {currency}"
                                cureent_user["hestory"].append(transaction_msg)
                                cureent_user["wallet"]["balance"] = amount_in_egp
                    else:
                        print("Invalid input")
                        print("the process isn't success")
                        continue
        ########################################################################################################################
                elif (user_input == Withdraw):    
                    withdraw_value = input("please enter the value: ")
                    if(withdraw_value.isdigit()):
                        withdraw_value = int(withdraw_value)
                        if(withdraw_value <= 0):
                            print("Invalid input")
                            print("the process isn't sucsess please try again")
                            continue
                        else:
                            if(withdraw_value > cureent_user["wallet"]["balance"]):
                                print("you don't have enogh money")
                                print("the process isn't sucsess")
                                continue
                            else:
                                cureent_user["wallet"]["balance"] -= withdraw_value

                                transaction_msg = f"Withdraw: {withdraw_value}"
                                cureent_user["hestory"].append(transaction_msg)
                                print("process success")
                    else:
                        print("Invalid value")
                        print("the process isn't sucsess please try again")

        ############################################################################################################################
                elif (user_input == Transfer):
                    id_target_user = int(input("please enter the id of the target user: "))
                    for u in users:
                        if u["id"] == id_target_user:
                            target_user = u
                    if (target_user == cureent_user):
                        print("you can't transfer to your self")
                        continue
                    elif(target_user == "no one"):
                        print("Invalid Id number")
                        continue


                    transfer_value = input("Enter The Transfer value: ")

                    if (transfer_value <= 0):
                        print("Invalid input")
                        print("the Transfer isn't sucsess please try again")
                        continue
                    else:
                        if(transfer_value > cureent_user["wallet"]["balance"]):
                            print("you don't have enogh money please deposit money and try again")
                            print("the Transfer isn't sucsess ")
                        elif(transfer_value < cureent_user["wallet"]["balance"]):
                            cureent_user["wallet"]["balance"] -= transfer_value
                            transaction_msg = f"transfer to {target_user["profile"]["name"]}: {transfer_value}"
                            cureent_user["hestory"].append(transaction_msg)

                            target_user["wallet"]["balance"] += transfer_value
                            transaction_msg = f"transfer from {cureent_user["profile"]["name"]}: {transfer_value}"
                            cureent_user["hestory"].append(transaction_msg)
                            print("Transfer success")

        ###########################################################################################################################
                elif (user_input == Transaction_history):
                    if (cureent_user["hestory"] == []):
                        print("you don't have Transaction_history")
                        continue
                    else:
                        for i in cureent_user["hestory"]:
                            print(i)
        ##################################################################################################################################
                elif (user_input == Reports):
                    print()
                elif (user_input == Branch_ATM_status):
                    print()
                elif (user_input == Update_personal_info):
                    print()
                elif (user_input == Exit):
                    print("End session")
                    break
                else:
                    print("Invalid Input")
                    print("enter number from the menu")





                    
            # You can place your user menu / update personal info here
            
    elif option == "exit":
        print("Have a nice day! Goodbye :) ")
        break
    else:
        print("Invalid Input. Please Try again.")





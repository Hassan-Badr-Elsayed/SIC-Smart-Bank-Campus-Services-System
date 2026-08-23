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
        }
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
        }
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
            }
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
            # You can place your user menu / update personal info here
            
    elif option == "exit":
        print("Have a nice day! Goodbye :) ")
        break
    else:
        print("Invalid Input. Please Try again.")
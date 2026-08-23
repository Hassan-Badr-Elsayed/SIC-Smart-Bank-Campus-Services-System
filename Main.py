import copy
from collections import defaultdict

# Constant menu options
Deposit = "0"
Withdraw = "1"
Transfer = "2"
Transaction_history = "3"
Branch_ATM_status = "4"
Update_personal_info = "5"
Exit = "6"

# 4x4 ATM Matrix (1 = Available, 0 = Out of Service)
atm_matrix = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1]
]

# Initial users with explicit roles
users = [
    {
        "id": 1,
        "profile": {
            "name": "Ahmed Admin",
            "password": "admin",
            "phone": "01000000000",
            "email": "admin@bank.com",
            "gender": "Male",
            "age": 35,
            "city": "Cairo",
            "account type": "Admin",
            "role": "Admin"
        },
        "wallet": {"balance": 0, "currency": "EGP"},
        "settings": {"active": True, "vip": False, "failed_logins": 0},
        "history": [],
        "snapshot": None
    },
    {
        "id": 2,
        "profile": {
            "name": "Mohamed",
            "password": "124",
            "phone": "01011111112",
            "email": "Mohamed@gmail.com",
            "gender": "Male",
            "age": 20,
            "city": "Cairo",
            "account type": "Savings",
            "role": "VIP"
        },
        "wallet": {"balance": 500, "currency": "EGP"},
        "settings": {"active": True, "vip": True, "failed_logins": 0},
        "history": [],
        "snapshot": None
    },
    {
        "id": 3,
        "profile": {
            "name": "Sara",
            "password": "999",
            "phone": "01011111113",
            "email": "sara@gmail.com",
            "gender": "Female",
            "age": 22,
            "city": "Alexandria",
            "account type": "Checking",
            "role": "User"
        },
        "wallet": {"balance": 2000, "currency": "EGP"},
        "settings": {"active": True, "vip": False, "failed_logins": 0},
        "history": [],
        "snapshot": None
    }
]

def reports_menu():
    """Admin Reports Menu"""
    while True:
        print("\n***************** ADMIN REPORTS MENU *****************")
        print("1. Duplicate detection")
        print("2. User set analysis")
        print("3. Transaction frequency report")
        print("4. Membership check")
        print("5. All accounts report")
        print("6. Logout / Exit Reports")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            phone_list = [u["profile"]["phone"] for u in users]
            email_list = [u["profile"]["email"] for u in users]

            dup_phones = [p for p in set(phone_list) if phone_list.count(p) > 1]
            dup_emails = [e for e in set(email_list) if email_list.count(e) > 1]

            print("\n========== DUPLICATE REPORT ==========")
            print("Duplicate phone numbers:", dup_phones if dup_phones else "None")
            print("Duplicate emails:", dup_emails if dup_emails else "None")

        elif choice == "2":
            active_users = {u["profile"]["name"] for u in users if u["settings"].get("active")}
            vip_users = {u["profile"]["name"] for u in users if u["profile"]["role"] == "VIP"}
            failed_login_users = {u["profile"]["name"] for u in users if u["settings"].get("failed_logins", 0) > 0}
            transfer_users = {
                u["profile"]["name"] for u in users 
                if any(t["type"] == "transfer" for t in u["history"])
            }

            print("\n============== USER SEGMENTS ==========")
            print("Active users:", active_users)
            print("VIP users:", vip_users)
            print("Failed logins:", failed_login_users)
            print("Transfer users:", transfer_users)
            
            print("\nActive OR VIP (Union):", active_users.union(vip_users))
            print("Active AND VIP (Intersection):", active_users.intersection(vip_users))
            print("Active but NOT VIP (Difference):", active_users.difference(vip_users))
            print("Active or VIP, NOT both (Symmetric Diff):", active_users.symmetric_difference(vip_users))

        elif choice == "3":
            freq = defaultdict(int)
            for u in users:
                for t in u["history"]:
                    freq[t["type"]] += 1
            print("\n========== TRANSACTION FREQUENCY ==========")
            for t_type, count in freq.items():
                print(f"{t_type}: {count}")

        elif choice == "4":
            check_name = input("Enter user name: ").strip()
            found = any(u["profile"]["name"].lower() == check_name.lower() for u in users)
            print(f"Is user registered: {found}")

        elif choice == "5":
            print("\n========== ALL ACCOUNTS REPORT ==========")
            for u in users:
                print(f"User ID: {u['id']} | Role: {u['profile']['role']}")
                print("Profile info:", u["profile"])
                print("-" * 20)

        elif choice == "6":
            print("Exiting Reports Menu...")
            break
        else:
            print("Invalid choice, try again.")

# The beginning of the main program
while True:
    print("\n******** SIC SMART BANK SYSTEM ********")
    print("""If you already have an account, enter login
If you do not have an account, enter register
To close the system, enter exit""")
    
    option = input("> ").lower().strip()

    if option == "register":
        print("=====REGISTER=====")
        name = input("Please enter your name: ").strip()
        while not name:
            print("Empty Field !")
            name = input("Please enter your name: ").strip()

        password = input("Please enter your password: ").strip()
        while not password:
            print("Empty Field !")
            password = input("Please enter your password: ").strip()
        
        while True: 
            phone = input("Please enter your phone: ").strip()
            if any(u["profile"]["phone"] == phone for u in users):
                print("Sorry! This Number already exists in the system.")
            elif not phone:
                print("Phone Number is Empty!")
            else:
                break

        while True:
            email = input("Please enter your Email: ").strip()
            if any(u["profile"]["email"] == email for u in users):
                print("Sorry! This Email already exists in the system.")
            elif not email:
                print("Email is Empty!")
            else:
                break

        gender = input("Please enter your gender (Male/Female): ").strip()

        age = -1
        while age < 0:
            age_input = input("Please enter your age: ").strip()
            if age_input.isdigit():
                age = int(age_input)
                if age < 0:
                    print("Invalid age input!")
            else:
                print("Invalid age input! Numbers only.")

        city = input("Please enter your city: ").strip()
        account_type = input("Please enter your account type: ").strip()

        # Select Role
        print("Select account role: [1] Standard User, [2] VIP User")
        role_choice = input("> ").strip()
        user_role = "VIP" if role_choice == "2" else "User"

        max_id = max([u["id"] for u in users], default=0)
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
                "account type": account_type,
                "role": user_role
            },
            "wallet": {"balance": 0, "currency": "EGP"},
            "settings": {"active": True, "vip": (user_role == "VIP"), "failed_logins": 0},
            "history": [],
            "snapshot": None
        }

        users.append(new_user)
        print(f"Sign up successful. Your ID is {new_id} ({user_role} account)")

    elif option == "login":
        print("=====LOGIN PAGE=====")
        
        current_user = None
        while current_user is None:
            id_input = input("Please enter your ID: ").strip()
            if not id_input.isdigit():
                print("Invalid ID format!")
                continue

            user_id = int(id_input)
            current_user = next((u for u in users if u["id"] == user_id), None)
            
            if current_user is None:
                print("Invalid ID")

        attemp = 3
        login_success = False

        while attemp > 0:
            password = input(f"Please enter your password ({attemp} attempts left): ").strip()
            
            if current_user["profile"]["password"] == password:
                login_success = True
                current_user["settings"]["failed_logins"] = 0
                break
            else:
                attemp -= 1
                current_user["settings"]["failed_logins"] += 1
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
                            
                        deposit_value = int(raw_dep[0])
                        currency = raw_dep[1].upper()

                        if deposit_value <= 0 or currency not in ["EGP", "SAR", "USD"]:
                            print("Invalid value or currency.")
                            continue

                        rates = {"EGP": 1, "SAR": 9, "USD": 30}
                        amount_in_egp = deposit_value * rates[currency]

                        current_user["wallet"]["balance"] += amount_in_egp
                        current_user["history"].append({
                            "type": "deposit",
                            "details": f"Deposit: {deposit_value} {currency} (+{amount_in_egp} EGP)"
                        })
                        print("Deposit Successful!")

                    elif user_input == Withdraw:    
                        withdraw_val = input("Please enter value: ").strip()
                        if withdraw_val.isdigit():
                            withdraw_value = int(withdraw_val)
                            if withdraw_value <= 0:
                                print("Invalid value.")
                            elif withdraw_value > current_user["wallet"]["balance"]:
                                print("You don't have enough money.")
                            else:
                                current_user["wallet"]["balance"] -= withdraw_value
                                current_user["history"].append({
                                    "type": "withdraw",
                                    "details": f"Withdraw: {withdraw_value} EGP"
                                })
                                print("Withdrawal successful.")
                        else:
                            print("Invalid value.")

                    elif user_input == Transfer:
                        target_id_in = input("Please enter target user ID: ").strip()
                        if not target_id_in.isdigit():
                            print("Invalid Target ID.")
                            continue
                            
                        id_target = int(target_id_in)
                        target_user = next((u for u in users if u["id"] == id_target), None)

                        if target_user is None:
                            print("Invalid ID number.")
                            continue
                        if target_user["id"] == current_user["id"]:
                            print("You can't transfer to yourself.")
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
                    while True:
                        print("\n================================")
                        print("***************** REPORTS MENU*****************")
                        print("========================================")
                        print("1. Duplicate detection")
                        print("2. User set analysis")
                        print("3. transaction reports")
                        print("4. Membership check")
                        print("5. back to main menu")
                        choice = input("enter choice: ")

                        if choice == "1":
                            # DUPLICATE REPORT
                            phone_list = []
                            email_list = []

                            for username in users:
                                phone_list.append(users[username].get("phone"))
                                email_list.append(users[username].get("email"))

                            duplicate_phones = []
                            for phone in phone_list:
                                if phone_list.count(phone) > 1 and phone not in duplicate_phones:
                                    duplicate_phones.append(phone)

                            duplicate_emails = []
                            for email in email_list:
                                if email_list.count(email) > 1 and email not in duplicate_emails:
                                    duplicate_emails.append(email)
                            print("\n========== DUPLICATE REPORT ==========")

                            if len(duplicate_phones) == 0:
                                print("Duplicate phone numbers: None")
                            else:
                                print("Duplicate phone numbers:", duplicate_phones)

                            if len(duplicate_emails) == 0:
                                print("Duplicate emails: None")
                            else:
                                print("Duplicate emails:", duplicate_emails)

                        elif choice == "2":
                            # SET ANALYSIS
                            active_users = set()
                            vip_users = set()
                            failed_login_users = set()
                            transfer_users = set()

                            for username in users:
                                if users[username].get("active") == True:
                                    active_users.add(username)

                                if users[username].get("vip") == True:
                                    vip_users.add(username)

                                if users[username].get("failed_logins", 0) > 0:
                                    failed_login_users.add(username)

                                history = users[username].get("history", [])
                                for transaction in history:
                                    if transaction.get("type") == "transfer":
                                        transfer_users.add(username)
                                        break

                            print("\n============== USER SEGMENTS ==========")
                            print("Active users:", active_users)
                            print("VIP users:", vip_users)
                            print("Users with failed login:", failed_login_users)
                            print("Users with transfers:", transfer_users)

                            print("\n========== UNION ==============")
                            active_or_vip = active_users.union(vip_users)
                            print("Active OR VIP:")
                            print(active_or_vip)

                            print("\n=============== INTERSECTION ==========")
                            active_and_vip = active_users.intersection(vip_users)
                            print("Active AND VIP:")
                            print(active_and_vip)

                            print("\n============= DIFFERENCE ==========")
                            active_not_vip = active_users.difference(vip_users)
                            print("Active but NOT VIP:")
                            print(active_not_vip)

                            print("\n================ SYMMETRIC DIFFERENCE ==========")
                            active_vip_difference = active_users.symmetric_difference(vip_users)
                            print("Active or VIP, but NOT both:")
                            print(active_vip_difference)

                        elif choice == "3":
                            # TRANSACTION REPORTS
                            print("\n========== TRANSACTION REPORT ==========")

                            transaction_frequency = {}

                            for username in users:
                                history = users[username].get("history", [])

                                user_transaction_count = {}

                                for transaction in history:
                                    transaction_type = transaction.get("type")

                                    user_transaction_count[transaction_type] = (
                                        user_transaction_count.get(transaction_type, 0) + 1
                                    )

                                    transaction_frequency[transaction_type] = (
                                        transaction_frequency.get(transaction_type, 0) + 1
                                    )

                                print("\nUser:", username)

                                for transaction_type in user_transaction_count:
                                    if user_transaction_count[transaction_type] > 1:
                                        print(
                                            "Repeated",
                                            transaction_type,
                                            ":",
                                            user_transaction_count[transaction_type],
                                            "times"
                                        )

                            print("\n========== TRANSACTION FREQUENCY ==========")

                            for transaction_type in transaction_frequency:
                                print(
                                    transaction_type,
                                    ":",
                                    transaction_frequency[transaction_type]
                                )

                        elif choice == "4":
                            # MEMBERSHIP CHECK
                            active_users = set()
                            vip_users = set()
                            failed_login_users = set()
                            transfer_users = set()

                            for username in users:
                                if users[username].get("active") == True:
                                    active_users.add(username)
                                if users[username].get("vip") == True:
                                    vip_users.add(username)
                                if users[username].get("failed_logins", 0) > 0:
                                    failed_login_users.add(username)
                                history = users[username].get("history", [])

                                for transaction in history:
                                    if transaction.get("type") == "transfer":
                                        transfer_users.add(username)
                                        break

                            print("\n========== MEMBERSHIP CHECK ==========")
                            check_username = input("Enter username: ")

                            if check_username not in users:
                                print("User doesn't exist.")
                            else:
                                print("\nChoose a segment:")
                                print("1. Active")
                                print("2. VIP")
                                print("3. Failed login")
                                print("4. transfers")

                                while True:
                                    seg_choice = input("Enter choice: ")

                                    if seg_choice == "1":
                                        print("is user active?", check_username in active_users)
                                        break
                                    elif seg_choice == "2":
                                        print("is user VIP?", check_username in vip_users)
                                        break
                                    elif seg_choice == "3":
                                        print("Has user failed login?", check_username in failed_login_users)
                                        break
                                    elif seg_choice == "4":
                                        print("did user make a transfer?", check_username in transfer_users)
                                        break
                                    else:
                                        print("invalid choice, try again.")

                        elif choice == "5":
                            break

                        else:
                            for item in current_user["history"]:
                                print(item["details"])

                    elif user_input == Branch_ATM_status:
                        print("\n*************** ATM Availability ***************")
                        print("      C0  C1  C2  C3")
                        for r_idx, row in enumerate(atm_matrix):
                            print(f"Row {r_idx}  " + "   ".join(str(val) for val in row))

                    elif user_input == Update_personal_info:
                        print("\n*************** Update Personal Information ***************")
                        print("[0] Change city\n[1] Change phone number\n[2] Change password")
                        sub_opt = input("Select option: ").strip()
                        if sub_opt == "0":
                            current_user["profile"]["city"] = input("Enter new city: ").strip()
                            print("City updated.")
                        elif sub_opt == "1":
                            current_user["profile"]["phone"] = input("Enter new phone: ").strip()
                            print("Phone updated.")
                        elif sub_opt == "2":
                            current_user["profile"]["password"] = input("Enter new password: ").strip()
                            print("Password updated.")

                    elif user_input == Exit:
                        print("Logging out...")
                        break

    elif option == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid Input. Please Try again.")

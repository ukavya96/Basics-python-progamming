correct_password = "password123"
attempts = 0
blocked = False

while attempts < 3:
        if not blocked:
            password = input("Enter the password: ")
            if password == correct_password:
                print("Password correct!")
                break
            else:
                print("Incorrect password. Please try again.")
                attempts += 1
                if attempts == 3:
                    print("Too many incorrect attempts. Your account is now blocked.")
                    blocked = True
        else:
            print("Your account is blocked. Please contact support.")
            break
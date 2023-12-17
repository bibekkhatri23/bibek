# user_list = []

# def register_user():
#     """
#     Register a new user.
#     """
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     user_data = {'username': username, 'password': password, 'logged_in': False}
#     user_list.append(user_data)
#     print(f"User '{username}' registered successfully.")

# def login_user():
#     """
#     Log in a user.
#     """
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     for user in user_list:
#         if user['username'] == username and user['password'] == password:
#             user['logged_in'] = True
#             print(f"User '{username}' logged in successfully.")
#             return
#     print("Invalid username or password.")

# def logout_user():
#     """
#     Log out a user.
#     """
#     username = input("Enter username: ")
#     for user in user_list:
#         if user['username'] == username and user['logged_in']:
#             user['logged_in'] = False
#             print(f"User '{username}' logged out successfully.")
#             return
#     print("User not found or not logged in.")

# register_user()


# login_user()


# logout_user()





def registration():
    global user_list
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_list.append([username, password, name])
    print("Registration Successful")

def login():
    global user_list
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in user_list:
        if user[0] == username and user[1] == password:
            print("Login Successful")
            return user[2]
    print("Invalid Credentials")
    return None

def logout(user):
    if user:
        
          print(f"{user} has been logged out.")

user_list = []
while True:
    print("\nChoose an option:")
    print("1. Registration")
    print("2. Login")
    print("3. Logout")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        registration()
    elif choice == '2':
        name = login()
        if name:
            user_logged_in = name
    elif choice == '3':
        logout(user_logged_in)
        user_logged_in = None
    elif choice == '4':
        print("Exit")
        break
    else:
        print("Invalid Choice")
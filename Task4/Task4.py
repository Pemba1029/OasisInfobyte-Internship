users = {}

def register():
  username = input("Enter username: ")
  password = input("Enter password: ")
  confirm_password = input("Confirm password: ")

  if password != confirm_password:
    print("Passwords don't match. Please try again.")
  elif username in users:
    print("Username already exists. Please choose a different one.")
  else:
    users[username] = password
    print("Registration successful!")

def login():
  username = input("Enter username: ")
  password = input("Enter password: ")

  if username not in users:
    print("Username doesn't exist. Please register first.")
  elif users[username] != password:
    print("Incorrect password. Please try again.")
  else:
    print("Login successful!")
    # Access secured page
    print("Welcome to the secured page!")

def main():
  while True:
    choice = input("1. Register\n2. Login\n3. Quit\nEnter your choice: ")
    if choice == "1":
      register()
    elif choice == "2":
      login()
    elif choice == "3":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
# 1. Name:
#      Nathan Yochim
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program reads usernames and passwords from a JSON file, prompts the user for their credentials, and checks if they are authenticated based on the data.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was handling file errors gracefully and ensuring the username and password match at the same index. Debugging the logic for authentication required careful attention to list indexing and error handling.
# 5. How long did it take for you to complete the assignment?
#      About 1 hour including reading the assignment and writing the code.

import json
import os

FILENAME = os.path.join(os.path.dirname(__file__), "Lab02.json")

def load_credentials(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
    except Exception:
        print(f"Unable to open file {filename}.")
        return None, None
    try:
        obj = json.loads(data)
        usernames = obj.get("username", [])
        passwords = obj.get("password", [])
        return usernames, passwords
    except Exception:
        print("Error reading JSON data.")
        return None, None

def authenticate(usernames, passwords, username, password):
    if usernames is None or passwords is None:
        return False
    if username in usernames:
        idx = usernames.index(username)
        if idx < len(passwords) and passwords[idx] == password:
            return True
    return False

def main():
    usernames, passwords = load_credentials(FILENAME)
    if usernames is None or passwords is None:
        return
    username = input("Username: ")
    password = input("Password: ")
    if authenticate(usernames, passwords, username, password):
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")

if __name__ == "__main__":
    main()

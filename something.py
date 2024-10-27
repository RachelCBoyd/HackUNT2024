def store_credentials():
    credentials = []  # List to store username-password pairs

    while True:
        username = input("Enter your username (or 'exit' to quit): ")
        if username.lower() == 'exit':
            break
        
        password = input("Enter your password: ")
        credentials.append((username, password))  # Store as a tuple
        print("Credentials stored!")

    return credentials

if __name__ == "__main__":
    stored_credentials = store_credentials()
    print("Stored Credentials:")
    for cred in stored_credentials:
        print(f"Username: {cred[0]}, Password: {cred[1]}")

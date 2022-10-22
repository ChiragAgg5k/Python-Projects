import secrets
import string

all_options = string.ascii_lowercase + string.ascii_uppercase + string.digits + "~`!@#$%^&*()_-+={[}]|:;\<,>.?/"
passwords = []

print("""
      
░██████╗███████╗░█████╗░██████╗░███████╗████████╗░██████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝
╚█████╗░█████╗░░██║░░╚═╝██████╔╝█████╗░░░░░██║░░░╚█████╗░
░╚═══██╗██╔══╝░░██║░░██╗██╔══██╗██╔══╝░░░░░██║░░░░╚═══██╗
██████╔╝███████╗╚█████╔╝██║░░██║███████╗░░░██║░░░██████╔╝
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░

      """)

print("""Welcome to SECRETS, a python program used to create passwords meant to be kept, YOU GUESSED IT, A SECRET!
Coincidentally the module used to create the password is also called SECRETS (100% it's a coincidence i swear...)
      
The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as 
passwords, account authentication, security tokens, and related secrets. Random module on the other hand is designed 
for modelling and simulation, not security or cryptography, hence why SECRETS was chosen. 
      
      """)

x = input("Press Enter to continue : ")

while True:

    print('\n' * 100)

    print("""
      
░██████╗███████╗░█████╗░██████╗░███████╗████████╗░██████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝
╚█████╗░█████╗░░██║░░╚═╝██████╔╝█████╗░░░░░██║░░░╚█████╗░
░╚═══██╗██╔══╝░░██║░░██╗██╔══██╗██╔══╝░░░░░██║░░░░╚═══██╗
██████╔╝███████╗╚█████╔╝██║░░██║███████╗░░░██║░░░██████╔╝
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░
      """)

    l = int(input("\nEnter the length of the password you want : "))
    s = int(input("How many? : "))
    for _ in range(s):
        passwords.append(''.join(secrets.choice(all_options) for _ in range(l)))

    print("\nHere are your generated password(s) :\n")
    [print(f"{pos + 1} : {i}") for pos, i in enumerate(passwords)]

    cont = input("\nDo you want to generate more passwords? (y/n) : ")

    if cont == 'n':

        with open("StoredPasswords.txt", 'w') as f:
            for pos, p in enumerate(passwords):
                f.write(f"{pos + 1} : {p}\n")

        print("\nAll the passwords generated are stored in a textfile named StoredPasswords.\n")
        x = input("Press Enter to exist the terminal....")

        break

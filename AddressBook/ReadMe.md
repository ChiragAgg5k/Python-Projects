# AddressBook

We all know how annoying it can be interact with MySQL , or heck any Sequel language in order to create and store Databases. This program eliminates that problem by providing a simple and minimalistic interface made via tkinter that uses Python's Mysql connector library to interact with the Mysql Servers.

## Requirements

- Python 3.6 or higher
- MySQL Server
- MySQL connector module (pip install mysql-connector-python)
- tkinter module (pip install tkinter)
- Stable internet connection

## How to use

Run the program. Enter your MySQL credentials (host is set to localhost by default). Click on the "Enter credentials" button. If incorrect credentials are entered , aka connection failed , it will ask your to simply enter valid credentials. If the connection is successful , a new window will pop up. In the background the program will check if the database already exists. If it doesnt , it will automatically create one. Currently the program only has the functionality to create more records using the "Add Address" button.
More functionaly will be added soon.

### Note

Logging is done via print statements.

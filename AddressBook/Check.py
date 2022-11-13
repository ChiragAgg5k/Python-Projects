import mysql.connector
from mysql.connector.errors import Error, ProgrammingError


def checkDatabase(USER_NAME: str, USER_PASSWORD: str) -> bool:
    """
    Summary : Checks if the database exists in MySQL or not, if not then it creates it
    Parameters : USER_NAME, USER_PASSWORD
    """

    db = mysql.connector.connect(
        host="localhost", user=USER_NAME, password=USER_PASSWORD)
    curr = db.cursor()  # type: ignore

    result = None

    try:
        curr.execute("use AddressBook;")
    except ProgrammingError:
        print("Database does not exist.")
        result = False
    else:
        result = True

    if result:
        print("Database exists")
    else:
        print("Creating database")
        curr.execute("create database AddressBook;")
        curr.execute("use AddressBook;")
        createTables(USER_NAME, USER_PASSWORD)

    curr.close()
    db.close()


def createTables(USER_NAME, USER_PASSWORD):

    db = mysql.connector.connect(
        host="localhost", user=USER_NAME, password=USER_PASSWORD, database="")
    curr = db.cursor()
    curr.execute("USE AddressBook;")

    createTableSyntax = """CREATE TABLE Addresses(
        Sno int(10) NOT NULL PRIMARY KEY,
        FirstName varchar(30) NOT NULL,
        LastName varchar(30),
        City varchar(30) NOT NULL,
        State varchar(30) NOT NULL,
        ZipCode int(10) NOT NULL
    );
    """

    curr.execute(createTableSyntax)


def CheckConnection(USER_NAME, USER_PASSWORD):

    try:
        print("Checking connection")
        db = mysql.connector.connect(
            host="localhost", user=USER_NAME, password=USER_PASSWORD, database="")
        if db.is_connected():
            db_Info = db.get_server_info()
            print("Connected to MySQL Server Version", db_Info)
    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True

import sys  # module imported to use sys.exit()

import mysql.connector  # type: ignore
# module to connect this py script with mysql servers

import random  # module to generate random values

from prettytable import PrettyTable  # type: ignore

# module to display data in tabular format

print("""
░█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ 　 █▀▄▀█ █──█ 　 █──█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
░█░█░█ █▄▄█ █──█ █▄▄█ █─▀█ █▀▀ 　 █─▀─█ █▄▄█ 　 █▄▄█ █▄▄█ ──█── █▄▄▀ █▄▄█ 
░█──░█ ▀──▀ ▀──▀ ▀──▀ ▀▀▀▀ ▀▀▀ 　 ▀───▀ ▄▄▄█ 　 ▄▄▄█ ▀──▀ ──▀── ▀─▀▀ ▀──▀
""")

print("""Welcome to Manage-My-Yatra, A simple console based program
that interacts with MySQL to store , manage and book travel tickets. \n""")

# Asking password to access mysql server
passwd = input("Enter the password of the MySQL server installed on this system:")

# Connecting to mysql server
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=passwd
    )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("create database if not exists TripDatabase")
        mycursor.execute("use TripDatabase")
    except Exception as error:
        print("An error occured.", error)

    # empty list to store bookedtickets
    bookedtickets = []

    sql = "INSERT IGNORE INTO locations (SNo, DestinationName, Location, Cost) VALUES (%s, %s, %s, %s)"
    val = [
        [1, 'Taj Mahal', 'Agra', 40000],
        [2, 'Eiffel Tower', 'Paris', 60000],
        [3, 'Statue of Liberty', 'New York City', 80000],
        [4, 'Machu Picchu', 'Peru', 30000],
        [5, 'Pyramids of Giza', 'Egypt', 45000],
        [6, 'Great Wall of China', 'China', 35000],
        [7, 'Grand Canyon', 'USA', 60000],
        [8, 'Stonehedge', 'England', 55000],
        [9, 'Niagra Falls', 'Canada', 60000],
        [10, 'Sydney Opera House', 'Australia', 65000],
        [11, 'The Louvre', 'Paris', 75000],
        [12, 'Maui', 'Hawaii', 50000],
        [13, 'Red Fort', 'New Delhi', 45000],
        [14, 'Burj Khalifa', 'Dubai', 85000],
        [15, 'Colosseum', 'Rome', 40000],
        [16, 'Banana Reef', 'Maldives', 55000],
        [17, 'Buckingham Palace', 'London', 70000],
        [18, 'Van Gogh Museum', 'Amsterdam', 55000],
        [19, 'Elephanta Caves', 'Mumbai', 60000],
        [20, 'Big Buddha', 'Thailand', 40000]
    ]

    # creating table consisting all the locations
    mycursor.execute(
        "CREATE TABLE if not exists locations (SNo INT(255) primary key, DestinationName VARCHAR(255), "
        "Location VARCHAR(255), Cost INT(255))")
    mycursor.executemany(sql, val)

    # Generating values for travel costs using user's location
    address = input("\nEnter your address:")
    val2 = []
    mycursor.execute("select SNo from locations")
    myresult = mycursor.fetchall()
    len_sno = len(myresult)
    for i in range(len_sno):
        road_cost = 1000 * (random.randrange(10, 50))
        rail_cost = 1000 * (random.randrange(20, 60))
        water_cost = 1000 * (random.randrange(30, 150))
        air_cost = 1000 * (random.randrange(50, 200))
        list_i = [i + 1, road_cost, rail_cost, water_cost, air_cost]
        val2.append(list_i)

    sql2 = "INSERT IGNORE INTO travel_cost (SNo, Roadways, Railways, Waterways, Airways) VALUES (%s, %s, %s, %s, %s)"

    # creating table consisting travel costs
    mycursor.execute(
        "create table if not exists travel_cost (SNo INT(255), Roadways INT(255), Railways INT(255), Waterways INT("
        "255), Airways INT(255))")
    mycursor.executemany(sql2, val2)

# checking for wrong password
except Exception as error:
    print("Oops , looks like you typed the wrong password.")
    print("Terminating program , try again...")
    sys.exit()


# function to display table locations
def showlocations():
    x = PrettyTable()
    x.field_names = ["SNo.", "DestinationName", "Location", "Cost"]
    mycursor.execute("select * from locations")
    myresult = mycursor.fetchall()
    x.add_rows(myresult)
    print(x)


# function to display table costs
def showcosts():
    x = PrettyTable()
    x.field_names = ["SNo.", "Roadways", "Railways", "Waterways", "Airways"]
    mycursor.execute("select * from travel_cost")
    myresult = mycursor.fetchall()
    x.add_rows(myresult)
    print(x)


# function to book tickets
def book():
    ask = input("\nEnter the SNo. of place you want to book:")
    nameask = input("Enter Name to be registered on the ticket:")

    mycursor.execute("select * from locations where SNo=" + ask)
    list1 = mycursor.fetchall()
    list2 = list(list1[0])
    list2.insert(1, nameask)
    list2.insert(4, address)
    list2.append(random.randrange(100000, 999999))
    ask2 = input("\nYou are going to book a ticket to " + list2[2] + ", " + list2[3] + ". Print(y/n) to continue:")
    if ask2 == "y":
        print()
        bookedtickets.append(list2)


# function to display booked tickets
def showtickets():
    print("\nYour Final Yatra Tickets:")

    x = PrettyTable()
    x.field_names = ["Sno.", "Registered Name", "Destination Name", "Location", "Address", "Cost", "Ticket-ID"]
    x.add_rows(bookedtickets)
    print(x)


# function to add new destination
def add_destination():
    x = 0
    while x < 1:
        try:
            l1 = eval(input("Enter details of new destination as a list ['DestinationName', 'Location', Cost]:"))
            l2 = eval(
                input("Enter travel costs of new destination as a list [Roadways , Railways , Waterways , Airways]:"))
            x = 2
        except Exception as error:
            print("Error. Please enter the values in exact given format")

    # to add new destination to locations
    new_sno = len_sno + 1
    l1.insert(0, new_sno)
    mycursor.execute(sql, l1)

    # to add new destination to travel costs
    l2.insert(0, new_sno)
    mycursor.execute(sql2, l2)

    print("\nNew destination successfully added.")


# function to edit package cost of a destination
def editcost():
    sno2 = input("\nEnter the Serial No. of the place whose cost is to be edited:")
    new_cost = input("Enter the new cost:")
    mycursor.execute("""UPDATE locations
                        SET Cost=%s
                        WHERE SNo=%s""", (new_cost, sno2))
    print("\nCost successfully edited")


# function to edit travel cost of a destination
def edittravelcost():
    sno = input("Enter serial number of the destination which is to be edited:")
    mode1 = input("Enter the mode of transport whose value is to be edited(Roadways,Railways,Waterways,Airways):")
    new_cost = input("Enter the new cost:")
    query2 = """UPDATE travel_cost
            SET """ + mode1 + """=""" + new_cost + """\nWHERE SNo=""" + sno
    mycursor.execute(query2)
    print("\nCost successfully edited.")


# function to calculate total cost of ticket packages
def calcpackagecost():
    pkgcost = 0
    for i in range(len(bookedtickets)):
        x = bookedtickets[i][0]
        mycursor.execute("select cost from locations where SNo=" + str(x))
        list1 = mycursor.fetchall()
        num2 = int(list1[0][0])
        pkgcost += num2
    return pkgcost


# function to calculate total cost of travel
def totalcost():
    ques3 = input("\nDo you want the travel service?(y/n):")
    if ques3 == "y":
        mode = input("\nWhich mode of transport do you want to choose?(Roadways/Railways/Waterways/Airways):")
        for i in range(len(bookedtickets)):
            varmode.append(bookedtickets[i][0])

        # assigning the number of placeholders required to a variable
        placeholders = ', '.join(['%s'] * len(varmode))
        query = "select sum(" + mode + ") from travel_cost where SNo in (" + placeholders + ")"
        mycursor.execute(query, tuple(varmode))
        myresult = mycursor.fetchall()
        print("Total cost of trip is:", (int(myresult[0][0]) + package_cost))

    else:
        print("Total cost of trip is:", package_cost)


while True:
    # asking user's input for either management or booking
    var1 = input("\nDo you want to manage or book tickets?(Manage/Book):")
    try:

        # booking code
        if (var1.lower() == "book"):
            print("\nHere's the list of tickets you can book:")
            showlocations()
            print(
                "Cost includes services like breakfast, transport, hotels, flights, sightseeing, monument entry, etc.")

            while True:
                book()

                ask3 = input("Do you want to book more tickets?(y/n):")
                if ask3 == "y":
                    continue
                else:
                    break

            # printing final tickets booked
            showtickets()

        # management code
        elif (var1.lower() == "manage"):
            print("\nHere's the list of tickets you can book:")
            showlocations()
            print("\nHere's the costs of different modes of transport:")
            showcosts()

            print("""\nYou can perform the following functions to manage the list:\n
        1. Add a new destination.
        2. Edit the cost of an existing destination.
        3. Edit the cost of mode of transport of a destination.
                    \n""")

            while True:
                ques1 = int(input("Which one do you want to perform?(1/2/3):"))
                print()

                # adding new destination
                if ques1 == 1:
                    add_destination()

                # editing cost of existing destination
                elif ques1 == 2:
                    editcost()

                # editing cost of mode of transport
                elif ques1 == 3:
                    edittravelcost()

                else:
                    print("Sorry you have entered invalid query")

                ques2 = input("\nDo you want to continue managing?(y/n):")
                if ques2 == "y":
                    continue
                else:
                    break

            print("\n\nThe new database is:\n")
            showlocations()
            showcosts()

        else:
            print("Sorry you have entered invalid query.")

            # showing total cost of travel
        varmode = []
        package_cost = calcpackagecost()
        if var1.lower() == "book":
            totalcost()

    # checking for value error
    except ValueError:
        print("Sorry but the entered query is invalid.", error)

    print()
    ques2 = input("\nContinue booking or managing?(y/n):")
    if ques2 == "y":
        continue
    elif ques2 == "n":
        print("\nThanks for using Manage-My-Yatra.")
        break
    else:
        print("Invalid query, program terminated.")
        break

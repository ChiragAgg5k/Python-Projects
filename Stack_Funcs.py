# defining all the operations we want to perform on our stack

def isempty(stack):
    if stack == []:
        return False
    else:
        return True


def ADD(stack, member):
    stack.append(member)


def DELETE(stack):
    return stack.pop()


def DISPLAY(stack):
    l = len(stack)
    for i in range(0, l):
        print(stack[i])


stack = []

while True:
    print("\nSTACK OPERATIONS....")
    print("1.PUSH-add an element")
    print("2.POP-delete an element")
    print("3.DISPLAY-display the stack")

    ch = int(input("\nEnter your choice(1-3):"))

    if ch == 1:
        eno = int(input("Enter employee's number:"))
        ename = input("Enter employee name:")
        esalary = int(input("Enter employee's salary:"))
        member = [eno, ename, esalary]

        ADD(stack, member)
        print(stack)

        input("Press enter to continue...")

    elif ch == 2:
        item = DELETE(stack)
        print("Pop id :", item)
        input("Press enter to continue...")

    elif ch == 3:
        DISPLAY(stack)

    elif ch == 4:
        break

    else:
        print("Invalid choice!")
        input("Press enter to continue...")

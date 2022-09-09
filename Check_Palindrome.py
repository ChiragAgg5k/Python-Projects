# writing a user-defined function that checks if a number is palindrome or not WITHOUT converting it into a string.

def check_palindrom(x):
    div = 1

    while (x // 10) >= div:  # creating the maximum multiple of 10 smaller than the given number
        div *= 10

    while x:
        if (x % 10) != (x // div): return False  # x%10 gives the left-most val , x//div gives the right most val

        x = (x % div) // 10
        div = div / 100

    return True


num_1 = int(input('Enter the number to be checked for palindrome:'))
print(check_palindrom(num_1))

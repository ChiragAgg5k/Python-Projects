def snake_to_camel(snake_str):

    sys_output = ''
    # splitting the string with underscore as the seperator
    for word in snake_str.split('_'):
        sys_output += word.capitalize()
    return sys_output


def camel_to_snake(camel_str):

    # starting a list with first letter of camel case in smaller case
    str_list = [camel_str[0].lower()]
    for letter in camel_str[1:]:
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            str_list.append('_')
            str_list.append(letter.lower())
        else:
            str_list.append(letter)

    final_str = ''.join(str_list)  # joining the created list into one string
    return final_str


while True:
    try:
        choice = int(input(
            '\nEnter your choice \n 1. Snake to Camel \n 2. Camel to Snake \n Or press any other key to terminate :'))

        if choice == 1:
            user_input = input(
                "Enter the string to be converted to Camel casing:")
            print(
                f"\nThe string in camel case is: {snake_to_camel(user_input)}")
        elif choice == 2:
            user_input = input(
                "Enter the string to be converted to Snake casing:")
            print(
                f"\nThe string in snake case is: {camel_to_snake(user_input)}")
        else:
            print("\nTerminating the program....")
            break
    except Exception as error:
        print("\nTerminating program...")
        break

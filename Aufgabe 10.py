def main():

    user_input()

    return True


def user_input():

    i = 0
    list_of_inputs = []

    while i <= 10:
        user_input = input('Please fill the list with a name: ')
        i += 1

        if user_input not in list_of_inputs:
            list_of_inputs.append(user_input)
            list_of_inputs.sort()
            print(f'This is your current list: {list_of_inputs}')

        else:
            print(f'Error: {user_input} is already in the list.')
            i -= 1
    
        
    
    return print(f'This is your final list: {list_of_inputs}')



if __name__ == '__main__':
    result = main()
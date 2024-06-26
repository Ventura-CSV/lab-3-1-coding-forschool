def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))

    range = 0
    if number <= 50:
        range = 1
    elif number > 50 and number <= 100:
        range = 2
    elif number >= 100:
        range = 3

    print(f'Range is {range}')
    ########################################
    # Do not delete the return statement
    ########################################
    return range


if __name__ == '__main__':
    main()

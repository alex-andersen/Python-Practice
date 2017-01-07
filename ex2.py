#!/usr/local/bin/python3.6
def main():

    inputInt = int(raw_input("Input a number: "))

    if inputInt % 2 == 0 & inputInt % 4 == 0:
        print("{} is even and divisible by 4.".format(inputInt))
    elif inputInt % 2 == 0:
        print("{} is even but NOT divisible by 4.".format(inputInt))
    else:
        print("{} is odd.".format(inputInt))

if __name__ == '__main__':
    main()

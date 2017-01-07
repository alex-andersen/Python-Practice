#!/usr/local/bin/python3.6
def main():

    name = str(raw_input("What is your name? "))
    age = int(raw_input("How old are you? "))
    nPrint = int(raw_input("How many prints? "))

    for i in range(nPrint):

        print("Name: {} Age: {}".format(name, age))

    #print("User info:\nName: {}\nAge: {}" .format(name, age))

if __name__ == '__main__':
    main()

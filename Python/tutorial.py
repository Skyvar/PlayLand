#!/usr/bin/env python

import datetime
import requests
import json

date = datetime.datetime.now()
REPEAT = "Would you like to do anything else?"

print("What is your name")
name = input()

print("\nHello " + name + ", welcome to PyMenu")
print("Please make your selection from the menu below")

def menu():
    print("""
    1. Print today's date
    2. Print friendly greeting
    3. Read todo list (/home/taft/playland/python/todo.list)
    4. Show weather using zip code
    9. Exit PyMenu
    """)

def temperature(zipcode):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(zipcode) + "&APPID=7d309f4fac16c6fe0779b433aa566dbf"
    weather = requests.get(url).json()
    degree_symbol='°'
    ktemp = weather['main']['temp']
    ftemp = (ktemp * 9/5) - 459.67
    print("The current temp for zip " + str(zipcode) + " is:\n")
    print(str(int(ftemp)) + str(degree_symbol) + "F")


while True:
    menu()
    choice = input()
    if choice == "1":
        print("\nToday is : " + date.strftime("%A"), date.strftime("%B"), date.strftime("%d"), date.strftime("%Y"))
        print("\n")
        print(REPEAT)
    elif choice == "2":
        print("\nHello " + name + ", it's a pleasure to meet you\n")
        print(REPEAT)
    elif choice == "3":
        while True:
            todo = open('todo.list', 'r+')
            print("\n" + todo.read() + "\n")
            print("Would you like to add to your todo list? (y/n)")
            todoChoice = input()
            if todoChoice == "y" or todoChoice == "Y":
                print("What else would you like to add?")
                newItem = str(input())
                todo.write(newItem)
                todo.write("\n")
                todo.close()
            elif todoChoice == "n" or todoChoice == "N":
                break
                print(REPEAT)
            else:
                print("Not a valid option")
            print(REPEAT)
    elif choice == "4":
        print("Please enter your zip code:")
        zipcode = input()
        temperature(zipcode)
    elif choice == "9":
        print("Thanks for using PyMenu " + name + ", have a great day!")
        break
    else:
        print("That is not a valid option")
        print("Please make a valid selection")


import random
import requests

class bcolors:
    HEADER = '\033[95m'
    CWHITE  = '\33[37m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

APIURL = "https://api.kanye.rest/"

print(bcolors.OKGREEN)
print("--------------------")
print("Welcome to Kanye Quote Generator")
# print()


while (True):
    print(bcolors.OKCYAN)
    print("enter [g] to generate")
    print("enter [q] to quit")
    userInput = input()
    print()
    if (userInput == "q"):

        break
    elif (userInput != "g"):
        print(); 
        print("invalid input")
        continue
    response = requests.get(APIURL)
    response = response.json()

    print(bcolors.WARNING + "\"" + response['quote'] + "\"")
print(bcolors.OKGREEN)
print("Goodbyte")
print("--------------------")
print(bcolors.CWHITE)


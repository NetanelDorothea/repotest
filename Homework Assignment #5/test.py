from typing import Dict
import csv

policies = open('policies.csv', 'r')
Dict_policies = csv.DictReader(policies)


# checks if query available
def get_query(keyword):
    for row in Dict_policies:
        # Access the value from the keyword
        if keyword in row['keyword']: print(f"{row['keyword']}: {row['response']}")


# handling the request from user
def handle_request():
    while True:
        request = input("Which would you like help with? 'vacation', 'contact', 'location', or 'exit': ")

        if request == "vacation":
            get_query(request)
        elif request == "contact":
            get_query(request)
        elif request == "location":
            get_query(request)
        elif request == "insurance":
            get_query(request)
        elif request == "exit":
            print("Thank you for using this chatbot!")
            break
        else:
            print(
                "I'm sorry, this chatbot is currently under development and can provide information on vacation, contact, and location.")


# Initiate function
def chatbot():
    handle_request()


chatbot()
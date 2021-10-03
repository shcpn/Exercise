import csv
import pandas as pd
import os.path

header = ['firefox_webdriver', 'link', 'username_element_ID', 'username', 'password_element_ID', 'password', 'login_button_ID']
monitoring = []
start = input("do you want to start monitor(Yes/No): ")
csv_PATH = str(input("please enter your csv file path: "))
if os.path.isfile(csv_PATH):
    df = pd.read_csv(csv_PATH)
    print (df)
else:
    print("the csv_PATH is not create")
    with open(csv_PATH, "a", encoding='UTF8', newline='') as new:
        writer = csv.writer(new)
        writer.writerow(header)
        new.close()
    while start == "yes":
        new = input("do you want to add new URL(Yes/No): ")
        while new == "yes":
            print ("please enter your link: ")
            link = str(input())
            print("please enter the username_element_ID: ")
            username_element_ID = str(input())
            print("please enter your username: ")
            username = str(input())
            print("please enter the password_element_ID: ")
            password_element_ID = str(input())
            print("please enter your password: ")
            password = str(input())
            print("please enter the login_button_ID: ")
            login_button_ID = str(input())
            monitoring = ["firefox_webdriver", link, username_element_ID, username, password_element_ID, password, login_button_ID]
            print (monitoring)
            with open(csv_PATH, "a", encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(monitoring)
                f.close()
                cont = input("do you want to continue or enugh(continue/enugh): ")
                if cont == "cont":
                    continue
                else:
                    break
        if new == "no":
            df = pd.read_csv(csv_PATH)
            print (df)
            break







#    if input() == "n":
#        URL = str(input())
#        link.append(URL)
#    else:
#        print ("your URLs are: ", link )

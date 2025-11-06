# exc1
import json


def count_word(url_file):
    with open(url_file, "r") as file:
        contact = file.read()
        contact = contact.split()
        return len(contact)


# exc2

import csv


def writefile(list_of_lists):
    with open('people.csv', "w", newline=" ") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['First Name', 'Last Name', 'Age', 'City'])
        writer.writerows(list_of_lists)


# exc3
def write_json(dic):
    with open("data.json", "w") as file_json:
        json.dump(dic, file_json)
    with open("data.json", "r") as file_json1:
        contact = json.load(file_json1)
        print(contact)

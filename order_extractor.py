import re

# pattern dictionary
patterns = {"1": r"#\d+", # order number
            "2": r"1Z[a-zA-Z0-9]{16}", # tracking number
            "3": r"[a-zA-Z0-9-._]+@[a-zA-Z-]+\.[a-zA-Z]{2,}", # email
            "4": r"\(?\d{3}\)?[-]?\s?\d{3}-\d{4}", # phone number
            "5": r"\$\d+\.\d{2}" # purchase amount
            }


def main():
    choice = user_menu()
    file_content = read_data()
    results = pattern_compare(file_content, choice) # file_content & choice are arguments being passed in

    for result in results:
        print(result)


def user_menu():
    print("Welcome to Order Extractor\n"
          "Enter one of the following options\n"
          "1: Extract Order Number\n"
          "2: Extract Tracking Number\n"
          "3: Extract Email\n"
          "4: Extract Phone Number\n"
          "5: Extract Purchase Amount\n")

    return input("Enter one of the following options (1 - 5): ")

def read_data():
    with open("order_det.txt", "r") as file:
        content = file.read()

    return content

def pattern_compare(content, user_choice): # parameters being used to accept the arguments that are passed
    if user_choice in patterns:
        results = re.findall(patterns[user_choice], content)

        return results # return results if user_choice existed - re.findall() returns a list of values of found
    return [] # return an emtpy list


main()


#with open ("order_det.txt", "r") as f:
#    data = re.findall(paren_test, f.read())
#    for phone in data:
#        print(phone)
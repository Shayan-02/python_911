user1 = input("entekhab e khod ra vared konid1: ")
user2 = input("entekhab e khod ra vared konid2: ")

if user1 == "sang" or user1 == "gheichi" or user1 == "kaghaz" and user2 == "sang" or user2 == "gheichi" or user2 == "kaghaz":
    if user1 == "sang" and user2 == "kaghaz":
        print("user2 barandeh shod.")
    elif user1 == "kaghaz":
        if user2 == "sang":
            print("user1 barandeh shod.")
        elif user2 == "gheichi":
            print("user2 barandeh shod.")
import csv

inventory = []

with open("inventory.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  #skips the header row

    for row in reader:
        item = row[0]
        quantity = int(row[1])
        price = float(row[2])
        inventory.append([item, quantity, price])  #this will store each item in a list

while True:
    print("\n1. view inventory")
    print("2. sell item")
    print("3. exit")

    choice = input("choose: ")

    if choice == "1":
        for item in inventory:
            print(item[0], "| qty:", item[1], "| price:", item[2])

    elif choice == "2":
        name = input("enter item name: ")
        found = False

        for item in inventory:
            if item[0] == name:
                found = True
                amount = int(input("how many to sell? "))

                if amount > item[1]:
                    print("not enough in stock.")  #this prevents negative inventory
                elif amount <= 0:
                    print("invalid amount.")
                else:
                    item[1] -= amount  #subtract sold quantity
                    print("sold.")

        if not found:
            print("item does not exist.")  #this validates item exists

    elif choice == "3":
        break

    else:
        print("invalid choice.")

with open("inventory.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Quantity", "Price"])

    for item in inventory:
        writer.writerow(item)

print("inventory saved.")
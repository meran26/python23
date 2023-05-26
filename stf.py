import csv

menu_stocks = {}
stocks = {}
id = 0

reset_history = []
reset_sales = []

sales = open("sales.csv", "w")
sales_reset = csv.writer(sales)
sales_reset.writerows(reset_sales)

history = open("history.csv", "w")
history_reset = csv.writer(history)
history_reset.writerows(reset_history)

def init():
    global menu_stocks, stocks, id, header
    f = open("stf.csv", "r")
    header = f.readline()
    line = f.readline()

    while line:
        id = id + 1
        token = line
        tokens = token.split(',')
        menu_stocks[id] = tokens[0]
        stocks[tokens[0]] = [int(tokens[1]), int(tokens[2])]
        line = f.readline()
    
    f.close()

def add():
    global menu_stocks, stocks, id, amount, header
    id = id + 1
    name = input("Enter Name: ")
    amount = int(input("Enter Amount: "))
    value = int(input("Enter Value: "))
    history = open("history.csv", "a")
    history.write(name + "\n" + str(amount) + "\n" + str(value) + "\n")
    history.close()
    menu_stocks[id] = name
    stocks[name] = [amount, value]
    f = open("stf.csv", "w")
    f.write(header)
    for key, value in stocks.items():
        f.write(key + "," + str(value[0]) + "," + str(value[1]) + "\n")
    f.close()

def delete():
    global menu_stocks, stocks, header
    d_choice = int(input("Enter ID: "))
    f = open("stf.csv", "w")
    for m_key in list(menu_stocks):
        if d_choice == m_key:
            del menu_stocks[m_key]
    for s_key in list(stocks):
        if s_key not in menu_stocks.values():
            del stocks[s_key]
    f.write(header)
    for key, value in stocks.items():
        f.write(key + "," + str(value[0]) + "," + str(value[1]) + "\n")
    f.close()

def sell(key, amount):
    global stocks
    print(f"Sell {key}, amount: {stocks[key][0]}")
    if stocks[key][0] >= amount:
        stocks[key][0] = stocks[key][0] - amount
        print(f"sell {key}: {stocks[key][1] * amount}")
    else:
        print(f"Cannot sell {key}")
    
def print_store():
    print("==========STF============")
    for key, item in stocks.items():
        print(f"{key}:{item}")

def print_menu():
    for key, item in menu_stocks.items():
        print(f"{key}. Buy {item}")
    print("97. Insert Item")
    print("98. Remove Item")
    print("99. Bye")
    print("0. Print Stock")
    print("=========================")

def save():
    global menu_stocks, stocks, id
    menu_stocks_list = list(menu_stocks.items())
    for key, value in stocks.items():
        menu_stocks_list.append(value)
    f = open("stf.csv", "w", newline='')
    wt = csv.writer(f, delimiter=',')
    wt.writerows(menu_stocks_list)
    print(menu_stocks_list)

init()

while 1:
    print_store()
    print_menu()

    choice = int(input("Enter Choice: "))
    history = open("history.csv", "a")
    history.write(str(choice) + "\n")
    history.close()

    if choice == 99:
        break
    elif choice == 97:
        add()
    elif choice == 98:
        delete()
    elif choice == 0:
        print_store()
    else:
        amount = int(input("Enter amount: "))
        sell(menu_stocks[choice], amount)
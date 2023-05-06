menu_stocks = {}
stocks = {}
id = 0

def init():
    global menu_stocks, stocks, id
    f = open("stf.csv", "r")
    f.readline()
    line = f.readline()

    while line:
        token = line
        tokens = token.split(',')
        menu_stocks[int(tokens[0])] = tokens[1]
        stocks[tokens[1]] = [int(tokens[2]), int(tokens[3])]
        id = int(token[0])
        line = f.readline()
    
    f.close()

def add():
    global menu_stocks, stocks, id
    id = id + 1
    name = input("name: ")
    amount = int(input("amount: "))
    value = int(input("value: "))
    menu_stocks[id] = name
    stocks[name] = [amount, value]
    
def delete():
    global menu_stocks, stocks
    list = []
    for menu_key, menu_value in menu_stocks.items():
        list.extend([menu_key, menu_value])
        for s_key, s_value in stocks.items():
            if s_key == menu_value:
                list.append(s_value)
    print(list)
    d_choice = input("Delete Choice: ")
    

init()

while 1:
    choice = int(input("Enter Choice: "))
    if choice == 99:
        break
    elif choice == 97:
        add()
    elif choice == 98:
        delete()

print(menu_stocks)
print(stocks)
'''save()
def save():
    f = open("stf.csv", "w", encoding="utf8")
    f.write(",".join)'''
import csv # csv 모듈을 불러옴

# stock = {"apple":[20, 1000], "mango":[3, 30000]}
# menu_stocks = {1: "apple", 2: "mango"}

menu_stocks = {} # 물품의 품목을 이 딕셔너리에 담기 위해 만든 딕셔너리
stock = {} # 물품의 이름과 수량과 가격을 넣어줄 딕셔너리

reset_history = []
reset_sales = []

sales = open("sales.csv", "w")
sales_reset = csv.writer(sales)
sales_reset.writerows(reset_sales)

history = open("history.csv", "w")
reset = csv.writer(history)
reset.writerows(reset_history)

menu_price = 0
total_price = 0

def csv_read(): # csv를 불러올 함수를 만들어줌
    global token, num, tokens, f # 지역변수를 전역변수로 만들어줌
    f = open("stf.csv", "r") # stf.csv 를 읽기전용으로 불러옴
    f.readline() # 파일 첫번째 헤더를 불러옴

    num = 1 # 품목의 id를 설정할 num이라는 변수를 선언

    while True: # 무한 루프 돌려줌
        token = f.readline() # 라인마다 읽어서 끝까지 읽어줌
        if not token: # 마지막 행까지 갔으면
            break # 루프 끝내줌
        num += 1 # 읽을 때 마다 num에 1을 추가해서 1, 2, 3 순으로 갈 수 있게 해줌
        tokens = token.split(',') # token이 현재 1, apple, 20, 1000 으로 되어있기 때문에 ,를 기준으로 split으로 구분해줌
        menu_stocks[int(tokens[0])] = tokens[1] # tokens[0]은 id를 의미 하고 menu_stocks는 id를 키로 가지고 그 밸류로 tokens[1] 즉 name을 가지게 된다.
        stock[tokens[1]] = [int(tokens[2]), int(tokens[3])] # stock[tokens[1]] 은 tokens[1]이 name이 되고 그 name을 key로 가지는 stock[tokens[1]]의 밸류를 리스트 형식으로 [amount, price] 로 가지게 된다.        

def sell(key, count): 
    global stock, menu_stocks, amount, menu_price, total_price
    print(f"Sell {key}, amount:{stock[key][0]}")
    if stock[key][0] >= count:
        stock[key][0] -= count
        menu_price += stock[key][1]
        total_price += menu_price * count
        menu_stocks[key] += count
        print(f"sell {key}: {menu_price * count}")
        history = open("history.csv", "a", encoding="UTF-8")
        history.write("\n" + "구매한 품목 : " + menu_stocks[choice])
        history.write("\n" + "구매한 품목의 갯수 : " + str(amount))
    else:
        print(f"Cannot sell {key}")

def print_store():
    print("======STF======")
    for key, item in stock.items():
        print(f"{key}:{item}")

def print_menu():
    for key, item in menu_stocks.items(): 
        print(f"{key}. Buy {item}") 
    print("97. add menu") 
    print("98. delete menu")
    print("99. Bye")
    print("====================")

def add_menu():
    global stock, menu_stocks, num, name, amount, price
    name = input("Enter stock name : ")
    amount = int(input("Enter stock's amount : "))
    if amount > 90:
        print("수량은 최대 90개를 넘을 수 없습니다.")
        amount = int(input("Enter stock's amount : "))
    price = int(input("Enter stock's price : "))

    menu_stocks[num] = name 
    stock[name] = [int(amount), int(price)]
    f = open("stf.csv", "a")
    f.write("\n" + str(num) + "," + name + "," + str(amount) + "," + str(price))

def delete_menu():
    global stock, menu_stocks, f
    choice = int(input("(delete) Enter id : "))

    f = open("stf.csv", "r")
    rows = list(csv.reader(f))

    del rows[choice]
    del stock[menu_stocks[choice]]
    del menu_stocks[choice]

    with open("stf.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def show_menu():
    global stock, menu_stocks
    print("======STF======")
    for key, item in menu_stocks.items():
        print(f"{key}. {item}")

loop = 5
csv_read()

for _ in range(loop):
    print_store()
    print_menu()

    choice = int(input("Enter Choice: "))

    if choice < 97 and choice > 0:
        amount = int(input("Enter amount: "))
        sell(menu_stocks[choice], amount)
    elif choice == 99:
        break
    elif choice == 97:
        add_menu()
        loop += 1
    elif choice == 98:
        show_menu()
        delete_menu()
        loop += 1
    elif choice == 0:
        print_store()
        back = int(input("위는 현재 재고 상황입니다. 돌아가려면 다시 0을 입력해주세요 : "))
        if back == 0:
            loop += 1
            continue

history.close()
menu={
    1:{
        "name":'espresso',
        "price":1.99
    },
    2:{
        "name":"coffee",
        "price":2.50
    },
    3:{
        "name":"cake",
        "price":2.79
    },
    4:{
        "name":"soup",
        "price":4.50
    } ,
    5: {"name": 'sandwich',
        "price": 4.99}
};

def display_menu():
    print("-------Menu-------")
    for key in menu:
        print(f"{key}. {menu[key]['name'] : <9} | {menu[key]['price'] : >5}")

def take_order():
    display_menu()
    order=[]
    count=1
    for i in range(5):
        item=input("Select menu item number: "+str(count)+" (from 1 to 5):\n enter any character from a to z for exiting order list: ")
        count+=1
        order.append(menu[int(item)])
        if(type(int(item))!=type(2)):
            break;
    return order

def print_order(order):
    print("You have ordered "+str(len(order))+' items.')
    items=[]
    items=[item["name"] for item in order]
    print(items)
    return order;

def calculate_subtotal(order):
    subtotal=0
    for i in range(len(order)):
        subtotal+=order[i]["price"]
    return subtotal; 

def calculate_tax(subtotal):
    tax=round(subtotal*15/100,2);
    return tax;

def summarize_order(order):
    subtotal=calculate_subtotal(order)
    tax=calculate_tax(subtotal)
    total=round(subtotal+tax,2)
    names=[]
    for item in order:
        names=[item["name"]]
    return names,total;

def main():
    order=take_order()
    print(order)
    print_order(order)


    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)

if __name__=="__main__":
    main()
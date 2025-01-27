#define menu medicine of medical
menu={"paracetamol":20,"cefexime":30,"azitral":60,"syrup":100}

#greet
print("welcome to my medical shoap")
print("paracetamol: rs20\n cefexime: rs30\n aziral: rs60\n syrup: rs100\n")

order__total=0

item_1=input("enter item name you want to order")
if item_1 in menu:
    order__total +=menu[item_1]
    print("your order{item_1} has been added")

else:
    print("your order{item_1} not available")

another_item=input("do you want  order another_item? (yes/no) ")
if another_item== "yes":
    item_2=input("enter the second order")
    if item_2 in menu:
        order__total +=menu[item_2]
        print("your second order{item_2} has been added")
    else:
         print("your order{item_2} not available")
print(f"total amount of item pay is {order__total}")
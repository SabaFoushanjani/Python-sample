product={}
def add():
    name= input ("enter the name of product: ") .lower ()
    price= float(input ("enter the price of product: "))
    if name not in product.keys():
        product[name]= price
        print (f"{name} added")
    else:
        print ("already exist! ")
def display ():
    if len (product) == 0:
        print ("empty! ")
        return
    for name, price in product.items():
        print(f"{name} ----->{price}")
def remove (name):
    if name in product.keys ():
        product.pop (name)
        print (f" {name} removed")
    else:
        print ("not found! ")
def edit (name):
    if name in product.keys ():
        new_price= input ("enter new price: ")
        product [name]= new_price or product [name]
    else:
        print ("not found! ")
def search (name):
    flag= True
    for i in product:
        if name in i:
            print (f"{i} ------> {product [i]}")
            flag= False
            if flag:
                print ("not found! ")
def details ():
    d= input ("choose an item: number of products, average, min, max: ") . lower ()
    if d== "number of products":
        length= len (product)
        print (length)
    elif d== "average":
        prices= list (product.values ())
        average= sum (prices) // len (prices)
        print (average)
    elif d== "min":
        prices= list (product. values ())
        minimum= min (prices)
        print (minimum)
    elif d== "max":
        prices= list (product. values ())
        maximum= max (prices)
        print (maximum)
    else:
        print ("command not found! ")
while True:
    answer= input ("add, remove, edit, search, display, details, exit: ") .lower ()
    if answer== "add":
        add()
    elif answer== "remove":
        name= input ("name for remove: ")
        remove (name)
    elif answer== "edit":
        name= input ("name for edit: ")
        edit (name)
    elif answer== "search":
        name= input ("name for search: ")
        search (name)
    elif answer== "display":
        display ()
    elif answer== "details":
        details ()
    elif answer== "exit":
        break
    else:
        print ("command not found!")
product=[]
price=[]
for i in range (100):
    answer=input ("choose an action:add, remove, edit, search, display: ").lower ()
    if answer=="add":
        p= input("what is your product? ") .lower ()
        if p not in product:
            pr= float (input ("how much does it cost? "))
            product.append (p)
            price.append (pr)
            print ("*"*7+ "added" +"*"*7)
        else:
            print (f"{p} already exist! ")
    elif answer== "remove":
        p_name= input ("which product do you want to remove? ").lower ()
        if  p_name in product:
            i= product. index(p_name)
            n1= product. pop (i)
            p1= price. pop (i)
            print (f"{n1} with the price of {p1} has been removed successfully!")
        else:
            print ("not found!")
    elif answer=="edit":
        e_name= input ("which product do you want to edit? ").lower ()
        if e_name in product:
            new_name= input (" what is the name of new product? ").lower ()
            i= product. index (e_name)
            if new_name not in product:
                product[i]= new_name or product [i]
            else:
                print ("already exist! ")
            new_price= input (" what is the new price? ")
            price[i]=float (new_price or price [i])
            print(f"{e_name} edited to {new_name} with this price {new_price}")
        else:
            print ("not found! ")
    elif answer=="search":
        name= input (" which product? ").lower ()
        if name in product:
            i= product. index (name)
            print (f"{name} with the price of {price [i]}")
        else:
            print ("not found! ")
    elif answer== "display":
        if len (product)==0:
            print(" there are no items! ")
            continue
        for i, name in enumerate(product):
            print (f"{i+1}: {name} with the price of {price[i]}")
    else:
        print ("command not found! ")


    






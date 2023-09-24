##p_info = name, color, price, category
all_products = {}
def valid_price(price):
    if price > 0:
        return True
    return False
def add ():
    p_id = input ("product information: ")
    if p_id not in all_products.keys():
        name = input ("the name of the product? ")
        color = input ("what color is it? ")
        price = float(input ("How much does it cost? "))
        if valid_price == False:
            price = 100
        category = input ("which category? ")
        product = {
            "name" : name,
            "color": color,
            "price": price,
            "category": category
        }
        all_products[p_id]= product
        print ("added")
def search (name):
        flag = False
        for i in all_products:
             product = all_products[i]
             if name in product ["name"]:
                  flag = True
                  for i in product:
                       print (f"{i} -----> {product [i]}")
        if flag == False:
             print ("not found!")
def edit (pr_id):
     if pr_id in all_products.keys ():
          name_ = input ("new name: ")
          color_ = input ("new color: ")
          price_ = input ("new price: ")
          category_ = input ("new category: ")
          all_products[pr_id]["name"] = name_ or all_products[pr_id]["name"]
          all_products[pr_id]["color"] = color_ or all_products[pr_id]["color"]
          all_products[pr_id]["price"] = float (price_ or all_products[pr_id]["price"])
          all_products[pr_id]["category"] = category_ or all_products[pr_id]["category"]
     else:
          print ("not found! ")
def remove (p_id):
    if p_id in all_products.keys ():
          all_products. pop (p_id)
          print ("removed")
    else:
         print ("not found! ")
def display ():
     for i in all_products:
          print (i, all_products[i])
          product = all_products[i]
          for j in product:
               print (f"{j} ----> {product[j]}")
def details ():
     count = len (all_products)
     print (f"the number of products are {count}.")
     prices = []
     for i in all_products:
          product = all_products[i]
          price = product["price"]
          prices. append(price)
     avg = sum(prices)/ len (prices)
     print (f"the average of prices are {avg}.")
     max_pr = max (prices)
     min_pr = min (prices)
     print (f"the maximum of price is {max_pr} and the minimum is {min_pr}")
while True:
    command = input ("add, edit, remove, display, search, details: ")
    if command == "add":
        add ()
    elif command == "search":
        name = input (" the name of the product? ")
        search (name)
    elif command == "edit":
         pr_id = input ("the id of the product? ")
         edit (pr_id)
    elif command == "details":
         details ()
    elif command == "remove":
         p_id = input ("the id of the product: ")
         remove (p_id)
    elif command == "display":
         display ()
    elif command == "":
         break
    else:
         print ("command not found! ")

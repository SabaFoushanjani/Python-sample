student_number=[]
score=[]
def add (n):
    if n not in student_number:
        s= (float (input ("what is your score? ")))
        score.append(s)
        student_number.append(n)
        print("-"*5 +"added" +"-"*5)
    else:
        print (f"{student_number}already exist")
def remove (number):
    if number in student_number:
        i= student_number.index (number)
        s1= score.pop (i)
        n1=student_number.pop (i)
        print (f"{n1} with  the score of {s1} has been removed successfully")
    else:
        print ("not found!")
def edit (number):
    if number in student_number:
        new= (int( input( " new student number: ")))
        i= student_number. index (number)
        student_number[i]= new
        print (f'{number} is edited to {new}')
    else:
        print ("already exist!")
def search (student_num):
    if student_num in student_number:
        i= student_number.index (student_num)
        print (f"{student_num} with the score of {score [i]}")
    else:
        print ("not found!")
def details (item):
    if item== "sum":
        s= sum (score)
        print(s)
    elif item== "average":
        avg= sum (score)/ len (score)
        print (avg)
    elif item== "min":
        m= min (score)
        print (m)
    elif item== "max":
        ma= max (score)
        print (ma)
    elif item=="number":
        l= len (score)
        print (l)
    else:
        print ("command not found!")
for i in range (100):
  answer= input("select an option; add, remove, edit, search, display,details. ").lower ()
  if answer=="add":
    n=(int (input ("what is your student number? ")))
    add (n)
  elif answer== "remove":
    number= (int(input ("student number for remove: ")))
    remove(n)
  elif answer== "edit":
      number=(int(input( "which student number do you want to edit? ")))
      edit (number)
  elif answer== "search":
        student_num= int(input ("what is your student number? "))
        search (student_num)
  elif answer== "display": 
    if len (student_number)== 0:
        print("there are no items")
    for i, student_num in enumerate(student_number):
        print (f"{i+1} = {student_num} with the score of {score[i]}")
  elif answer== "details":
    item= input ("choose an item: sum, average, min, max, number. ")
    details (item)
else:
  print ("command not found!")


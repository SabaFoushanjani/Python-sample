#students......>(id, first name, last name, score)
students = []
def find_id(id_s):
	for i, s in enumerate(students):
		if s[0] == id_s:
			return i
	return -1
def add():
     id_s = input ("enter the student's id: ")
     find = find_id(id_s)
     if find == -1:
          first_name = input ("what is the name of the student?")
          last_name = input ("what is the last name of the student? ")
          score = float (input ("what is the score of the student? "))
          student = (id_s, first_name, last_name, score)
          students. append (student)
          print ("added! ")
     else:
          print ("already exist! ")
def display():
     if len (students) == 0:
          print ("empty list! ")
          return
     for i, n, l, s in students:
          print (f" {i}) {n} {l} with the score of {s}")
def remove(id_s):
     find = find_id(id_s)
     if find != -1:
          students. pop (find)
          print ("removed! ")
     else:
          print (" not found! ")
def edit(id_s):
     find = find_id(id_s)
     if find != -1:
        name = input ("enter the new name: ")
        l_name = input ("enter the new last name: ")
        score = input ("enter the new score: ")
        student  = students [find]
        student = list (student)
        student[1]= name or student [1]
        student[2]= l_name or student[2]
        student[3]= float (score or student[3])
        student = tuple (student)
        students [find] = student
        print ("edited")
     else:
          print ("not found! ")
def search (name):
     flag =True
     for s in students:
          if name in s[1]:
            flag= False
            print (f"{s[0]}), the name and last name of student is {s[1]} {s[2]} with the score of {s[3]}")
     if flag:
          print("Not Found!")
def find_score(score):
     for s in students:
          if s[3] == score:
               print (f"{s[0]}), {s[1]} {s[2]} with the score of {s[3]}")
               return
def details():
     length = len (students)
     scores=[]
     for s in students:
          scores. append (s[3])
          max_s = max (scores)
          min_s = min (scores)
          avg = sum (scores) / length
          print ("number of students:", length)
          print ("max: ")
          find_score (max_s)
          print ("min: ")
          find_score(min_s)
          print (" average:", avg)
while True:
    cmd = input ("add, display, remove, search, details, edit, exit: ")
    if cmd == "add":
        add()
    elif cmd == "remove":
        id_s = (" id to remove: ")
        remove (id_s)
    elif cmd == "display":
        display ()
    elif cmd == "search":
        name = input ("name to search: ")
        search (name)
    elif cmd == "details":
        details ()
    elif cmd == "edit":
        id_s= input (" id to edit: ")
        edit (id_s)
    elif cmd == "exit":
        break
    else:
        print ("command not found! ")
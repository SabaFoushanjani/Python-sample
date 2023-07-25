##question1
num_lists= [12, 2, 5, 8, 16, 20]
l= len (num_lists)
print (l)
total= sum (num_lists)
print (total)
average= total / l 
print (average)
minimum= min (num_lists)
print (minimum)
maximum= max (num_lists)
print (maximum)
sort= sorted(num_lists)
middle_index= l //2
if l %2==0:
    median= (sort [ middle_index-1] + sort[middle_index]) / 2
else:
    median= sort [middle_index]
print (median)
#question2
my_list= []
for i in range (3):
    my_list. append(input ("enter three numbers: "))
print (my_list)
my_list [ int (input ("which index?" ))] = (input("new number: "))
print (my_list)
my_list. pop (int (input( "which index? ")))
print (my_list)








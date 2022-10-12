my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
num = []
for i in my_list:
    if(i >= 10):
       num.append(i)
print(num)
input1=int(input("enter a value:"))
list2=[ i for i in my_list  if i>=input1]
print(list2)



    
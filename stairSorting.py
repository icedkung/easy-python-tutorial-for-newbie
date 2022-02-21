"""
input = 10
1
12
123
1234
12345
123456
"""
def stairsorting():
  #input value
 num = int(input("ป้อนตัวเลข = "))
 
 #loop print by value
 for row in range(1,num+1): 
     for column in range(1,row+1):
         print(column,end='')
     print(" ")

#function call
stairsorting()
"""
input = 3
row = 1 , 3
column 1,2
1
row 2
column 1, 3
12
row 3
column 1,4
123
"""

#class from P36 to P45, current is ===> P42

#位运算取反的结果是 -(x + 1), such as:  print(~12) ==> -13
#print(~12)  # -13

########################################################################
"""practice one: 给定一个5位之内的数,判断有几位"""

while True:
    try:
        num = int(input("Enter a integer number: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue
    if  0 <= num <= 99999:
        if num/10000 >1:
            print("5 bit integer")
        elif num/1000 >1:
            print("4 bit integer")

        elif num/100 >1:
            print("3 bit integer")
        elif num/10 >1:
            print("2 bit integer")
        else :
            print("1 bit integer")
        break

########################################################################


#print(list(range(10, 0,-1)))







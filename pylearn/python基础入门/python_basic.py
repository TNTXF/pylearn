#class from P36 to P45, current is ===> P42

#位运算取反的结果是 -(x + 1), such as:  print(~12) ==> -13
#print(~12)  # -13

########################################################################
#practice one: 给定一个5位之内的数,判断有几位
"""
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
"""
########################################################################


#print(list(range(10, 0,-1)))

#for loop
'''
for i in range(10):
    if not i%2:
        print(i)
'''

'''
count = 0
for i in range(0,1000,7):
    print(i)
    count += 1
    if count >= 20:
        print(count)
        break
'''
########################################################################
#给定一个不超过5位的正整数，判断其有几位，依次打印每位的数字
#vs code 乱码解决：新建一个环境变量，key=PYTHONIOENCODING  value=UTF-8
'''
def print_digits(number: int):
    if 1 <= number <= 99999:
        number_str = str(number)
        digit_count = len(number_str)
        print(f"这个数有 {digit_count} 位")
        
        for i, digit in enumerate(number_str, 1):
            print(f"第 {i} 位：{digit}")
    else:
        print("please enter a number that is between 1 and 99999")

print_digits(12385)
'''



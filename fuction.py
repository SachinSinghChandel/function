# def sum(a,b):
#     return a+b
# print(sum(5,6))
 
# # or
# def sum(a,b):
#     sum=a+b
#     return sum
# print(sum(2,4)) 

# def avrage(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     return avg
# print(avrage(1,2,3))
    
# # WAF to print the length of list (list is the  parameter)
# marks=[40,86,2,5666,2252,34,24,3,6]
# # def cal_list(list):
# #     print(len(list))
# # cal_list(marks)
# #WAF to print the element of the list in single line(list is the parameter)
# def el_list(list):
#     for item in list:
#         print(item,end=" ")    #end=""(this is done for printing the value in same line)
# el_list(marks)

# WAF find the factorial of the n (n is parameter)
# def fact_n(n):
#     fact=1
#     for i in range (1,n+1):
#         fact*=i
#     print(fact)
# fact_n(6)
# # write convert USD in INR
# def convert(USD):
#     return USD*80
# print(convert(4))
# #WAF take number from user if the number is odd print string "odd " if even print "even"

num=int (input( "your number is:"))
def check():
    if (num % 2==0):
        print("even")
    else:
        print("odd")
check(num)            

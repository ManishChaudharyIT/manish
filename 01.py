# Here are following questions like
'''
1.Prime number checking and prime number between
2.Armstrong checking
3.Even odd chekcing  even number between
4.Palindrome checking and palindrome string checking
5.Reverse digit and reverse string
6.Sum of digit 

'''
#checking given number is prime or not 
'''num=int(input('Enter the number'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count +=1
    
if count==2:
    print("Yes This is prime number")
else:
    print("This is not a prime number")'''
# two number between prime number
start=int(input("Enter the starting number::"))
end=int(input("Enter the Ending number/last number::"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)

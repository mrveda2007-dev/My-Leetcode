n=int(input("enter a number"))
result=[]
for i in str(n):
    result.append(i)

c1=result[::-1]

# int("".join(map(str,result))) == int("".join(map(str,c1)))
if result == c1 :
    print("palindrome")
else:
    print("not a palindrome")


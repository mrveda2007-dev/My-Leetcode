import math
class power:
    def power_of_two(self,n):
        if n<1:
            print("power value cannot be generated!!")
            return False
        #for i in range(n):
            #if math.pow(2,i) == n:
                #print("it is power of two at ",i) 
                #break
            #if math.pow(2,i)>n:
                #print("it is not a power of two!")
                #break
        while n%2==0:
            n = n/2
        if n == 1 :
            return True
        else:
            return False
n=int(input("enter the number:"))
p=power()
print(p.power_of_two(n))
 

class number:
    def febonacci_number(self,n):
        a=0
        b=1
        i=2
        if  n==0:
            return 0
        if n == 1:
            return 1
        while i<=n:
            a,b= b,a+b
            i+=1
        return b   
            
        
n=int(input("enter the fibonachi number:"))
num = number()
print(num.febonacci_number(n))
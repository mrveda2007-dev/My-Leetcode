class tribonacci_number:
    def tribonacci(self,n):
        t0 = 0
        t1 = 1
        t2 = 1
        if n==0 :
            return t0
        if n==1 or n==2:
            return t1
        i = 3
        while i <= n:
            t0,t1,t2 = t1,t2,t0+t1+t2
            i+=1
        return t2

tt = tribonacci_number()
n=int(input("enter a number for t : "))
print(tt.tribonacci(n))
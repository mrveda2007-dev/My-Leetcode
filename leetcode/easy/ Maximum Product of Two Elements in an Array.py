class array:
    def maxProduct(self,n):
        max=0
        l1=[]
        for i in n :
            l1.append(i-1)
        for i in range(len(l1)):
            for j in range(i+1,len(l1)):
                if (l1[i]) * (l1[j]) > max:
                    max = l1[i]*l1[j]
        return max
    # def max(self,n):
    #     max1=max2=0
    #     for num in n:
    #                 if num > max1:
    #                     max2 = max1
    #                     max1 = num
    #                 elif num > max2:
    #                     max2 = num
    #     return((max1-1)*(max2-1))
         

n = input("enter array:")
l1 = []
for i in n:
    l1.append(int(i))
a=array()
print(a.maxProduct(l1))
# print(a.max(l1))





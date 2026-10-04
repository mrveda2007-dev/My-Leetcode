class Solution(object):
    def addToArrayForm(self, num, k):
        r = int("".join(map(str, num)))
        r = int(r)
        r += k
        r = str(r)
        li=[]
        for i in r :
            li.append(int(i)) 
        return li
s=Solution()
n = input('enter a number:')
li=[]
for i in n :
    li.append(i)
k=int(input("enter a value for k :"))
print(s.addToArrayForm(li,k))

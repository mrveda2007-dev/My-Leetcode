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
<<<<<<< HEAD
print(s.addToArrayForm(li,k))
=======
print(s.addToArrayForm(li,k))
>>>>>>> b2f8eb56b1ecf1b40c218bbc4feacaf86a0963d9

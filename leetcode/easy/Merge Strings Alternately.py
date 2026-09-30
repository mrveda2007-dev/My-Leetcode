# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.
class Solution(object):
    def mergeAlternately(self, w1, w2):
        self.w1=w1
        self.w2=w2
        i,j=0,0
        n1,n2=len(w1),len(w2)
        result = []
        while i<n1 or j<n2:
            if i<n1:
                result.append(w1[i])
                i+=1
            if j<n2:
                result.append(w2[j])
                j+=1
        
        return " ".join(result)

w1 = input("enter word 1:")
w2 = input("enter word 2:")
Solutions=Solution()
print(Solutions.mergeAlternately(w1,w2))


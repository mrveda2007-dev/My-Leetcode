class parantheses:
    def valid_parantheses(self,s):
        p=[]
        condition ={")":"(",
                    "}":"{",
                    "]":"["}
        for i in s :
            if i in condition.values():
                p.append(i)
            elif i in condition:
                if not p or p[-1] != condition[i]:
                    return False
                
                p.pop()
        return not p

    
s = input("enter the parantheses sequence:")
p=parantheses()
print(p.valid_parantheses(s))
# class Parentheses:
#     def isValid(self, s: str) -> bool:
#         p = []
        
#         for char in s:
#             match char:
#                 case '(' | '{' | '[':
#                     p.append(char)
#                 case ')':
#                     if not p or p.pop() != '(': return False
#                 case '}':
#                     if not p or p.pop() != '{': return False
#                 case ']':
#                     if not p or p.pop() != '[': return False
                    
#         return not p

class sum :
        def twoSum(self, nums, target):
            found =False
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        found = True
                        return i,j
                        break
            if found == False: 
                print("target not found") 

num=[1,2,3,8]
target = 9
s=sum()
print(s.twoSum(num,target))
class Solution:
    def jump(self, nums: List[int]) -> int:
        Stack = [len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            while len(Stack)>=2 and (i + nums[i] >= Stack[-2]):
                Stack.pop()
            Stack.append(i)
        return len(Stack) - 1
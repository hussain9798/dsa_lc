class Solution:
    def twoSum(self, nums, target):
       
        seen = {}

        # Loop through the list with both index and value
        for i, num in enumerate(nums):
            # Calculate the number we need to reach the target
            diff = target - num

            # Check if that needed number is already in 'seen'
            if diff in seen:
                # If yes, return the index of that number and current index
                return [seen[diff], i]

            # Otherwise, store the current number with its index
            seen[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    res = obj.twoSum(nums, target)
    print(res)
    
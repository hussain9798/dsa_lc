# 4_sum solve with two pointer technique
# Input = [1, 0, -1, 0, -2, 2], target = 0

def four_sum(arr, target):
    n = len(arr)
    
    # Step 1: Sort the array (important for skipping duplicates & two-pointer approach)
    arr.sort()
    
    # To store all unique quadruplets
    res = []
    
    # Step 2: First loop - pick the first element
    for i in range(n - 3):  # we need 4 numbers, so stop at n-3
        # Skip duplicate values for the first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        # Step 3: Second loop - pick the second element
        for j in range(i + 1, n - 2):  # stop at n-2 because we need at least 2 more numbers
            # Skip duplicate values for the second element
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            
            # Step 4: Use two pointers for the remaining two elements
            left, right = j + 1, n - 1
            
            # Step 5: Check all possible pairs between left and right
            while left < right:
                s = arr[i] + arr[j] + arr[left] + arr[right]  # current sum of 4 numbers
                
                if s == target:  # Found a valid quadruplet
                    res.append([arr[i], arr[j], arr[left], arr[right]])
                    
                    # Skip duplicate values for the third element
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    # Skip duplicate values for the fourth element
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    
                    # Move both pointers after finding a quadruplet
                    left += 1
                    right -= 1
                
                elif s < target:  # If sum too small, move left pointer to increase sum
                    left += 1
                else:  # If sum too large, move right pointer to decrease sum
                    right -= 1
    
    return res


# Driver code
if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    res = four_sum(arr, target)
    print(res)   # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

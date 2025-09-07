# 3Sum solution using two pointers technique
# Given an array, find all unique triplets that sum up to 0
# Example input = [-1, 0, 1, 2, -1, -4]

def three_sum(arr):
    n = len(arr)
    arr.sort()  # Sort array to simplify duplicate handling and two-pointer logic
    res = []    # Store result triplets
    
    # Loop through the array (fix one element and find the other two using two pointers)
    for i in range(n - 2):
        
        # Skip duplicate elements for the first number
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        # Initialize two pointers
        left, right = i + 1, n - 1
        
        while left < right:
            s = arr[i] + arr[left] + arr[right]  # Calculate sum of triplet
            
            if s == 0:
                res.append([arr[i], arr[left], arr[right]])  # Found a valid triplet
                
                # Skip duplicates for left pointer
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                    
                # Skip duplicates for right pointer
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                    
                # Move both pointers inward
                left += 1
                right -= 1
                
            elif s < 0:
                left += 1  # Need a bigger sum → move left pointer
            else:
                right -= 1  # Need a smaller sum → move right pointer
    
    return res

# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    res = three_sum(arr)
    print(res)  # Expected output: [[-1, -1, 2], [-1, 0, 1]]

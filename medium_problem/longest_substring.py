class Solution:
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store last seen index of each character
        seen = {}
        left = 0   # Left pointer of the sliding window
        max_len = 0  # Variable to store the maximum length found

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is seen and its index is within current window
            if s[right] in seen and seen[s[right]] >= left:
                # Move left pointer to one position after the last occurrence
                left = seen[s[right]] + 1

            # Update the last seen index of the character
            seen[s[right]] = right
            # Calculate the maximum length of substring without repeating characters
            max_len = max(max_len, right - left + 1)

        return max_len


def main():
    s = "abcabcbb"   # Example input
    obj = Solution()  # Create object of Solution class
    res = obj.lengthOfLongestSubstring(s)  # Call the method
    print("Length of longest substring without repeating characters:", res)


if __name__ == "__main__":
    main()

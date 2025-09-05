from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])
        
        merged = []  # to store final merged intervals
        
        # Step 2: Initialize with the first interval
        start, end = intervals[0]
        
        # Step 3: Traverse through all intervals
        for i in range(1, len(intervals)):
            # If overlapping (next interval start <= current end)
            if intervals[i][0] <= end:
                # Extend the end to cover overlap
                end = max(end, intervals[i][1])
            else:
                # No overlap → push current interval to result
                merged.append([start, end])
                # Update start and end with new interval
                start, end = intervals[i]
        
        # Step 4: Append the last interval
        merged.append([start, end])
        
        return merged


# ------------------ MAIN FUNCTION ------------------
if __name__ == "__main__":
    obj = Solution()
    
    # Example input
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    # Call function
    result = obj.merge(intervals)
    
    # Print output
    print("Merged Intervals:", result)

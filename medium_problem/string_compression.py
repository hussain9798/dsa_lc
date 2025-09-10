# sorting string by counting character frequencies
# Example input = "LeetCode"

def string_compress(s):
    dct = {}   # dictionary to store character counts
    res = ""   # result string to store final compressed output
    
    # Step 1: Count frequency of each character
    for ch in s:
        dct[ch] = dct.get(ch, 0) + 1   # increment count if exists, else set 1
        
    # Step 2: Build result string with char + frequency
    for key, value in dct.items():
        res += key + str(value)   # concatenate key + count (convert count to string)
    
    return res

if __name__ == "__main__":
    s = "LeetCode"   # test string
    res = string_compress(s)
    print(res)       # Example output: L1e2t1C1o1d1

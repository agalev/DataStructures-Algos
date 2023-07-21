# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/
def sumOddLengthSubarrays(arr: list[int]) -> int:
        total = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                total += sum(arr[i:j+1])
        return total

# Test Cases
print(sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(sumOddLengthSubarrays([1,2])) # 3
print(sumOddLengthSubarrays([10,11,12])) # 66
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        # result = []
        # for i in candies:
        #     if i + extraCandies >= max(candies):
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        return [True if i + extraCandies >= max(candies) else False for i in candies]

# Test Cases
print(kidsWithCandies([2,3,5,1,3], 3)) # [True,True,True,False,True]
print(kidsWithCandies([4,2,1,1,2], 1)) # [True,False,False,False,False]
print(kidsWithCandies([12,1,12], 10)) # [True,False,True]
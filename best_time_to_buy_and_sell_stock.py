class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 9999
        largest_diff = 0
        highest = 0
        highest_after_lowest = False
        for i in prices:
            if i < lowest:
                lowest = i
                highest_after_lowest = False
            if (i > highest or highest_after_lowest == False) and lowest != i:
                highest = i
                highest_after_lowest = True
            if highest_after_lowest == True and highest - lowest > largest_diff:
                largest_diff = highest - lowest
            # print("low:", lowest, " high:", highest, " largest diff:", largest_diff)
            #if highest_after_lowest == True:
            #    print("highest after lowest true")
            #else:
            #    print("highest after lowest false")
        return largest_diff

        
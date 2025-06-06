class Solution:
    def candy(self, ratings: List[int]) -> int:
        r = len(ratings)
        candies = [1] * r

        for i in range(1, r):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(r - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
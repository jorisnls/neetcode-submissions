class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = [0] * 2000
        for num in nums:
            if num >= 0:
                count[num] += 1
            else:
                print(-num+1000)
                count[-num+1000] += 1

        result = []
        for i in range(k):
            frequent = max(count)
            index = count.index(frequent)
            if index < 1000:
                result.append(index)
                count[index] = 0
            else:
                result.append(-index+1000)
                count[index] = 0


        return result
        
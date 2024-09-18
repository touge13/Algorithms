class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = -1 # указатель для хранения последней позиции 1
        maxDistance = 0
        for r in range(len(seats)):
            if seats[r] == 1:
                if l == -1: # если окно из нулей с начала
                    maxDistance = r
                else: # между двумя единицами => // 2
                    maxDistance = max(maxDistance, (r - l) // 2)
                l = r
        # если окно из нулей от последней единицы до конца списка
        maxDistance = max(maxDistance, len(seats) - l - 1)
        return maxDistance

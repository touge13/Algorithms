class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        p1 = p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])
            # проверим существует ли пересечение
            if start <= end:
                res.append([start, end])
            # смотрим какой интервал закончился раньше
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return res

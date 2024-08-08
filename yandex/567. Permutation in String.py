# O(N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # создадим хэш таблицу с символами строки s1
        hm1 = {}
        for i in s1:
            if i in hm1:
                hm1[i] += 1
            else:
                hm1[i] = 1
        
        # пробежимся по s2 скользящим окном
        l = r = 0
        hm2 = {}
        while r < len(s2):
            #  создадим хэш таблицу с символами строки s2
            if s2[r] in hm2:
                hm2[s2[r]] += 1
            else:
                hm2[s2[r]] = 1
            # скользящее окно
            if r - l == len(s1):
                if hm2[s2[l]] == 1:
                    del hm2[s2[l]]
                else:
                    hm2[s2[l]] -= 1
                l += 1
            # проверка
            if hm1 == hm2:
                return True
                
            r += 1
        return False
        

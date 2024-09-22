class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {} 
        for i in words:
            d[i] = 1 + d.get(i, 0)
        res = sorted(d, key=lambda x: (-d[x], x))
        return res[:k]

# res = sorted(d, key=lambda x: (-d[x], x))
# Эта функция сортирует ключи словаря (слова)
# -d[x]: минус перед d[x] означает, что мы сортируем по частоте в обратном порядке.
# x: Если частоты одинаковые, слова сортируются по алфавиту

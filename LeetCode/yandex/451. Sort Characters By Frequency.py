class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = 1 + freq.get(ch, 0)
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return ''.join([key * val for key, val in freq])


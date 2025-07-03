class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        l = 0
        for r in range(len(chars)):
            if chars[r] != chars[l]:
                chars[i] = chars[l]
                i += 1
                if r - l > 1:
                    for n in str(r - l):
                        chars[i] = n
                        i += 1
                l = r
        chars[i] = chars[l]
        i += 1
        if r - l + 1 > 1:
            for n in str(r - l + 1):
                chars[i] = n
                i += 1
        return i

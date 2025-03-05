class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        pos = 0
        ch = chars[0]
        for r in range(len(chars)):
            if chars[r] != ch:
                chars[pos] = ch
                ch = chars[r]
                if r - l > 1:
                    for i in range(len(str(r - l))):
                        chars[pos + 1 + i] = str(r - l)[i]
                    pos += len(str(r - l)) + 1
                else:
                    pos += 1
                l = r
        chars[pos] = ch
        if r - l + 1 > 1:
            for i in range(len(str(r - l + 1))):
                chars[pos + 1 + i] = str(r - l + 1)[i]
            pos += len(str(r - l + 1)) + 1
        else:
            pos += 1
        return pos

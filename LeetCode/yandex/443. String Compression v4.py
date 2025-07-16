class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        ch = chars[0]
        cnt = 0
        for r in range(len(chars)):
            if chars[r] != ch:
                chars[l] = ch
                l += 1
                if cnt > 1:
                    for i in range(len(str(cnt))):
                        chars[l] = str(cnt)[i]
                        l += 1
                cnt = 1
                ch = chars[r]
            else:
                cnt += 1
        chars[l] = ch
        l += 1
        if cnt > 1:
            for i in range(len(str(cnt))):
                chars[l] = str(cnt)[i]
                l += 1
        return l

class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        while r < len(chars):
            char = chars[r]
            count = 0
            
            while r < len(chars) and chars[r] == char:
                r += 1
                count += 1
            
            chars[l] = char
            l += 1
            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l += 1
        
# chars[:] = chars[:l] изменяет существующий список, сохраняя его объект.
# chars = chars[:l] создает новый список и присваивает его переменной chars.
        chars[:] = chars[:l]
        
        return len(chars)

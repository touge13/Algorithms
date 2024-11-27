# решето Эратосфена

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        a = [1] * (n + 1)
        a[0] = a[1] = 0 # 0 и 1 не являются простыми числами
        a[n] = 0 # n не включительно
# Внешний цикл проходит только до sqrt(n), так как все кратные до этого числа уже будут помечены.
        for r in range(2, int(n ** 0.5) + 1): 
            if a[r] == 1:
# Все кратные a[r] = r, меньшие чем a[r^2] = r^2, уже были обработаны на предыдущих шагах.
                for k in range(r * r, n, r):
                    a[k] = 0
        return sum(a)
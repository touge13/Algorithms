class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        res = 0
        while l < r:
            if skill[l] + skill[r] == skill[0] + skill[-1]:
                res += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return res

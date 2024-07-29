class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        negativeNums = []
        zeros = []
        positiveNums = []
        for num in nums:
            if num > 0:
                positiveNums.append(num)
            elif num == 0:
                zeros.append(num)
            else:
                negativeNums.append(num)
        
        #2. Create a separate set for negatives and positives for O(1) look-up times
        n = set(negativeNums)
        p = set(positiveNums)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	    # i.e. (-3, 0, 3) = 0
        if zeros:
            for num in p:
                if -1*num in n:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(zeros) >= 3:
            res.add((0, 0, 0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    	# exists in the positive number set
        for i in range(len(negativeNums)):
            for j in range(i+1, len(negativeNums)):
                if -1*(negativeNums[i] + negativeNums[j]) in p:
                    res.add(tuple(sorted([negativeNums[i], negativeNums[j], -1*(negativeNums[i] + negativeNums[j])])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	    # exists in the negative number set
        for i in range(len(positiveNums)):
            for j in range(i+1, len(positiveNums)):
                if -1*(positiveNums[i] + positiveNums[j]) in n:
                    res.add(tuple(sorted([positiveNums[i], positiveNums[j], -1*(positiveNums[i] + positiveNums[j])])))
        
        return res

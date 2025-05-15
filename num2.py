def combinationSum2(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])
    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result

candidates1 = [2, 5, 2, 1, 2]
target1 = 5
print(combinationSum2(candidates1, target1))

candidates2 = [10, 1, 2, 7, 6, 1, 5]
target2 = 8
print(combinationSum2(candidates2, target2))

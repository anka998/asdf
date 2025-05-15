def count_jewels(J, S):
    return sum(S.count(jewel) for jewel in J)
J = "ab"
S = "aabbccd"
result = count_jewels(J, S)
print(result)
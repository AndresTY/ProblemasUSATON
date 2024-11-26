def max_score(s):
    scores = {}
    for pivot in range(len(s)):
        left_side, right_side = list(s[:pivot + 1]), list(s[pivot + 1:])
        if not left_side or not right_side:
            continue
        scores[pivot] = left_side.count('0') + right_side.count('1')
    
    return max(scores.values()) if scores else 0

t = int(input())
for _ in range(t):
    print(max_score(input()))
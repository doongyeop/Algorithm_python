s = input().strip().upper()

letters = set(s)
max_cnt = 0
result = ''

for l in letters:
    cnt = s.count(l)
    if cnt > max_cnt:
        max_cnt = cnt
        result = l
    elif cnt == max_cnt:
        result = '?'

print(result)

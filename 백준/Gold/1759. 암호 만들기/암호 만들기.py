import sys

input = sys.stdin.readline

l, c = map(int, input().split())
alps = list(map(str, input().split()))
alps.sort()


def check(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for l in line:
        if l in vowels:
            count += 1

    return count >= 1 and len(line) - count >= 2

ans = []
def password_maker(password, idx):
    if len(password) == l:
        if check(password):
            ans.append(password)
        return

    if idx >= c:
        return

    password_maker(password, idx + 1)
    password_maker(password + alps[idx], idx + 1)

password_maker("", 0)
ans.sort()

print('\n'.join(ans))
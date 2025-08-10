def solution(n, words):
    used = set()
    prev = words[0]
    used.add(prev)

    for i in range(1, len(words)):
        word = words[i]
        if word in used:
            return [(i % n) + 1, (i // n) + 1]
        if prev[-1] != word[0]:
            return [(i % n) + 1, (i // n) + 1]

        used.add(word)
        prev = word

    return [0, 0]  


def solution(sides):
    sides.sort()
    print(sides)
    tri = sides[0] + sides[1]
    return 1 if tri > sides[2] else 2
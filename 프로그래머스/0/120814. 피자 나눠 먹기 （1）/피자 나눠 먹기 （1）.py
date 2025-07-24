def solution(n):
    pizzas = n // 7 + 1 if n % 7 != 0 else n // 7
    return pizzas
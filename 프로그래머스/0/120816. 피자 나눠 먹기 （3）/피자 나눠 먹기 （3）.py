def solution(slice, n):
    pizzas = n // slice + 1 if n % slice != 0 else n // slice
    return pizzas


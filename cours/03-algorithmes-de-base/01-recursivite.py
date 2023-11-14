# Suite de Fibonacci
# 1, 2, 3, 5, 8, 13

def fibonacci(n):
    # Calculer le n-ième terme de fibonacci
    # Les deux premiers termes de la suite sont 0 et 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 // n2


ans = add(10, 20)
ans += sub(ans, 10)  # ans = ans + sub(ans, 10)
ans -= multiply(ans, 20)  # ans = ans - multiply(ans, 20)
ans *= div(ans, 10)  # ans = ans * div(ans, 10)

print(ans)

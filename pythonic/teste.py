def fibonacci1(n):
    prev = 1
    curr = 1
    yield 1
    for _ in range(n-1):
        prev, curr = curr, curr + prev
        yield curr

def fibonacci2(n):
    result = [1]
    prev = 1
    curr = 1
    for _ in range(n-1):
        prev, curr = curr, curr + prev
        result.append(curr)
    return result

# Testing the functions
for i in fibonacci1(6):
    print(i)
for i in fibonacci2(6):
    print(i)
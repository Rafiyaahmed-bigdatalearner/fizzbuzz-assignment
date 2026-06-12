def generate_fizzbuzz(int1: int, int2: int, limit: int, str1: str, str2: str):
    result = []

    for i in range(1, limit + 1):
        if i % int1 == 0 and i % int2 == 0:
            result.append(str1 + str2)
        elif i % int1 == 0:
            result.append(str1)
        elif i % int2 == 0:
            result.append(str2)
        else:
            result.append(str(i))

    return result
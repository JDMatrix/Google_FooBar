def solution(n):
    if n == '1':
        return 0

    cache = {0: 1,
             1: 0,
             2: 1,
             3: 2}

    current = long(n)
    count = 0

    while current != 1:
        if current in cache.keys():
            count += cache[current]
            break

        binary = bin(current)

        count_normal = 0
        for i in binary[::-1]:
            if current in cache.keys():
                count_normal = cache[current]
                break
            elif i == '0':
                count_normal += 1
            else:
                break

        plus_one = current + 1
        binary = bin(plus_one)
        count_plus_one = 0
        for i in binary[::-1]:
            if plus_one in cache.keys():
                count_plus_one = cache[plus_one]
                break
            elif i == '0':
                count_plus_one += 1
            else:
                break

        minus_one = current - 1
        binary = bin(minus_one)
        count_minus_one = 0
        for i in binary[::-1]:
            if minus_one in cache.keys():
                count_minus_one = cache[minus_one]
                break
            elif i == '0':
                count_minus_one += 1
            else:
                break

        if count_normal == max(count_normal, count_plus_one, count_minus_one):
            current /= 2 ** count_normal
            count += count_normal

        elif count_plus_one == max(count_normal, count_plus_one, count_minus_one):
            current += 1
            current /= 2 ** count_plus_one
            count += count_plus_one + 1

        elif count_minus_one == max(count_normal, count_plus_one, count_minus_one):
            current -= 1
            current /=  2 ** count_minus_one
            count += count_minus_one + 1

    return count


def main():
    assert solution('15') == 5
    assert solution('4') == 2
    assert solution('5') == 3
    assert solution('1') == 0
    assert solution('3') == 2
    assert solution('6') == 3
    assert solution('0') == 1
    assert solution('2') == 1


if __name__ == '__main__':
    main()

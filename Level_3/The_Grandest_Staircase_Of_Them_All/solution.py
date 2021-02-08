import math


def solution(n):
    partition = PartitionQ(n + 1)
    return partition.q(n) - 1


def calc_j_seq(max_n):
    result = {}
    j = 0
    val_n = -1
    while val_n <= max_n:
        jj = 3 * j * j
        val_p, val_n = (jj - j) // 2, (jj + j) // 2
        result[val_p] = j
        result[val_n] = j
        j += 1

    return result


class PartitionQ:
    def __init__(self, max_n):
        self.max_n = max_n
        self.j_seq = calc_j_seq(max_n)
        self.cache = {}

    def q(self, n):
        if self.cache.get(n) is None:
            assert n < self.max_n
            if n == 0:
                return 1

            sqrt_n = int(math.sqrt(n)) + 1
            temp = sum(((-1) ** (k + 1)) * self.q(n - k * k) for k in range(1, sqrt_n))
            self.cache[n] = 2 * temp + self.s(n)
            return self.cache[n]
        else:
            return self.cache.get(n)

    def s(self, n):
        if n in self.j_seq:
            return (-1) ** self.j_seq[n]
        else:
            return 0


def main():
    assert solution(200) == 487067745
    assert solution(3) == 1
    assert solution(4) == 1
    assert solution(5) == 2
    assert solution(6) == 3
    assert solution(7) == 4
    assert solution(8) == 5
    assert solution(9) == 7
    assert solution(10) == 9
    assert solution(11) == 11
    assert solution(12) == 14
    assert solution(13) == 17
    assert solution(14) == 21
    assert solution(15) == 26
    assert solution(16) == 31
    assert solution(17) == 37
    assert solution(18) == 45
    assert solution(19) == 53
    assert solution(20) == 63
    assert solution(21) == 75
    assert solution(22) == 88
    assert solution(23) == 103
    assert solution(24) == 121
    assert solution(25) == 141
    assert solution(26) == 164
    assert solution(27) == 191
    assert solution(28) == 221
    assert solution(29) == 255
    assert solution(50) == 3657
    assert solution(100) == 444792


if __name__ == '__main__':
    main()

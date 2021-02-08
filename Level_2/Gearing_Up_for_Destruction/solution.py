from fractions import Fraction


def solution(beam):
    vector = [float(b - beam[i - 1]) if i > 0 else 0.0 for i, b in enumerate(beam)]
    first_row = [1.0] + [0.0 for _ in range(0, len(beam) - 2)] + [-2.0]
    second_row = [1.0, 1.0] + [0.0 for _ in range(0, len(beam) - 2)]
    matrix = [first_row, second_row]

    for i in range(1, len(beam) - 1):
        matrix.append([0.0] + matrix[i][:-1])

    for i, e, in enumerate(matrix):
        e.append(float(vector[i]))

    result = gauss(matrix)

    for i in result:
        if i < 1:
            return [-1, -1]

    # Important to use high enough precision of the fraction
    f = Fraction(result[0]).limit_denominator(1000000000)
    a = f.numerator
    b = f.denominator

    return [int(a), int(b)]


def gauss(a):
    """ Solve system of equations using Gauss method"""

    n = len(a)
    for i in range(0, n):
        max_el = abs(a[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(a[k][i]) > max_el:
                max_el = abs(a[k][i])
                max_row = k

        for k in range(i, n + 1):
            tmp = a[max_row][k]
            a[max_row][k] = a[i][k]
            a[i][k] = tmp

        for k in range(i + 1, n):
            c = -a[k][i] / a[i][i]
            for j in range(i, n + 1):
                if i == j:
                    a[k][j] = 0
                else:
                    a[k][j] += c * a[i][j]

    # solve ax=b
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n] / a[i][i]
        for k in range(i - 1, -1, -1):
            a[k][n] -= a[k][i] * x[i]

    return x


def main():
    assert solution([4, 30, 50]) == [12, 1]
    assert solution([4, 17, 50]) == [-1, -1]
    assert solution([4, 30, 58, 78]) == [12, 1]


if __name__ == '__main__':
    main()

from collections import OrderedDict


def solution(data, n):
    new_list = []
    final_list = []
    count_dict = OrderedDict()

    for i in data:
        if i in count_dict.keys():
            count_dict[i] = count_dict.get(i) + 1
        else:
            count_dict[i] = 1

    for i in count_dict.keys():
        if count_dict.get(i) <= n:
            new_list.append(i)

    for i in data:
        if i in new_list:
            final_list.append(i)

    return final_list


def main():
    assert solution([5, 10, 5, 5, 10, 7, 3, 5], 3) == [10, 10, 7, 3]
    assert solution([5, 5, 5, 5, 5], 0) == []
    assert solution([], 3) == []
    assert solution([5, -1, 'a', 'a', ], 1) == [5, -1]
    assert solution([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 5) == [2, 2, 2, 2, 2]


if __name__ == '__main__':
    main()

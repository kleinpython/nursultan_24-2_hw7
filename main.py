def binary_search(target: int, lst: list):
    l, r = 0, len(lst)
    while l + 1 < r:
        m = (l + r) // 2
        if target == lst[m]:
            print(f'Число найдено под индексом {m}')
            r, l = m, m
            break
        if target > lst[m]:
            l = m + 1

        if target < lst[m]:
            r = m

    if lst[l] != target:
        print('Число не найдено')


binary_search(6, [1, 2, 3, 4, 5, 7])


def bubble_sort(a: list):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = bubble_sort([7, 34, 4, 6, 5, 65, 6, 56])
print(a)

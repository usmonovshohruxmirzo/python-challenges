def sum_odd_and_even(lst):
    even = []
    sum_even = 0

    odd = []
    sum_odd = 0

    even_and_odd = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)
        elif num % 2 == 1:
            odd.append(num)

    for e in even:
        sum_even += e

    for o in odd:
        sum_odd += o

    even_and_odd.append(sum_even)
    even_and_odd.append(sum_odd)

    return even_and_odd

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
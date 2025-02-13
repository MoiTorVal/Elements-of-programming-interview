def even_odd(A: list[int]) -> None:
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1 
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even ]
            next_odd -= 1        

a = [3, 1, 2, 4, 6, 5]
even_odd(a)
print(a)

    
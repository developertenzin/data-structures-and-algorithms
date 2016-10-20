# Uses python3
def max_pairwise_product():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    max = 0
    max_index = 0
    for num in range(0, n):
        if a[num] > max:
            max = a[num]
            max_index = num

    max1 = 0
    for num1 in range(0, n):
        if a[num1] > max1 and num1 != max_index:
            max1 = a[num1]

    print(max * max1)



max_pairwise_product()

'''
#slow solution
result = 0

for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)
'''


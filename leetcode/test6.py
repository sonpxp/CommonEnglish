# def largest(arr, n):
#     return max(arr)
#
#
# print(largest(arr, n))


# def largestElement(array):
#     n = len(array)
#     array.sort()
#     return array[n - 1]
#
#
# print(largestElement(arr))

arr = [10, 324, 45, 15, 90, 9808]


# def largestElement1(arr: []):
#     max_element = arr[0]
#
#     for i in range(0, len(arr)):
#         if arr[i] > max_element:
#             max_element = arr[i]
#
#     return max_element
#
#
# print(largestElement1(arr))


def largestElement2(arr: []):
    n = len(arr)
    new_list = []

    for i in range(0, n):
        max1 = 0
        for j in range(len(arr)):
            if arr[j] > max1:
                max1 = arr[j]


        arr.remove(max1)
        new_list.append(max1)

    return new_list  # [::-1]


print(largestElement2(arr))


# def largest_ele(l):
#     n = len(l)
#     s = []
#
#     for i in range(n):
#         s.append(max(l))
#         l.remove(max(l))
#     print('by largest_ele function: ', s)


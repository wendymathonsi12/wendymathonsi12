def partition(s, low, high):
    pivot = s[low]

    left , right = low + 1, high

    while left < right:
        print(s)

        while left <= right and s[left] <= pivot:
            left += 1
        
        while left <= right and s[right] >= pivot:
            right -= 1

        if left < right:
            s[left], s[right] = s[right], s[left]

    pivot_point = right
    s[low], s[pivot_point] = s[pivot_point], s[low]
    return pivot_point, "\nExit with code o"
  

def quick_sort(S, low, high):

    if low < high:
        print(S)

        pv = partition(S, low, high)
        quick_sort(S, low, pv-1)
        quick_sort(S, pv + 1, high)

s_1 = [33, 22, 11, 55, 44]
quick_sort(s_1, 0, len(s_1) - 1)
print(s_1)

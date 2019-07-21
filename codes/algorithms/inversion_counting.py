def count_inversions_and_merge_sort(arr, start, end):

    if start>=end:
        return 0
    if end-start==1:
        if arr[start]>arr[start+1]:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            return 1
        else:
            return 0

    mid = (start+end)//2

    arr1 = list()
    arr2 = list()
    for i in range(mid+1):
        arr1.append(arr[i])
    for i in range(mid+1, end+1):
        arr2.append(arr[i])

    count1 = count_inversions_and_merge_sort(arr1, 0, mid)
    count2 = count_inversions_and_merge_sort(arr2, 0, len(arr2)-1)
    count = count1 + count2

    i=0
    j=0
    k=0

    while i<len(arr1) and j<len(arr2):
        if arr1[i]>arr2[j]:
            arr[k] = arr2[j]
            k += 1
            j += 1
            count += (len(arr1)-i)
        else:
            arr[k] = arr1[i]
            k += 1
            i += 1

    while i<len(arr1):
        arr[k] = arr1[i]
        k += 1
        i += 1

    while j<len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1
    return count

arr = list(map(int, input("Enter numbers to sort: ").split()))
print("List before sorting : ", arr)
print("No. of inversions = ", count_inversions_and_merge_sort(arr, 0, len(arr)-1))
print("List after sorting : ", arr)

def majorityelement(arr, n):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > n // 2:
        return candidate
    return -1


arr=[2,2,1,2,2]
print(majorityelement(arr,len(arr)))




def majorityelement(arr, n):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num

arr=[2,2,1,2,2]
n=len(arr)

result=majorityelement(arr,n)
print(result)
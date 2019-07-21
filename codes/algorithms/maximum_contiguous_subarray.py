arr = list(map(int, input("Enter array: ").split()))

dp = [arr[0]]
for i in range(1, len(arr)):
    dp.append(max(arr[i], dp[i-1]+arr[i]))

end_index = dp.index(max(dp))
start_index = end_index
sum = arr[end_index]
while sum!=max(dp):
    start_index = start_index - 1
    sum += arr[start_index]

print("The required array is from index", start_index, "to index", end_index)
print("The sum =", dp[end_index])


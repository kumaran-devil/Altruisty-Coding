k = int(input())
n = int(input())
arr = []

def max_of_mins(arr, k):
    max_min = float('-inf')
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        current_min = min(subarray)
        max_min = max(max_min, current_min)
    return max_min

for _ in range(n):
    arr.append(int(input()))

print(f"[{max_of_mins(arr, k)}]")

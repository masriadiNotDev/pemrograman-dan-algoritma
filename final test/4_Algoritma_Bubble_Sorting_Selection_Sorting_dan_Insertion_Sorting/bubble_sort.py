
# masriadi sisfo b D0425309

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

data = [50, 20, 40, 10, 30]
bubble_sort(data)
print("Bubble Sort:", data)

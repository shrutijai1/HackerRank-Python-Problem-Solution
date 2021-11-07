if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
arr.sort()
arr.reverse()
for i in range(n):
    if arr[0] > arr[i]:
        print(arr[i])
        break
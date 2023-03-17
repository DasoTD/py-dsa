def sev(arr= 5):
    for i in range(arr):
        for j in range(arr):
            print(i,j)

d = sev()

# Sum = (arr[i][j]+ arr[i][j+1] + arr[i][j+2])+ (arr[i + 1][j + 1]) + (arr[i + 2][j] +arr[i + 2][j + 1] + arr[i + 2][j + 2])

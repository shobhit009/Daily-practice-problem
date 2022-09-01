def maximize_profit(arr,n):
    profit = 0
    buy = arr[0]
    buyFlag = False

    for i in range(1,n-1):
        if arr[i]>arr[i+1] and buyFlag == False:
            profit += arr[i]-buy
            buyFlag = True
        elif buyFlag:
            if (arr[i]< arr[i+1]):
                buy = arr[i]
                buyFlag = False
        elif i+1 == n-1:
            profit += arr[i+1]-buy
        
    return 0 if profit < 0 else profit

def max_profit(arr,n):
    profit = 0
    for i in range (1,n):
        if arr[i] > arr[i-1]:
            profit += arr[i]-arr[i-1]
    return profit

print (max_profit([1,5,3,8,12],5))
arr = list(map(int, input().split()))
print([i for i in arr if i!=0] +[0]*arr.count(0)) 


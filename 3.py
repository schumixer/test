first = (int(input()),int(input()))
second = (int(input()),int(input()))
if abs(first[0] - second[0]) == abs(first[1] - second[1]) or first[0] == second[0] or first[1] == second[1]:
    print('YES')
else:
    print('NO')
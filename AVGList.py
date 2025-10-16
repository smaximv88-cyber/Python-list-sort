a = []
b = []
while True:
    req = int(input("Enter a number: "))
    a.append(req)
    if req == 0:
        break
a_len = len(a)
k = 0
b_sum = 0
while k < a_len:
    b_sum += a[k]
    k += 1
    b.append(round(b_sum/k, 2))
print(b)

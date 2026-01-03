# total = 188_000
# i = 0
# sum = 0
# while total > 0:
#     i+=1
#     square = i * i
#     if square % 2 == 1:
#         sum += square
#     total -= 1

sum = 0
for i in range(1, 188_001):
    square = i*i
    if square % 2 == 1:
        sum += square


print(sum)

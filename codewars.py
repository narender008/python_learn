#
# data = [[45, 12], [55, 21], [19, -2], [104, 20]]
#
#
# def openOrSenior(data):
#     empty = []
#     for i in data:
#         if i[0] >= 55 and i[1] >= 7:
#             empty.append("Senior")
#
#         else:
#             empty.append("Open")
#
#     return empty
#
#
# print(openOrSenior(data))


# def persistence(n):
#     mul = 1
#     dig = 0
#     count = 0
#     while(len(str(n))):
#         print(len(str(n))
#         while n:
#             rem=n % 10
#             mul=mul * rem
#             n=n / 10
#             dig=dig + 1
#             count += 1
#         print(mul)
#         count += 1
#
#
# print(persistence(39))


Number = 999
Count = 0
while(Number > 0):
    Number = Number // 10
    print(Number)
    Count = Count + 1

print("\n Number of Digits in a Given Number = ", Count)

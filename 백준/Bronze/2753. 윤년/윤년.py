year_score = int(input())

if year_score%4 == 0 and (year_score%100 !=0 or year_score%400 == 0):
    print(1)
else:
    print(0)
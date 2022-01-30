N = int(input())
X = input().split()


X.sort()
result = 0
count = 0

for idx , val in enumerate(X):
    count +=1

    if idx <=count:
        result +=1
        count = 0


print(result)

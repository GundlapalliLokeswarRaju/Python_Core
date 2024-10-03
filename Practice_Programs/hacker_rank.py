
# List compression
x = int(input())
y = int(input())
z = int(input())
n = int(input())
a = []
b = []
new = [x, y, z]
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            a.append([i,j,k])
for i in a:
    if sum(i) != n:
        b.append(i)
print(b)
#  2. Print second highest number
b =[]
n = int(input())
arr = map(int, input().split())
a= sorted(arr)
for i in a:
    if i == max(a):
        continue
    else:
        b.append(i)
print(max(b))
# nested list
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records = name, score


n=int(input("Enter range of number: "))
total = 0
count = 0

for num in range(1, n):
    total += num
    count += 1

average = total / count
print("Total: ",total)
print("count: ",count)
print("Average: ", average)

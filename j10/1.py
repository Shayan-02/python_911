input_line1 = input().split()
input_line2 = input().split()
count = 0
for i in range(8):
    if int(input_line1[i]) == int(input_line2[i]) == 1:
        count += 1
print(count)

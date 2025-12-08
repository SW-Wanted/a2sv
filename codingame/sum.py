
s = str(input())
def normal(i):
    c = 0
    if i >= 97 and i <= 97 + 26:
        c = (int(i) - 97) + 1
        print(c)
    elif i >= 65 and i <= 65 + 26:
        c = (int(i) - 65) + 1
        print(c)
    return (c)
print(sum(list(map(normal, list(map(ord, s))))))

# s = input().upper()
# total = 0
# for i in s:
#     total += ord(i)-64

# # Write an answer using print
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print(total)

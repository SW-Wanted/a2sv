
dna = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print("".join([{"A":"T","C":"G","G":"C","T":"A"}[x] for x in dna]))

words = dict()
words['A'] = 'T'
words['T'] = 'A'
words['C'] = 'G'
words['G'] = 'C'

letters = list()
for x in dna:
    letters.append(words[x])

print("".join(letters))

dna = input()

for i in dna:
    if i == 'A':
        print('T', end='')
    if i == 'C':
        print('G', end='')
    if i == 'G':
        print('C', end='')
    if i == 'T':
        print('A', end='')
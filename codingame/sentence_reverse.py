n = int(input())
while n:
    sentence = input()

    words = sentence.split(' ')
    words.reverse()
    print(" ".join(words))
    n -= 1
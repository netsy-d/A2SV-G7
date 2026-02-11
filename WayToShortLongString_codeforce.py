for _ in range(int(input())):
    words = input()
    if len(words) > 10:
        print(f" {words[0]}{str(len(words)-2)}{words[-1]}")
    else:
        print(words)

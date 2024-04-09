def edit_string(s):
    s = " ".join(s.split()).replace(" .", ".").split(". ")
    width = 0
    for sentence in s:
        if len(sentence) > width:
            width = len(sentence)
    for sentence in s:
        print(sentence.center(width))
s = input()
edit_string(s)
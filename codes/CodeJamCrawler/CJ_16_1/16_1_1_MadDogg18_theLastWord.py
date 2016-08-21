def theLastWord(s):
    winningWord=s[0]
    for char in s[1:]:
        if ord(char)>=ord(winningWord[0]):
            winningWord=char+winningWord
        else:
            winningWord=winningWord+char
    return winningWord




t = int(input())
for i in range(1, t + 1):
  print("Case #%d: %s" %(i,theLastWord(input())))


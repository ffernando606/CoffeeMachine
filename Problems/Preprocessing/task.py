text = input()
text = text.lower()
text = text.strip(",.!?")
print(text.replace("!", ""))
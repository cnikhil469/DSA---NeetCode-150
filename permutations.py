#finding the permutations of a string

def permutations(name, i=0, wordsList=[]):
    if (i == len(name) and name not in wordsList):
        wordsList.append(''.join(name))
        return
    for j in range(i, len(name)):
        words = [c for c in name]
        words[i], words[j] = words[j], words[i]
        permutations(words, i+1, wordsList)
    return wordsList

print(permutations('ABC'))

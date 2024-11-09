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

def checkInclusion(s1: str, s2: str) -> bool:
    p = permutations(s1)
    print(p)
    l, r, lens1 = 0, len(s2), len(s1)
    while(l<r):
        if lens1+l<=r and s2[l:l+lens1] in p:
            return True
        l += 1
    return False

print(checkInclusion("ab", "lecabeehbh"))

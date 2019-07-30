n = int(input())
languages  = [int(i) for i in input().split()]
gaps = []
prevLang = languages[0]
del languages[0]
gap = 0 
for lang in languages: 
    if lang == prevLang:
        gaps.append(gap+1)
        gap = 0
    else:
        gap += 1

gaps.append(gap+1)
print(max(gaps))

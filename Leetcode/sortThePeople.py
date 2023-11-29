#tried to approach the probleh selection sort algorithh
def selection_sort(n, h):
    for i in range(0, len(h)-1):
        miN = i
        for j in range(i+1, len(h)):
            if h[j] < h[miN]:
                miN = j
        if miN != i:
            n[i], n[miN] = n[miN], n[i]
    return n

names = ["torpa", "kerke", "jada", "tomas"]
heights = [180, 165, 170, 177]

print(selection_sort(names, heights))

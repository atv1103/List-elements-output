num = int(input())
list_from = []
list_search = []
list_result = []
for _ in range(num):
    text = input()
    list_from.append(text)
print(list_from)
k = int(input())
for c in range(k):
    search = input()
    list_search.append(search)
print(list_search)
for i in range(len(list_from)):
    counter = 0
    for j in range(len(list_search)):
        if list_search[j].lower() in list_from[i].lower():
            counter += 1
            if counter == len(list_search):
                list_result.append(list_from[i])

print(*list_result, sep='\n')


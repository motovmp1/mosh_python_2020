from pprint import pprint

sentence = "this is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency, width=1)

final_list = (sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True))

pprint(final_list, width=1)

print(f' final list most element is: {final_list[0]}')

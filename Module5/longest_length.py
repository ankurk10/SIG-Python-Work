print("Ankur Kumar Kushwaha   1900300100034")

def longest_word(list):
    word_length = []
    for n in list:
        word_length.append((len(n), n))
    word_length.sort()
    return word_length[-1][1]

print(longest_word(["Python", "C++", "C", "Java", "Android"]))

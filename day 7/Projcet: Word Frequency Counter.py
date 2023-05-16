# Using Sets, make a Word Frequency Counter that reads a text file, counts the frequency of each word in the file,
# and displays the unique words along with their frequencies.
import string

# Reads a .txt file
unique_word = set()
word_freq = {}
with open("sample.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            word = word.strip(string.punctuation)
            unique_word.add(word)
            if word in unique_word:
                if word not in word_freq:
                    word_freq[word] = 0
                else:
                    pass
                word_freq[word] += 1
            else:
                word_freq[word] = 1


# Display the result
print(word_freq.items())
for w, f in word_freq.items():
    print(f"'{w}' has {f} number of occurrence")
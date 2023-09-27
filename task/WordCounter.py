# Write a program that takes a sentence as input and counts the occurrences of each word in the sentence. Print out a dictionary where the keys are the unique words and the values are the counts of their occurrences.

paragraph = input("Enter a paragraph of text: ")
words= paragraph.split()
len_word =len(words)
print(f"The occurrences of each word in the sentence is : {len_word}")
dic = {}
for word in words:
    lenw =len(word)
    dic [word]=lenw
print(dic)
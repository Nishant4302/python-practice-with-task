# Write a program that takes a paragraph of text as input. Count the number of words in the paragraph and calculate the average length of the words. Display both the word count and the average word length.
paragraph = input("Enter a paragraph of text: ")
words = paragraph.split()  
word_count = len(words)
print(f"Count the number of word is : {word_count}")
total_length = 0
for word in words:  
    total_length= total_length + len(word) 
average_length= total_length / len(words)
print('Average Length Per Word:', average_length, 'characters')



    


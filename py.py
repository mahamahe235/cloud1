import re
from collections import Counter 

#open the flie
with open('random_paragraphs','r') as file:
 text = file.read()
 text

#reading
 words = re.findall(r'\b\w+\b ', text.lower()) 
#define stop words
stop_words = set(["i", "me", "my", "myself", "we"
"our", "ours", "ourselves", "you", "your"
"the","and","or","but","to","of","a","an","in","on","for","with","as","by","at"])

#remove stop words
filtered_words = [word for word in words if word not in stop_words] 
filtered_words

#calculate the freq
word_freq = Counter(words)
word_freq

#display the word freq
for word ,freq in word_freq.items():
   print(word + ":" + str(freq))


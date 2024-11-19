# Mad Libs Generator

# open stories.txt in readmode
# Readmode = r, Writemode = w
with open("stories.txt", "r") as f:
    story = f.read()

# Using set instead of list for words
# becuz it will take unique word. Minimum the duplicate word
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# Loop then cut of this kind of <word> and add it to list words. 
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
        
print (words)

# Use dictionary for answers to replace the <word> to value
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

print(answers) 

# Replace the single word that user enter in the previous steps.
for word in words:
    story = story.replace(word, answers[word])
    
print(story)
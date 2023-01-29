# all code extracts below have been copied from the T38 task file.
# the code extracts have been run
# notes about what I found interesting have been added below

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word3.similarity(word3))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
	for token2 in tokens:
		print(token1.text, token2.text, token1.similarity(token2))

# =========== Compulsory Task 1 - part 1 =========== #
'''My notes about what I found interesting about the similarities
between cat, monkey and banana and think of an example of your own:
'''
'''It's interesting to see that the similarity index between cat and
cat or apple and apple is 1 (obviously because it's the same thing).
Cat and monkey has a high similarity index  because they are both animals. 
Apple and banana have high similarity index because they are both fruits. 
I found it interesting though that apple and banana (both fruits) 
have a higher similarity index than cat and banana (both animals).
Monkey and banana also had a high similarity index . This I believe
is because monkeys eat bananas. 
Apple and cat and apple and monkey had low similarity index. 
Interesting though to see that apple and monkey had a slightly higher similarity index
than cat and apple and cat and banana.'''

# ========== One Example of my own ========= #
tokens_example = nlp('doctor school hospital teacher')

for token_1 in tokens_example:
	for token_2 in tokens_example:
		print(token_1.text, token_2.text, token_1.similarity(token_2))

# ======= Notes from example of my own ======== #
'''It was interesting to see that school and teacher had the highest similarity of 0.65... 
I had excepted that this would be higher. Doctor and hospital also was not as high as I
expected. It only has a similarity index of 0.58. 
The lowest similarity index (teacher and hospital) was as I expected. '''

# code extracts copied as required from the T38 task file.
# the code extracts have been run

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
			 "Hello, there is my car",
			 "I\'ve lost my car in my car",
			 "I\'d like my boat back",
			 "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
	similarity = nlp(sentence).similarity(model_sentence)
	print(sentence + " - ", similarity)



# =========== Compulsory Task 1 - part 2 =========== #
''' My notes on what I notice is different from the model 'example file' 
run with the simpler language model ‘en_core_web_sm’ and then 'en_core_web_md. '''

'''When run on en_core_web_md, the complaints similarity index were all high
and had a significant similarity that ranged from about 0.75... to 1. The recipes 
similarity index were higher and had an even more significant similarity that ranged 
from 0.82.. to 1. When the recipe is compared with the complaints, the similarity 
index is lower and range from 0.52.. to 0.84...'''


'''When run on en_core_web_sm, I got a UserWarding that said: The model you're using has no word 
vectors loaded,  so the result of the Doc.similarity method will be based on the tagger, parser and 
NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, 
e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available.

However, the program still returned similarity indexes. The similarity index when run on en_core_web_sm were 
all lower when compared to when it was run on en_core_web_md. The complaints similarity index ranged from 
about 0.44... to 1. The recipe similarity index ranged from 0.58... to 1. when the recipe is compared with 
the complaints, the similarity index is even much lower and range from 0.13.. to 0.78.'''
# In this python game user has to enter substitutes for blanks in the story without knowing the story.
# The user has to enter specific words like a noun, adverb, verb, food, adjective, etc, according to the requirements. And then the story will be generated.

print("Welcome to madlibs. Please enter specific words (like: nouns, adverbs, verbs, food, etc..) according to the requirements, and the story will be generated.")

person = input("Enter a name of a person: ")
color = input("Enter a color: ")
food_stuff = input("Enter a food: ")
adjective = input("Enter an Adjective: ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
food1 = input("Enter a food: ")
food2 = input("Enter a food: ")


madlib = f"Today we picked apples from {person}'s Orchard. I had no idea there were so many different varieties of apples. I ate {color} apples straight of the tree that tasted like {food_stuff}. Then there was a {adjective} apple that looked like a {noun}. When our bags were full, we went on a free hay ride to {place} and back. It ended at a hay pile where we got to {verb} {adverb}. I can hardly wait to get home and cook with the apples. We are going to make apple {food1} and {food2} pies!"

print(madlib)
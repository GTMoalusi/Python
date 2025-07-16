# --- Advanced Mad Libs Game ---

#Introduction to the game

print("Welcome to the Advanced Mad Libs! Let's create an even sillier and more complex story.")
print("Please provide the following words to help us build our narrative:")
print("-" * 50)

#Prompt the user for different words and store them
#Adjectives
adjective_1 = input("Enter an adjective (e.g., 'sparkling', 'ancient'): ").strip()
adjective_2 = input("Enter an adjective (e.g., 'sleepy', 'vibrant'): ").strip()
adjective_3 = input("Enter an adjective (e.g., 'mysterious', 'fluffy'): ").strip()

#Nouns
noun_1 = input("Enter a singular noun (e.g., 'cat', 'mountain'): ").strip()
plural_noun = input("Enter a singular noun (e.g., 'shoes', 'clouds'): ").strip()
noun_2 = input("Enter a singular noun (e.g., 'treasure', 'robot'): ").strip()

#Verbs
verb_past_tense = input("Enter a singular noun (e.g., 'jumped', 'whispered'): ").strip()
verb_ing = input("Enter a verb ending in (-ng), (e.g., 'singing', 'flying'): ").strip()

#Adverb
adverb_1 = input("Enter an adverb (e.g., 'quickly', 'loudly'): ").strip()

print("-" * 50)

#Optional: Add simple validatio or default if input is empty.
#This makes the game more robust even if the user just presses enter.
if not adjective_1: adjective_1 = "shiny"
if not adjective_2: adjective_2 = "wobbly"
if not adjective_3: adjective_3 = "giant"
if not noun_1: noun_1 = "banana"
if not plural_noun: plural_noun = "unicorns"
if not noun_2: noun_2 = "spaceship"
if not verb_past_tense: verb_past_tense = "danced"
if not verb_ing: verb_ing = "giggling"
if not adverb_1: adverb_1 = "gracefully"

#Build the story with placeholder for user-provided words.
#Using an f-string for easy variable insertion.

story_parts = []

story_parts.append(f"One {adjective_1} morning, a {noun_1} {verb_past_tense} {adverb_1} through the enchanted forest.")
story_parts.append(f"It was on a quest to find the legendary {adjective_2} {noun_2}, guarded by {plural_noun}.")
story_parts.append(f"Suddenly, a {adjective_3} creature appeared, {verb_ing} a strange melody.")

#Conditional Touches (Bonus) - More advanced variations
#Condition based on the first noun

if noun_1.lower() == "dragon" or noun_1.lower() == "knight":
   story_parts.append("The forest trembled as our hero bravely faced the challenge ahead.")
elif noun_1.lower() == "squirrel" or noun_1.lower() == "mouse":
   story_parts.append("Despite its small size, the tiny adventurer was full of courage!")
else:
   story_parts.append("Our protagonist felt a mix of excitement and apprehension.")

#Condition based on the past tense verb
if verb_past_tense.lower() == "flew" or verb_past_tense.lower() == "soared":
   story_parts.append("It seemed to defy gravity with every movement.")
if verb_past_tense.lower() == "crawled" or verb_past_tense.lower() == "slithered":
   story_parts.append("Its journey was slow but determined, leaving a curious trail.")
else:
   story_parts.append("The action was unexpected and quite spectacular!")

story_parts.append(f"After a thrilling encounter, the {noun_1} finally reached the {noun_2}.")
story_parts.append(f"It was truly an unforgettable adventure!")

final_story = "\n".join(story_parts)

print(f"Here is your completed Advanced Mad Libs story: ")
print("-" * 50)

#Display the final story
print(final_story)
# --- Mad Libs Generator ---

#Introduction to the game

print("Welcome to Mad Libs! Let us create a silly story together.")
print("Please provide the words as prompted.")
print("-" * 30) #Separator for better readability

#1. Prompt the user for different words and store them.

adjective_1 = input("Enter an adjective (e.g., 'beautiful', 'sparkling'): ").strip()
adjective_2 = input("Enter another adjective (e.g., 'funny', 'gigantic'): ").strip()
adjective_3 = input("Enter one more adjective (e.g., 'majestic', 'tiny'): ").strip()
adjective_4 = input("Enter a final adjective (e.g., 'wild', 'calm'): ").strip()

#Optional Conditional Statement

if not adjective_1:
   adjective_1 = "lovely"
   print(f"No input for adjective_1, defaulting to '{adjective_1}'.")
if not adjective_2:
   adjective_2 = "silly"
   print(f"No input for adjective_2, defaulting to '{adjective_2}'.")
if not adjective_3:
   adjective_3 = "grand"
   print(f"No input for adjective_3, defaulting to '{adjective_3}'.")
if not adjective_4:
   adjective_4 = "amazing"
   print(f"No input for adjective_2, defaulting to '{adjective_4}'.")

print("-" * 30)

#2. Build the story with placeholders for user-provided words.
# Using the f-string for easy variable insertion.
 
story_template = f"""
On a beautiful {adjective_1} day, I went to the zoo.
I saw a funny {adjective_2} monkey swinging from the trees.
Then, I spotted a majestic {adjective_3} lion lounging in the sun.
"""

print("-" *30)

#3. Conditional touches (Bonus)
#Add some variation based on the first adjective.

if adjective_1.lower() == "sunny" or adjective_1.lower() == "bright":
   story_template += "The sun was shining brightly, making it a perfect day for an adventure!\n"
elif adjective_1.lower() == "rainy" or adjective_1.lower() == "gloomy":
   story_template += "Despite the drizzle, the animals seemed to be enjoying themselves\n"
else:
   story_template += "The weather was just right for exploring all the exhibits.\n"

story_template += f"What a wild and {adjective_4} experience!"

print("Here is your complete Mad Libs story:")
print("-" * 30)

#4. Display the final story
print(story_template)

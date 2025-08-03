# mad libs 
# user will give the input

# basic:
# Welcome message
print("******** Welcome to Mad Libs ********")
print("-----Your Crazy Abroad Adventure-----")
print("********------ Begins ------******** ")
print("1st give me some inputs dear!")

# Inputs
country = input("Enter a Country Name: ")
friend_name = input("Enter Your Friend's Name: ")  # New
plural_obj = input("Enter an Object in Plural: ")
clothing = input("Enter a Clothing Item: ")
transport = input("Enter a mode of Transport: ")
food = input("Enter a Food Item: ")
music_genre = input("Enter a Music genre: ")
landmark = input("Enter a famous landmark: ")
adjective = input("Enter an Adjective: ")
bizarre_food = input("Enter a Bizarre Food Item: ")  # Actually used now
drink = input("Enter a Drink: ")
container = input("Enter a Strange Container: ")
adjective2 = input("Enter an another Adjective: ")
costume = input("Enter a Costume Item in Plural: ")
random = input("Enter a Random Noun: ")
emotion = input("Enter an Emotion: ")
another_country = input("Enter another Country Name: ")

# Output
print("\nHere is your crazy abroad adventure:\n")
print(f"Last month, I went on a trip to {country} with my best friend {friend_name}. "
      f"We packed our {plural_obj}, put on our {clothing}, and hopped on a {transport}. "
      f"When we arrived, the air smelled like {food}, and people were dancing to {music_genre} in the streets. "
      f"Our hotel was right next to a {landmark}, which looked more {adjective} than I imagined. "
      f"On the second day, we accidentally ordered {bizarre_food} for lunch and drank {drink} served in a {container}. "
      f"At night, we went to a {adjective2} festival where people wore {costume} and sang songs about {random}. "
      f"It was the most {emotion} trip I've ever had, and I can't wait to visit {another_country} next year!")

import tkinter as tk

def generate_story():
    country = entry_country.get()
    friend = entry_friend.get()
    plural_obj = entry_plural_obj.get()
    clothing = entry_clothing.get()
    transport = entry_transport.get()
    food = entry_food.get()
    music = entry_music.get()
    landmark = entry_landmark.get()
    adjective = entry_adj.get()
    bizarre_food = entry_bizarre_food.get()
    drink = entry_drink.get()
    container = entry_container.get()
    adjective2 = entry_adj2.get()
    costume = entry_costume.get()
    random_noun = entry_random.get()
    emotion = entry_emotion.get()
    another_country = entry_another_country.get()

    story = f"Last month, I went on a trip to {country} with my best friend {friend}. " \
            f"We packed our {plural_obj}, put on our {clothing}, and hopped on a {transport}. " \
            f"When we arrived, the air smelled like {food}, and people were dancing to {music} in the streets. " \
            f"Our hotel was right next to a {landmark}, which looked more {adjective} than I imagined. " \
            f"On the second day, we accidentally ordered {bizarre_food} for lunch and drank {drink} served in a {container}. " \
            f"At night, we went to a {adjective2} festival where people wore {costume} and sang songs about {random_noun}. \n" \
            f"It was the most {emotion} trip I've ever had, and I can't wait to visit {another_country} next year!"

    # Create new window to display the story
    output_window = tk.Toplevel(root)
    output_window.title("Your Mad Libs Story")
    output_window.geometry("600x400")

    story_label = tk.Label(output_window, text="Here’s Your Story:", font=("Helvetica", 14, "bold"))
    story_label.pack(pady=10)

    story_text = tk.Text(output_window, wrap=tk.WORD, font=("Helvetica", 12))
    story_text.insert(tk.END, story)
    story_text.config(state='disabled')  # make the text box read-only
    story_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create main window
root = tk.Tk()
root.title("Mad Libs - Crazy Abroad Adventure")
root.geometry("600x700")

# Input labels and entry fields
labels = [
    "Country", "Friend's Name", "Plural Object", "Clothing", "Transport", "Food", "Music Genre",
    "Famous Landmark", "Adjective", "Bizarre Food", "Drink", "Container", "Another Adjective",
    "Costume Item (Plural)", "Random Noun", "Emotion", "Another Country"
]

entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Assign entries to variables
(entry_country, entry_friend, entry_plural_obj, entry_clothing, entry_transport, entry_food,
 entry_music, entry_landmark, entry_adj, entry_bizarre_food, entry_drink, entry_container,
 entry_adj2, entry_costume, entry_random, entry_emotion, entry_another_country) = entries

# Submit Button
submit_btn = tk.Button(root, text="Generate Story", command=generate_story, bg="lightblue")
submit_btn.grid(row=len(labels), columnspan=2, pady=10)

# Run the application
root.mainloop()

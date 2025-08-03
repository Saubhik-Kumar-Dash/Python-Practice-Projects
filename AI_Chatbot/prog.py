import pyautogui
import time
import pyperclip
import openai

openai.api_key = "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"  # Replace with your actual key
openai.api_base = "https://openrouter.ai/api/v1"

def is_last_message_from_target(chat_history, target_number="+91 90655 63116"):
    lines = chat_history.strip().split("/2025] ")[-1]
    if target_number in lines:
        return True
    return False
    # for line in reversed(lines):
    #     if line.startswith("[") and target_number in line:
    #         return True
    #     elif line.startswith("[") and "+91" in line:
    #         return False
    # return False  # If no valid message lines found

# Step 1: Click the icon to open or activate window
pyautogui.click(535, 330)

time.sleep(1)  # Wait for the window to activate

while True:

    # Step 2: Drag to select text
    pyautogui.moveTo(535, 250)
    pyautogui.mouseDown()
    pyautogui.moveTo(535, 955, duration=1.5)  # Smooth drag
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Step 3: Copy the selected text, then deselect
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for clipboard to update
    pyautogui.click(535, 250)

    # Step 4: Paste from clipboard to variable
    chat_history = pyperclip.paste()

    print("Copied Text:\n", chat_history)
    
    if is_last_message_from_target(chat_history):

        #AI response
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # You can change this to another free model
            messages=[
                {"role": "system", "content": "you are a saubhik who speaks different language. you are also a coder. You analyse the chats and then respond like saubhik. output should be next chat response as saubhik and don't sound robotic or formal, be casual"},
                {"role": "user", "content": chat_history}
                ]
        )
        output = response.choices[0].message.content
        pyperclip.copy(output)
            
        #     try:
        #         openai.api_key = "sk-..."  # your key here

        #         response = openai.ChatCompletion.create(
        #             model="gpt-3.5-turbo",
        #             messages=[
        #                 {"role": "system", "content": "You are Bhola, a virtual assistant..."},
        #                 {"role": "user", "content": command}
        #             ]
        #         )

        #         return response['choices'][0]['message']['content']


            # except Exception as e:      # specifically for API limit reached Errors
            #     print("❌ Error:", e)
            #     return "Sorry, I have reached my limit or encountered an error."

        # Step 5: Click at (732, 988) to focus input field
        pyautogui.click(732, 988)
        time.sleep(0.5)

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)

        # Step 7: Press Enter
        pyautogui.press('enter')
    
    else:
        break
import pyautogui
import time
import pyperclip
from openai import OpenAI


client = OpenAI(
  api_key="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"
)

def is_last_message_from_sender(chat_log, sender_name="Aryan"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

    # Step 1: Click on the icon
pyautogui.click(979, 746)
time.sleep(1)  # Wait for any response

while True:

    # Step 2: Click and drag to select text
    pyautogui.moveTo(974, 103)
    pyautogui.dragTo(1245, 696, duration=1, button='left')
    time.sleep(0.5)

    # Step 3: Copy selection to clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1333, 53)
    time.sleep(2)

    # Step 4: Get clipboard content into a variable
    chat_history = pyperclip.paste()

    print(chat_history)
    
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": "You are a person named Aryan who speaks hindi as well as english. You are from india and you are a coder. You analyse chat history and respond like Aryan . Output should be the next chat response (text message only)"},
            {"role": "user", "content": chat_history}
          ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click the target box
        pyautogui.click(1018, 753)
        time.sleep(1)

        # Step 6: Paste and press Enter
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')

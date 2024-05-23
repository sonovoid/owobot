import time
import pyautogui
import keyboard

# Counter for the number of times "owo b" has been typed
local_counter = 0

def failsafe_quit():
    if keyboard.is_pressed('q') == True:
        exit()
try:
    with open('counter.txt', 'r') as f:
            content = f.read().strip()
            if content.isdigit():
                total_counter = int(content)
            else:
                total_counter = 0
                print("owo b has not been typed before")

            print(f"owo b has been typed {total_counter} times")
except FileNotFoundError:
    total_counter = 0
    print("owo b has not been typed before")

# Wait 5 seconds before typing "owo b"
for i in range(5):
    print(f"Waiting {5-i} seconds before starting")
    failsafe_quit()
    time.sleep(1)

while True:
    # Type "owo b"
    pyautogui.typewrite("owo b")
    pyautogui.press('enter')
    
    # Increment the counter
    local_counter += 1
    print(f"owo b has been typed {local_counter} times")

    with open('counter.txt', 'w') as f:
        f.write(str(total_counter + local_counter))
    # If "owo b" has been typed 4 times, take a 5-second break
    if local_counter % 4 == 0:
        time.sleep(5)

    # Wait 15 seconds before typing "owo b" again
    for j in range(15):
        print(f"Waiting {15-j} seconds before typing 'owo b' again")
        failsafe_quit()
        time.sleep(1)
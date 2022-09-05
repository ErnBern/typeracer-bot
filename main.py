from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import keyboard, time

#Creates keybinds
def create_keybinds(change):
    if change != 0:
        with open("keybinds.txt", "r") as file:
            #Gets the keybinds for rewriting
            keybinds = file.readlines()
            start_keybind = keybinds[0].strip()
            stop_keybind = keybinds[1].strip()
            end_keybind = keybinds[2].strip()
            file.close()

    with open('keybinds.txt', 'w+') as file:
        if change == 0 or change == 1:
            start = input('Enter your keybind to start the bot:\n')
            if len(start) == 0 or len(start) > 2:
                print("Invalid Keybind!")
                create_keybinds(change)
            if change == 0: file.write(f"{start}\n")
            else:
                #Rewrites the binds
                file.write(f"{start}\n")
                file.write(f"{stop_keybind}\n")
                file.write(f"{end_keybind}\n")
        if change == 0 or change == 2:
            stop = input('Enter your keybind to stop the bot:\n')
            if len(stop) == 0 or len(stop) > 2:
                print("Invalid Keybind!")
                create_keybinds(change)
            if change == 0: file.write(f'{stop}\n')
            else:
                file.write(f"{start_keybind}\n")
                file.write(f"{stop}\n")
                file.write(f"{end_keybind}\n")
        if change == 0 or change == 3:
            end = input('Enter your keybind to end the bot:\n')
            if len(end) == 0 or len(end) > 2:
                print("Invalid Keybind!")
                create_keybinds(change)
            if change == 0: file.write(f'{end}\n')
            else:
                file.write(f"{start_keybind}\n")
                file.write(f"{stop_keybind}\n")
                file.write(f"{end}\n")
        file.close()

def keybind():
    #Creates the menu for changing the keybinds
    type = input("Enter the number to change your keybind!\nAll:0\nStart:1\nStop:2\nEnd:3\n")
    if not type.isdigit(): 
        print("Invalid Input")
        keybind()
    if int(type) > 3 or int(type) < 0: 
        print("Invalid Input")
        keybind()
    create_keybinds(int(type))

#Creates file if not exists
with open('keybinds.txt', 'a') as file:
    file.close()

with open ('keybinds.txt', 'r') as file:
    keybinds = file.readlines()
    if not keybinds:
        create_keybinds(0)
        keybinds = file.readlines()
    if keybinds:
        change = False
        while change == False:
            start = input("To change your keybinds enter change or to start type start:\n")
            if start.lower() == 'change': 
                keybind()
                with open('keybinds.txt', 'r') as file:
                    keybinds = file.readlines()
            elif start.lower() != 'start': print('Invalid Input')
            else: break
    #Sets the keybinds
    start_keybind = keybinds[0].strip()
    stop_keybind = keybinds[1].strip()
    end_keybind = keybinds[2].strip()


ser = Service('C:\Program Files (x86)\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://play.typeracer.com/")

loop = True
play = False

while loop == True:
    #Starts the bot
    if keyboard.is_pressed(start_keybind): play = True
    if play == True:
        #Gets the words
        src = driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        text = ""
        span = soup.findAll("span")
        for i in span:
            if "unselectable" in str(i):
                text += i.text
        wordInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
        wordInput.clear()
        for word in text:
            #A delay so the keys get registered
            time.sleep(0.045)
            wordInput.send_keys(word)
            #Stops the bot
            if keyboard.is_pressed(stop_keybind): break
            #Stops the program
            if keyboard.is_pressed(end_keybind):
                driver.close()
                exit()    
        play = False
    if keyboard.is_pressed(end_keybind):
        driver.close()
        exit()

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
import keyboard, time

#These two values determines the First Speed (Determines the lowest value while calculating for speed in x)
fastTestSpeed_rand1 = 0.01 # Lower is better
fastTestSpeed_rand2 = 0.01 # Make it same with rand1 if you want the fastest

#These two values determines the Second Speed (Determines the highest value while calculating for speed in x)
FastSlowSpeed_rand1 = 0.06 # Higher is slower
SlowestSpeed_rand2  = 0.1 # Make all the value the same if you want the maximum speed :)


#These two values should be lower and higher than the    other or same not the other way around
mistake_range_lower = 18    # Lower the value the higher your mistakes will be
mistake_range_higher = 22   # Higher the value the less your mistakes will be

username = 'dirtyfellow'
password = 'asdfasdf123'

#Xpaths
Sign_in = '//*[@id="userInfo"]/div/div[2]/div[2]/div[1]/a[2]'
username_xpath = '/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input'
password_xpath = '/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input'
Sign_in_btn = '/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button'


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
                #Updates the keybinds list
                with open('keybinds.txt', 'r') as file:
                    keybinds = file.readlines()
            elif start.lower() != 'start': print('Invalid Input')
            else: break
    #Sets the keybinds
    start_keybind = keybinds[0].strip()
    stop_keybind = keybinds[1].strip()
    end_keybind = keybinds[2].strip()

ser = Service(ChromeDriverManager().install())
options = ChromiumOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=ser, options=options)
action = ActionChains(driver)


def login():
    driver.find_element(By.XPATH,Sign_in).click()
    time.sleep(0.05)
    driver.find_element(By.XPATH, username_xpath).send_keys(username)
    time.sleep(0.05)
    driver.find_element(By.XPATH, password_xpath).send_keys(password)
    time.sleep(0.05)
    driver.find_element(By.XPATH,Sign_in_btn).click()

def random_nums():
    y = random.randint(6,leng_txt)
    return y

# Determines random from the above values
def get_random_f():
    f = random.uniform(fastTestSpeed_rand1,fastTestSpeed_rand2)
    return f

# Determines random from the above values
def get_random_g():
    g = random.uniform(FastSlowSpeed_rand1,SlowestSpeed_rand2)
    return g


driver.get("https://play.typeracer.com/")
sleep(2)
login()

loop = True
play = False
contain_mistakes = True
AutoRun = False

while loop == True:
    #Starts the bot
    if keyboard.is_pressed(start_keybind): play = True
    if play == True:
        #Gets the words
        src = driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        text = ''
        span = soup.findAll("span")
        for i in span:
            if "unselectable" in str(i):
                text += i.text
        try:
            wordInput = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
            wordInput.clear()
        except:
            play == False
        # print(text)
        if contain_mistakes == True:
            leng_txt = len(text) # space is also counted as charact/,/er
            rnd = random.randint(mistake_range_lower,mistake_range_higher)
            num_of_mistakes = random.randint(0,round(leng_txt/rnd))
            point_of_mistakes = []
            for _ in range(num_of_mistakes):
                if random_nums() in point_of_mistakes:
                    pass
                else:
                    point_of_mistakes.append(random_nums())
            store_keys = []
            # print(leng_txt)    
            # print(rnd)
            # print(num_of_mistakes)
            # print(point_of_mistakes)
        for index,word in enumerate(text, start=1):
            x = random.uniform(get_random_f(),get_random_g())
            txt_to_list = text.split(' ')
            store_keys.append(word)
            time.sleep(x)
            wordInput.send_keys(word)
            if contain_mistakes == True:
                prev_word_str = "".join(store_keys)
                prev_word_split = prev_word_str.split(' ')
                prev_word = prev_word_split[-1]
                len_of_prev_word = len(prev_word_split)
                current_word = txt_to_list[len_of_prev_word-1]
                try:
                    next_word = txt_to_list[len_of_prev_word]
                except:
                    next_word = current_word
                # print(f"Current word is {current_word}")
                # print(f"Prev word is {prev_word}")
                # print(f"Next Word is  {next_word}")
                # print(f"Prev word to str is {prev_word_str}")
                # print(f"leng of prev word is {len_of_prev_word}")
                # print(f"Txt to list {txt_to_list}")
                if index < 6:
                    continue
                for u in point_of_mistakes:
                    if index == u:
                        res = [x for x in prev_word + current_word if x not in prev_word or x not in current_word]
                        next_keys = []
                        for a in res:
                            next_keys.append(a)
                        y=random.randint(2,5)
                        g = []
                        for s in next_word:
                            g.append(s)
                        j= []
                        for d in current_word:
                            j.append(d)
                        h=0
                        for n in range(1,y):
                            if n <= 2:
                                try:
                                    next_key = next_keys[n+h]
                                except:
                                    try:
                                        next_key = g[0+h]
                                        h+=1
                                    except:
                                        next_key = j[-1-h]
                                        h-=1
                            try:
                                sleep(x)
                                wordInput.send_keys(next_key)
                            except:
                                sleep(x)
                                wordInput.send_keys(Keys.SPACE)
                        if n in range(3,4):
                            sleep(0.09)
                            wordInput.clear()
                            sleep(0.09)
                            for letters in prev_word:
                                sleep(x)
                                wordInput.send_keys(letters)
                        else:
                            for _ in range(1,y):
                                sleep(0.09)
                                wordInput.send_keys(Keys.BACKSPACE)
            if keyboard.is_pressed(stop_keybind): 
                continue
            #Stops the program
            if keyboard.is_pressed(end_keybind):
                driver.close()
                exit()
        play = False
    if keyboard.is_pressed(end_keybind):
        driver.close()
        exit()
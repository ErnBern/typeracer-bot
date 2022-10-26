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
from time import perf_counter, sleep
import random
import keyboard
import time

#These two values determines the First Speed (Determines the lowest value while calculating for speed in x)

#These two values should be lower and higher than the    other or same not the other way around
mistake_range_lower = 18    # Lower the value the higher your mistakes will be
mistake_range_higher = 22   # Higher the value the less your mistakes will be
while True:
    try:
        Speed = int(input('''
Remember this are all calculated using no mistakes!
0 :- Searching for hentai 400wpm+
1 :- Ultra Super Instinct 250wpm+
2 :- Super Instinct 200wpm+
3 :- Spiderman going to rescue 180wpm+
4 :- Fast 160wpm+
5 :- CHAD 140wpm+
6 :- Mediocre 120wpm+
7 :- Slow 100wpm+
8 :- Super Snail 80wpm+
9 :- Noob Snail 60wpm+
Enter your choice for typinh speed :- '''))
        if Speed >9 or Speed <0:
            print("\nInvalid Input")
            continue
    except:
        print("\nInvalid Input")
        continue
    else:
        break

while True:
    try:
        Mistakes = int(input('''
0 :- No mistakes
1 :- a very few mistakes
2 :- few mistakes
3 :- a little more mistakes
4 :- more mistakes
5 :- even more mistakes
6 :- Quite a lot of Mistakes
7 :- Alot of Mistakes
8 :- SOOO MANY MISTAKES I CAN"T TYPEEE AHHHH
Enter your choice for misatkes :- '''))
        if Mistakes >8 or Mistakes <0:
            print("\nInvalid Input")
            continue
    except:
        print("\nInvalid Input")
        continue
    else:
        break


if Speed == 0:
    fastTestSpeed_rand1 = 0.001
    fastTestSpeed_rand2 = 0.001
    FastSlowSpeed_rand1 = 0.001
    SlowestSpeed_rand2  = 0.001
elif Speed == 1:
    fastTestSpeed_rand1 = 0.005
    fastTestSpeed_rand2 = 0.01
    FastSlowSpeed_rand1 = 0.01
    SlowestSpeed_rand2  = 0.04
elif Speed == 2:
    fastTestSpeed_rand1 = 0.01
    fastTestSpeed_rand2 = 0.03
    FastSlowSpeed_rand1 = 0.03
    SlowestSpeed_rand2  = 0.06
elif Speed == 3:
    fastTestSpeed_rand1 = 0.01
    fastTestSpeed_rand2 = 0.04
    FastSlowSpeed_rand1 = 0.04
    SlowestSpeed_rand2  = 0.07
elif Speed == 4:
    fastTestSpeed_rand1 = 0.01
    fastTestSpeed_rand2 = 0.04
    FastSlowSpeed_rand1 = 0.05
    SlowestSpeed_rand2  = 0.08
elif Speed == 5:
    fastTestSpeed_rand1 = 0.03
    fastTestSpeed_rand2 = 0.06
    FastSlowSpeed_rand1 = 0.07
    SlowestSpeed_rand2  = 0.1
elif Speed == 6:
    fastTestSpeed_rand1 = 0.04
    fastTestSpeed_rand2 = 0.07
    FastSlowSpeed_rand1 = 0.07
    SlowestSpeed_rand2  = 0.11
elif Speed == 7:
    fastTestSpeed_rand1 = 0.05
    fastTestSpeed_rand2 = 0.08
    FastSlowSpeed_rand1 = 0.09
    SlowestSpeed_rand2  = 0.13
elif Speed == 8:
    fastTestSpeed_rand1 = 0.07
    fastTestSpeed_rand2 = 0.11
    FastSlowSpeed_rand1 = 0.12
    SlowestSpeed_rand2  = 0.18
elif Speed == 9:
    fastTestSpeed_rand1 = 0.08
    fastTestSpeed_rand2 = 0.14
    FastSlowSpeed_rand1 = 0.19
    SlowestSpeed_rand2  = 0.24


if Mistakes == 0:
    mistake_range_lower = 1000000
    mistake_range_higher = 1000000
    contain_mistakes = False
elif Mistakes == 1:
    mistake_range_lower =  100
    mistake_range_higher = 200
    contain_mistakes = True
elif Mistakes == 2:
    mistake_range_lower = 35
    mistake_range_higher = 40
    contain_mistakes = True
elif Mistakes == 3:
    mistake_range_lower = 26
    mistake_range_higher = 30
    contain_mistakes = True
elif Mistakes == 4:
    mistake_range_lower = 22
    mistake_range_higher = 26
    contain_mistakes = True
elif Mistakes == 5:
    mistake_range_lower =  16
    mistake_range_higher = 20
    contain_mistakes = True
elif Mistakes == 6:
    mistake_range_lower = 10
    mistake_range_higher = 14
    contain_mistakes = True
elif Mistakes == 7:
    mistake_range_lower = 5
    mistake_range_higher = 7
    contain_mistakes = True
elif Mistakes == 8:
    mistake_range_lower = 1
    mistake_range_higher = 1
    contain_mistakes = True

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

# def login():
#     driver.find_element(By.XPATH,Sign_in).click()
#     time.sleep(0.05)
#     driver.find_element(By.XPATH, username_xpath).send_keys(username)
#     time.sleep(0.05)
#     driver.find_element(By.XPATH, password_xpath).send_keys(password)
#     time.sleep(0.05)
#     driver.find_element(By.XPATH,Sign_in_btn).click()

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

loop = True
play = False
AutoRun = False

while loop == True:
    if keyboard.is_pressed(start_keybind): 
        play = True
    sleep(0.1)
    if play == True:
        #Gets the words
        driver.set_script_timeout(5)
        driver.set_page_load_timeout(5)
        src=driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        text = ''
        span = soup.findAll("span")
        for i in span:
            if "unselectable" in str(i):
                text += i.text
        wordInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
        wordInput.clear()
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
            time.sleep(x)
            wordInput.send_keys(word)
            if contain_mistakes == True:
                store_keys.append(word)
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
            if keyboard.is_pressed(stop_keybind): continue
            #Stops the program
            if keyboard.is_pressed(end_keybind):
                driver.close()
                exit()    
        play = False
    if keyboard.is_pressed(end_keybind):
        driver.close()
        exit()


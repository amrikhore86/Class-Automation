import time
time.sleep(0.2)
print("Loading Packages",end='')
time.sleep(0.75)
print('.',end='')
time.sleep(0.75)
print('.',end='')
time.sleep(0.75)
print('.',end='')

from os import read
import pyautogui,keyboard,mouse,win32api,win32con,cv2

time.sleep(0.25)
print("Starting Service...")
time.sleep(0.5)
print("Please read Readme.md before proceeding!")

#taking in login creds
def login_info():
    login_file=open("login.txt","w")
    time.sleep(0.25)
    sid=input("Enter your Student ID: ")
    
    if len(sid)==8:
        login_file.write(sid+'\n')
        time.sleep(0.25)
        password=input("Enter your password for the website: ")
        login_file.write(password)
        login_file.close()
            
    else:
        print("Invalid length for Student ID. Must Be of 8 characters")
        

#checking if login.txt is empty or not and then calling function login_info   
with open('login.txt', 'r') as f:
  x = f.read()
  y = len(x)
  if y==0:
      login_info()
      print('Successfully Added to Login.txt')
      
#time.sleep(3)
while True:
    print('Looking for available browsers on Desktop')
    if pyautogui.locateOnScreen('chrome.png',confidence=0.9, grayscale=True) !=None:
         print("Chrome Found!")
         pyautogui.moveTo(pyautogui.locateOnScreen('chrome.png', confidence=0.9,grayscale=True))
         print("Launching Chrome...")
         pyautogui.doubleClick()
         break
    elif pyautogui.locateOnScreen('firefox.png', confidence=0.9,grayscale=True) !=None:
         print("Firefox Found!")
         pyautogui.moveTo(pyautogui.locateOnScreen('firefox.png', confidence=0.9,grayscale=True))
         print("Launching Firefox...")
         pyautogui.doubleClick()
         break
            
time.sleep(0.3)   
         
while True:
    if pyautogui.locateOnScreen('refresh.png',confidence=0.7, grayscale=True) !=None:
        keyboard.press_and_release('ctrl+E')
        break

time.sleep(0.3)
print("Visiting Live Class Portal")
keyboard.press('backspace')
time.sleep(0.3)
keyboard.press('backspace')
keyboard.write("http://aessmart.in/kps")
keyboard.press('enter')

login_file=open('login.txt','r')
creds=login_file.readlines()
str(creds).split()
creds[0]=creds[0][0:8]
        
while True:
    if pyautogui.locateOnScreen('signin.png',confidence=0.2, grayscale=True) !=None:
        print("Filling in Login Credentials")
        print("Student ID : " ,creds[0])
        print("Password : ", end='')
        #pass_len=(len(creds[1]*))*'*'
        time.sleep(2)
        keyboard.write(creds[0])
        time.sleep(1)
        time.sleep(1)
        keyboard.press('\t')
        time.sleep(1)
        keyboard.write(creds[1])
        time.sleep(1)
        keyboard.press('enter')
        print("Logged IN Successfully. If not, run the Debugger.")
        break

while True:
    if pyautogui.locateOnScreen('live_class.png',confidence=0.6, grayscale=True) !=None:
        pyautogui.moveTo(pyautogui.locateOnScreen('live_class.png', confidence=0.9,grayscale=True))
        pyautogui.click()
        break
        
sub=['PHY.png','CHEM.png','MATHS.png','ENG.png','COMP.SC.png']
        
def joining():
    while True:
        if pyautogui.locateOnScreen(sub[0] or sub[1] or sub[2] or sub[3] or sub[4] or sub[5],confidence=0.8, grayscale=False) !=None:
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('view_class.png', confidence=0.9,grayscale=True)))
            if pyautogui.locateOnScreen('mute.png', confidence=0.6, grayscale=True) !=None:
                pyautogui.click(pyautogui.moveTo('mute.png'))
                pyautogui.click(pyautogui.moveTo('no_cam.png', confidence=0.6,grayscale=True))
                pyautogui.click(pyautogui.moveTo('join.png'))
                keyboard.press_and_release('ctrl+tab')
                
                break
            
while True:
    joining()
    time.wait(16200)
    break
            

        


        


    

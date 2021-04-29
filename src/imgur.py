import requests
import os
import random
import ctypes
import threading

if not os.path.exists('Images'): os.makedirs('Images') # Makes Folder Called Images
lock = threading.Lock()
Valid = 0
Invalid = 0

def Clear(): # Simple Clear Console Function
    os.system('cls')

def UpdateTitle(): # Update The Title
    ctypes.windll.kernel32.SetConsoleTitleW("[imgur scraper] by armful#0001 | Valid: %s | Invalid: %s" % (Valid, Invalid))
    
def Bruteforce(imgtype):
    global Valid, Invalid
    rndm = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcbnm123456789') for i in range(7))
    link = f'https://i.imgur.com/{rndm}.{imgtype}'
    img = requests.get(link, allow_redirects=True)
    if img.url == "https://i.imgur.com/removed.png":
        lock.acquire()
        print('                        [\u001b[31mINVALID\u001b[37m] i.imgur.com/%s.%s' % (rndm, imgtype))
        Invalid += 1
        UpdateTitle()
        lock.release()
    else:
        lock.acquire()
        with open(f'images/{rndm}.{imgtype}', 'wb') as f: f.write(img.content)
        print('                        [\u001b[32mVALID\u001b[37m] i.imgur.com/%s.%s' % (rndm, imgtype))
        Valid += 1
        UpdateTitle()
        lock.release()

if __name__ == "__main__":
    Clear()
    ctypes.windll.kernel32.SetConsoleTitleW("[imgur scraper] by armful#0001")
    print(
        '\n                         \u001b[37m██████╗ \u001b[36m██╗  ██╗\u001b[37m██████╗ ███████╗███████╗',
        '\n                        \u001b[37m██╔═████╗\u001b[36m╚██╗██╔╝\u001b[37m╚════██╗██╔════╝██╔════╝',
        '\n                        \u001b[37m██║██╔██║ \u001b[36m╚███╔╝ \u001b[37m █████╔╝███████╗█████╗  ',
        '\n                        \u001b[37m████╔╝██║ \u001b[36m██╔██╗ \u001b[37m██╔═══╝ ╚════██║██╔══╝  ',
        '\n                        \u001b[37m╚██████╔╝\u001b[36m██╔╝ ██╗\u001b[37m███████╗███████║███████╗',
        '\n                         \u001b[37m╚═════╝ \u001b[36m╚═╝  ╚═╝\u001b[37m╚══════╝╚══════╝╚══════╝\n',
        '\n                       \u001b[37m imgur scraper by \u001b[36marmful#0001\u001b[37m\n',
        '\n                        [\u001b[36m1\u001b[37m] brute-force \u001b[36mPNG\u001b[37m extensions',
        '\n                        [\u001b[36m2\u001b[37m] brute-force \u001b[36mJPEG\u001b[37m extensions',
        '\n                        [\u001b[36m3\u001b[37m] brute-force \u001b[36mWEBP\u001b[37m extensions',
        '\n                        [\u001b[36m4\u001b[37m] brute-force \u001b[36mGIF\u001b[37m extensions',
        '\n                        [\u001b[36m5\u001b[37m] brute-force \u001b[36mCUSTOM\u001b[37m extensions',
    )
    imgtype = input(
        '\n                        \u001b[37m┌─[root@\u001b[36m0x25E\u001b[37m]\n                        └───\u001b[36m$ \u001b[37m'
        )
    if "1" in imgtype:
        Type = 'png'
    elif "2" in imgtype:   
        Type = 'jpeg'
    elif "3" in imgtype:      
        Type = 'webp' 
    elif "4" in imgtype:     
        Type = 'gif'
    elif "5" in imgtype:      
        Type = input('\n                        \u001b[37m┌─[root@\u001b[36m0x25E\u001b[37m]\n                        └───\u001b[36m$ \u001b[37m') 
    else:
        print(
        '                         ┌─[root@\u001b[36m0x25E\u001b[37m]\n',
        '                        └───\u001b[31m$ \u001b[37mInvalid Option'
        )
        os.system('pause >NUL')    
    print()
    while True:
        for i in range(100):
            threads = threading.Thread(target=Bruteforce, args=(Type,))    
            threads.start()

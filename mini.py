import os,time,platform
os.system('clear')
print('\n\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m Checking Updates..........\n')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print("\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Your Device \033[1;91m64\033[1;92m Bit Supported This Tool Enjoy.....")
    os.system ("xdg-open https://www.facebook.com/mr.rohman.129")
    time.sleep(2)
    import MINI64
elif bit=='32bit':
    print("\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Your Device \033[1;91m32\033[1;92m Bit Supported this Tool Enjoy.....")
    os.system ("xdg-open https://www.facebook.com/mr.rohman.129")
    time.sleep(2)
    import MINI32
else:
    print('\033[1;31m[\033[1;92m×\033[1;91m] No Internet Connection !!!!!')

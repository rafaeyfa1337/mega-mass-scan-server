import requests, sys, os
from colorama import Fore, Style
from platform import system
if system() == 'Linux':
    os.system('clear')
else:
    os.system('cls')
print(f"""{Fore.YELLOW}
    __  ___                 __  ___                _____                
   /  |/  /__  ____ _____ _/  |/  /___ ___________/ ___/___  ______   __
  / /|_/ / _ \/ __ `/ __ `/ /|_/ / __ `/ ___/ ___/\__ \/ _ \/ ___/ | / /
 / /  / /  __/ /_/ / /_/ / /  / / /_/ (__  |__  )___/ /  __/ /   | |/ / 
/_/  /_/\___/\__, /\__,_/_/  /_/\__,_/____/____//____/\___/_/    |___/  
            /____/ {Fore.WHITE} (c) Rafaeyfa1337 | Mass Scan Server (Apache, Litespeed etc)
""")
targetnya = input("Website list: ")
def main():
    with open(targetnya, 'r') as f, open('result_server.txt', 'w') as output:
        for line in f.readlines():
            url = line.strip('\n')
            try:
                r = requests.get('http://' + url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=8)
                print(f"{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] " + r.url + f" | {Fore.GREEN}" + r.headers['Server'] + f"{Fore.WHITE}")
                output.write(r.url + ' | ' + r.headers['Server'] + '\n')
            except:
                pass
            try:
                r = requests.get('https://' + url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=8)
                print(f"{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] " + r.url + f" | {Fore.GREEN}" + r.headers['Server'] + f"{Fore.WHITE}")
                output.write(r.url + ' | ' + r.headers['Server'] + '\n')
            except:
                pass
if __name__ == '__main__':
    main()
print('Manteppp! Semua web server telah berhasil di scan dan disimpan di file result_server.txt')
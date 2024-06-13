from colorama import Fore, Style, init

init(autoreset=True)

ASCII_LOGO = """
   ______ _      _        ______  _____ 
  |___  /| |    (_)       | ___ \\|  ___|
     / / | |__   _  _ __  | |_/ /| |__  
    / /  | '_ \\ | || '_ \\ | ___ \\|  __| 
  ./ /___| | | || || | | || |_/ /| |___ 
  \\_____/|_| |_||_||_| |_|\\____/ \\____/ 
                                         
"""

def display_logo():
    colors = [Fore.BLUE, Fore.MAGENTA]
    for i, line in enumerate(ASCII_LOGO.splitlines()):
        color = colors[i % len(colors)]
        print(f'{color}{line}{Style.RESET_ALL}')

def display_app_info(version, author):
    print(f'{Fore.CYAN}App Version: {version}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}Author: {author}{Style.RESET_ALL}')

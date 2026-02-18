import subprocess
import platform
import os
import time
from colorama import init, Fore

init(autoreset=True)
# YOU CAN ADJUST IF IS NOT GOOD FOR YOU 
TOR_WINDOWS_PATH = r"C:\Tor Browser\Browser\start-tor-browser.exe"
TOR_LINUX_PATH = "/usr/bin/torbrowser-launcher"



def get_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80


def center_block(text):
    return text.center(get_width())


def separator():
    print(Fore.WHITE + "═" * get_width())


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")



def print_banner():
    banner_lines = [
        "╔══════════════════════════════════════╗",
        "║                                      ║",
        "║         TOR AUTO LAUNCHER            ║",
        "║                                      ║",
        "║              BY C404C                ║",
        "║                                      ║",
        "╚══════════════════════════════════════╝"
    ]

    print()
    separator()
    print(Fore.MAGENTA + center_block(""))
    for line in banner_lines:
        print(Fore.MAGENTA + center_block(line))
    print(Fore.MAGENTA + center_block(""))
    separator()
    print()



sites = {
    1: {"name": "Vortex Market", "url": "https://vortexshopctlmqxyymj5fd73766kujn67audfvtxtsr7f5srduikdad.onion/login"},
    2: {"name": "   AwaZone   ", "url": "http://awazonevlc63543fjvtli35bk2iopdyyaaytkmmiop5avny6b24uljqd.onion/auth/login"},
    3: {"name": "  CIA Portal ", "url": "http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/"},
    4: {"name": "    Riseup   ", "url": "http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion/"},
    5: {"name": "    Oxacab   ", "url": "http://wmj5kiic7b6kjplpbvwadnht2nh2qnkbnqtcv3dyvpqtz7ssbssftxid.onion:44203/"},
    6: {"name": " Pirate Bay  ", "url": "http://piratebayo3klnzokct3wt5yyxb2vpebbuyjl7m623iaxmqhsd52coid.onion/"},
    7: {"name": "Not available", "url": "http://example7.onion"},
    8: {"name": "Not available", "url": "http://example8.onion"},
    9: {"name": "Not available", "url": "http://example9.onion"},
    10: {"name": "Not available", "url": "http://example10.onion"},
}



def detect_tor():
    print(Fore.CYAN + center_block("[INFO] Detecting operating system..."))
    time.sleep(1)

    system = platform.system()
    print(Fore.CYAN + center_block(f"[INFO] OS detected: {system}"))
    print()

    if system == "Windows" and os.path.exists(TOR_WINDOWS_PATH):
        return TOR_WINDOWS_PATH

    if system == "Linux" and os.path.exists(TOR_LINUX_PATH):
        return TOR_LINUX_PATH

    return None



while True:
    clear_screen()
    print_banner()

    print(Fore.YELLOW + center_block("AVAILABLE SITES"))
    separator()

    for key, data in sites.items():
        print(Fore.RED + center_block(f"[{key}]  →  {data['name']}"))

    separator()
    print(Fore.WHITE + center_block("[0]  →  Quit"))
    separator()

    print()
    print(Fore.GREEN + center_block("[INPUT] Select a site → "), end="")
    choice = input()

    if not choice.isdigit():
        print(Fore.RED + center_block("[ERROR] Invalid input."))
        time.sleep(2)
        continue

    choice = int(choice)

    if choice == 0:
        print(Fore.YELLOW + center_block("[INFO] Exiting program..."))
        time.sleep(1)
        break

    selected = sites.get(choice)

    if not selected:
        print(Fore.RED + center_block("[ERROR] Invalid option."))
        time.sleep(2)
        continue

    print()
    print(Fore.CYAN + center_block("[INFO] Checking Tor installation..."))
    time.sleep(1)

    tor_path = detect_tor()

    if not tor_path:
        print(Fore.RED + center_block("[ERROR] Tor Browser not found."))
        time.sleep(2)
        continue

    
    print(Fore.CYAN + center_block("[INFO] Launching Tor Browser..."))
    time.sleep(2)

    subprocess.Popen([tor_path])

    print()
    print(Fore.YELLOW + center_block('[ACTION REQUIRED] Click on "Connect" inside Tor Browser.'))
    print(Fore.YELLOW + center_block("Waiting for Tor connection..."))
    time.sleep(8)

    clear_screen()
    print_banner()

    print(Fore.CYAN + center_block("[INFO] Tor should now be connected."))
    print()
    print(Fore.GREEN + center_block("COPY-PASTE THIS URL INTO TOR BROWSER:"))
    print()
    print(Fore.RED + center_block(selected["url"]))
    print()

    input(Fore.WHITE + center_block("Press ENTER to return to menu..."))

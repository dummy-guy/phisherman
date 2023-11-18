import time

# ANSI color escape codes
cyan = '\033[0;36m'
magenta = '\033[0;35m'
reset = '\033[0m'
yellow = '\033[1;33m'
green = '\033[0;32m'
light_blue = '\033[1;34m'

def type_text(text):
    delay = 0.03
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_template(index, name):
    print(f"{yellow}[{reset}{index}{yellow}]{reset} {name}")
    
def index_str(number):
  indexed_str=str(number).zfill(2) 
  return indexed_str

def check_installed(command):
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False
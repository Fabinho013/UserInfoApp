from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_info():
    user_info = request.json
    ip_address = request.remote_addr  # Obtém o IP do usuário // # Gets the user's IP
    user_info['ip'] = ip_address

    # Cria uma pasta para armazenar informações do usuário
    # Creates a folder to store user information
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    folder_name = f'user_info_{timestamp}'
    os.makedirs(folder_name, exist_ok=True)

    # Arquivo
    # File
    filename = os.path.join(folder_name, 'info.txt')

    # Informações do usuário para um arquivo
    # User information to a file
    with open(filename, 'a') as file:
        for key, value in user_info.items():
            file.write(f"{key}: {value}\n")

    print(user_info)  # informações no console // # information in the console
    return jsonify({'status': 'success', 'data': user_info})

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)

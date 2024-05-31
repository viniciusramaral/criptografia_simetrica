import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configurações do cliente
host = '127.0.0.1'
port = 65432

# Chave de criptografia (deve ser secreta e compartilhada entre o cliente e o servidor)
key = b'0M1PHHKq4wqjq1EC'  # AES requer uma chave de 16, 24 ou 32 bytes letras e números apenas

#Função para criptografar a mensagem
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ct_bytes

#Função para descriptografar a mensagem
def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# Configuração do socket do cliente
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        while True:
            try:
                message = input("Digite a mensagem para enviar: ")
                if message.lower() == 'exit':
                    break
                encrypted_message = encrypt_message(message, key)
                s.sendall(encrypted_message)
                
                data = s.recv(1024)
                decrypted_response = decrypt_message(data, key)
                print(f"Resposta do servidor: {decrypted_response}")
            except (ValueError, KeyError) as e:
                print(f"Erro ao criptografar/descriptografar a mensagem: {e}")
                break
except socket.error as e:
    print(f"Erro de socket: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")

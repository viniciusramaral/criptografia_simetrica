import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configurações do servidor
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

#Configuração do socket do servidor
#Utilizamos o socket por recomendação nas instruções do trabalho.
#Poderíamos fazer também em forma de API utilizando Flask
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Servidor ouvindo em {host}:{port}...")

        while True:
            conn, addr = s.accept()
            print(f"Conectado por {addr}")

            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            print(f"Conexão encerrada por {addr}")
                            break
                        decrypted_message = decrypt_message(data, key)
                        print(f"Mensagem recebida: {decrypted_message}")
                        response = f"Mensagem recebida: {decrypted_message}"
                        encrypted_response = encrypt_message(response, key)
                        conn.sendall(encrypted_response)
                    except (ValueError, KeyError) as e:
                        print(f"Erro ao descriptografar a mensagem: {e}")
                        break
                    except socket.error as e:
                        print(f"Erro de socket durante a comunicação: {e}")
                        break
except socket.error as e:
    print(f"Erro de socket: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")

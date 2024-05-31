Criptografia ponta a ponta para envio e recebimento de dados.

Como utilizar:
git clone https://github.com/viniciusramaral/criptografia_simetrica/

Criar um ambiente virtual
python -m venv venv

Instalar os pacotes do requirements
pip install -r requirements.txt

Executar o arquivo server.py
python server.py
O sistema abrirá uma porta de escuta atuando como um servidor 

Executar o client.py
python client.py
O sistema irá abrir um prompt para envio de mensagens

Importante:
Em ambos os arquivos há uma variável chamada key
Ela é responsável por armazenar a chave criptográfica das funções.
Cada ponta deve ter a sua chave, e caso não tenham, o sistema não é capaz de interpretar a mensagem recebdida.

import socket

HOST = 'localhost'
PORTA = 50000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORTA))    #vinculando o socket ao endereço
s.listen()              #habilitando o servidor a receber conexão

print("Aguardando conexão de um cliente")

conn, end = s.accept()  #aceitando uma conexão

print("Conectado em :", end)

while True:
     data = conn.recv(1024) #recebendo mensagem do cliente
     msg = data.decode()    #decodificanco mensagem do cliente
     print('Mensagem recebida do cliente: ', msg)
     
     if msg != 'fim':       #mensagem diferente de 'fim' o servidor digita uma resposta ao cliente
            mensagem = input('Digite uma mensagem: ')
            conn.send(mensagem.encode())
     else:                  #caso a mensagem seja igual a 'fim' o servidor é encerrado e envia uma mensagem de 'Fim' para o cliente
        print('Conexão encerrada')
        conn.send(str.encode('Fim'))
        conn.close
        break
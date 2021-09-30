import socket
import dana as dana_app

def dana_program():
    print("Server Starting")
    host = socket.gethostname()
    port = 5000 

    server_socket = socket.socket()
    server_socket.bind((host, port))

    print("Waiting for connection")
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data_receive = conn.recv(1024).decode()

        data = data_receive.split(";")

        if not data_receive:
            print("Client tixid", str(address), "telah logout")
            break
        else:
            if data[0] == "check_balance":
                try:
                    response = str(dana_app.check_dana_balance(data[1]))
                    conn.send(response.encode())
                except:
                    response = "failed"
                    conn.send(response.encode())
            elif data[0] == "check_user":
                try:
                    result = dana_app.check_user(data[1])
                    if result == 1:
                        response = "exist"
                    else:
                        response = "empty"
                    
                    conn.send(response.encode())
                except:
                    response = "failed"
                    conn.send(response.encode())
            elif (data[0] == "cashback") or (data[0] == "return"):
                try:
                    dana_app.increase_dana_balance(data[1], int(data[3]))
                    dana_app.decrease_dana_balance(data[2], int(data[3]))
                    response = str(dana_app.check_dana_balance(data[1]))
                    conn.send(response.encode())
                except:
                    response = "failed"
                    conn.send(response.encode())
            elif data[0] == "transaction":
                try:
                    saldo = dana_app.check_dana_balance(data[1])

                    if saldo > int(data[3]):
                        dana_app.decrease_dana_balance(data[1], int(data[3]))
                        dana_app.increase_dana_balance(data[2], int(data[3]))
                        response = str(dana_app.check_dana_balance(data[1]))
                    else:
                        response = "mines"
                    conn.send(response.encode())
                except:
                    response = "failed"
                    conn.send(response.encode())
            else:
                print("Perintah tidak dikenali!")

    conn.close()

if __name__ == '__main__':
	dana_program()
	
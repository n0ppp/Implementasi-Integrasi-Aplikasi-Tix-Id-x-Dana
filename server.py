# Library yang digunakan untuk melakukan komunikasi antar program dengan menggunakan socket

import socket

# Melakukan import program dana.py untuk diintegrasikan dengan program tixid.py

import dana as dana_app

# Fungsi utama untuk server
def server_program():
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
        print(data)

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

                    if saldo >= int(data[2]):
                        dana_app.decrease_dana_balance(data[1], int(data[2]))
                        response = str(dana_app.check_dana_balance(data[1]))
                    else:
                        response = "mines"
                    conn.send(response.encode())
                except:
                    print("TRANSACTION FAILED\n")
                    response = "failed"
                    conn.send(response.encode())
            elif data[0] == "topup":
                try:
                    nominal = int(data[2])

                    if nominal > 0:
                        dana_app.increase_dana_balance(data[1], int(data[2]))
                        response = str(dana_app.check_dana_balance(data[1]))
                    else:
                        response = "mines"
                    conn.send(response.encode())
                except:
                    print("TOP UP FAILED\n")
                    response = "failed"
                    conn.send(response.encode())
            elif data[0] == 'history':
                try:
                    hasil = dana_app.check_history(data[1], data[2])
                    print(f"HASIL: {hasil}\n")
                    response = f"{hasil}"
                    conn.send(response.encode())
                except:
                    print("HISTORY FAILED\n")
                    response = "failed"
                    conn.send(response.encode())
            else:
                print("Perintah tidak dikenali!")

    conn.close()

# fungsi main yang digunakan untuk menampilkan menu yang digunakan untuk mengeksekusi program server
if __name__ == '__main__':
	while True:
		command = input("\n[PILIH MENU]\n1. Nyalakan Server\n2. Matikan Server\n\nMenu -> ")
		if command == "1" :
			server_program()
		elif command == "2":
			break
		else:
			print("command tidak ditemukan")
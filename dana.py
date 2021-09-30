'''
1. Saldo waktu awal daftar dihilangin
2. Tambah tabel history transaksi (+ waktu topup, - waktu transaksi)
'''


import socket
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ais_dana"
)

mycursor = mydb.cursor()

def check_user(nohp):
    try:
        sql = "SELECT * FROM user WHERE telepon = %s"
        val = (nohp, )
        mycursor.execute(sql, val)

        result = mycursor.fetchall()

        if len(result) == 1:
            print("\n[CEK AKUN]\nAkun dengan No HP", nohp,"tersedia")
            return(1)
        else:
            print("\n[CEK AKUN]\nAkun dengan No HP", nohp,"tidak tersedia")
            return(0)
    except:
        print("Gagal mendapatkan informasi akun", nohp)

def new_dana_user(nohp, nama, saldo):
    try:
        sql = "INSERT INTO user (telepon, nama, saldo) VALUES (%s, %s, %s)"
        val = (nohp, nama, saldo)
        mycursor.execute(sql, val)

        mydb.commit()
        print("\n[PENDAFTARAN BERHASIL]\nBerhasil mendaftarkan user", nama, "\nSaldo saat ini = Rp.", saldo, "\n")
    except:
        print("Gagal mendaftarkan user baru\n")

def check_dana_balance(nohp):
    try:
        sql = "SELECT * FROM user WHERE telepon = %s"
        val = (nohp, )
        mycursor.execute(sql, val)

        result = mycursor.fetchone()
        print("\n[CEK SALDO]\nSaldo", result[1],"saat ini = Rp.", result[2])

        return(result[2])
    except:
        print("Gagal mendapatkan informasi akun", nohp)

def increase_dana_balance(nohp, nominal):
    try:
        sql = "UPDATE user SET saldo = saldo + %s WHERE telepon = %s"
        val = (nominal, nohp)
        mycursor.execute(sql, val)

        mydb.commit()
        print("\n[TAMBAH SALDO]\nBerhasil menambah saldo sebesar", nominal, "pada user", nohp)
    except:
        print("Gagal menambah saldo pada user", nohp)

def decrease_dana_balance(nohp, nominal):
    try:
        saldo = check_dana_balance(nohp)
        if saldo > nominal:
            sql = "UPDATE user SET saldo = saldo - %s WHERE telepon = %s"
            val = (nominal, nohp)
            mycursor.execute(sql, val)    

            mydb.commit()
            print("\n[KURANGI SALDO]\nBerhasil mengurangi saldo sebesar", nominal, "pada user", nohp)
        else:
            print("\n[GAGAL KURANGI SALDO]\nSaldo", nohp, "Kurang!")
    except:
        print("Gagal mengurangi saldo pada user", nohp)

def dana_program():
    host = socket.gethostname()
    port = 5000 

    server_socket = socket.socket()
    server_socket.bind((host, port))

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
                    response = str(check_dana_balance(data[1]))
                    conn.send(response.encode())
                except:
                    response = "failed"
                    conn.send(response.encode())
            elif data[0] == "check_user":
                try:
                    result = check_user(data[1])
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
                    increase_dana_balance(data[1], int(data[3]))
                    decrease_dana_balance(data[2], int(data[3]))
                    response = str(check_dana_balance(data[1]))
                    conn.send(response.encode())
                except:
                    response = "failed"
                    conn.send(response.encode())
            elif data[0] == "transaction":
                try:
                    saldo = check_dana_balance(data[1])

                    if saldo > int(data[3]):
                        decrease_dana_balance(data[1], int(data[3]))
                        increase_dana_balance(data[2], int(data[3]))
                        response = str(check_dana_balance(data[1]))
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
    while True:
        reg_status = input("Apakah Anda ingin menambahkan user baru? [y/n] ")
        if reg_status == "n":
            break
        else:
            try:
                print("[DAFTAR USER BARU]\n")
                new_name = input("Nama -> ")
                new_nohp = input("No HP -> ")
                new_saldo = int(input("Saldo -> "))

                new_dana_user(new_nohp, new_name, new_saldo)
            except:
                print("Format Salah!\n")

    dana_program()
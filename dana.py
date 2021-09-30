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

def new_dana_user(nohp, nama):
    try:
        sql = "INSERT INTO user (telepon, nama, saldo) VALUES (%s, %s, 0)"
        val = (nohp, nama)
        mycursor.execute(sql, val)

        mydb.commit()
        print("\n[PENDAFTARAN BERHASIL]\nBerhasil mendaftarkan user", nama)
    except:
        print("\nGagal mendaftarkan user baru\n")

def check_dana_balance(nohp):
    try:
        sql = "SELECT * FROM user WHERE telepon = %s"
        val = (nohp, )
        mycursor.execute(sql, val)

        result = mycursor.fetchone()
        print("\n[CEK SALDO]\nSaldo", result[1],"saat ini = Rp.", result[2])

        return(result[2])
    except:
        print("\nGagal mendapatkan informasi akun", nohp)

def increase_dana_balance(nohp, nominal):
    try:
        sql = "UPDATE user SET saldo = saldo + %s WHERE telepon = %s"
        val = (nominal, nohp)
        mycursor.execute(sql, val)

        sql = "INSERT INTO history (telepon, nominal, keterangan) VALUES (%s, %s,'Top Up Saldo')"
        val = (nohp, nominal)
        mycursor.execute(sql, val)

        mydb.commit()
        print("\n[TAMBAH SALDO]\nBerhasil menambah saldo sebesar", nominal, "pada user", nohp)
    except:
        print("\nGagal menambah saldo pada user", nohp)

def decrease_dana_balance(nohp, nominal):
    try:
        saldo = check_dana_balance(nohp)
        if saldo >= nominal:
            sql = "UPDATE user SET saldo = saldo - %s WHERE telepon = %s"
            val = (nominal, nohp)
            mycursor.execute(sql, val)  

            sql = "INSERT INTO history (telepon, nominal, keterangan) VALUES (%s, %s,'Pembayaran')"
            val = (nohp, nominal)
            mycursor.execute(sql, val)  

            mydb.commit()
            print("\n[Pembayaran Berhasil]\nBerhasil melakukan Pembayaran sebesar", nominal, "pada user", nohp)

            saldo = check_dana_balance(nohp)
        else:
            print("\n[Pembayaran Gagal]\nSaldo anda tidak mencukupi")
    except:
        print("\nGagal melakukan pembayaran pada user", nohp)

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
        command = input("[PILIH MENU]\n1. Daftar akun dana\n2. Top Up Saldo\n3. Pembayaran\n4. Nyalakan Server untuk TixID\n5. Exit\n\nMenu -> ")
        if command == "1":
            try:
                print("[DAFTAR USER BARU]\n")
                new_name = input("Nama -> ")
                new_nohp = input("No HP -> ")
                # new_saldo = int(input("Saldo -> "))

                new_dana_user(new_nohp, new_name)
            except:
                print("Format Salah!\n")
        elif command == "2":
            try:
                nohp = input("No HP -> ")
                print("Masukkan Nominal Saldo\n")
                add_saldo = int(input("Saldo -> "))

                increase_dana_balance(nohp, add_saldo)
            except:
                print("Format Salah!\n")
        elif command == "3":
            dana_program()
        elif command == "4":
            try:
                nohp = input("No HP -> ")
                print("Masukkan Nominal Pembayaran\n")
                add_saldo = int(input("Saldo -> "))

                decrease_dana_balance(nohp, add_saldo)
            except:
                print("Format Salah!\n")
        elif command == "5":
            break
        else:
            print("Opsi tidak tersedia\n")

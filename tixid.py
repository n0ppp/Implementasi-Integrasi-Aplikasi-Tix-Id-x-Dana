'''
1. Tambah tabel bioskop (id, nama, harga)
2. Tambah tabel film (id, nama)
3. Tambah tabel jadwal (film, bioskop, )
'''


import socket
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ais_tixid"
)

mycursor = mydb.cursor()

client_socket = socket.socket()

host = socket.gethostname()
port = 5000

tixid_id = "123"

user_id = None
user_name = None
user_status = 2

def daftar_tix_id(nohp, nama):
    try:
        sql = "INSERT INTO user (telepon, nama) VALUES (%s, %s)"
        val = (nohp, nama)
        mycursor.execute(sql, val)

        mydb.commit()
        print("[PENDAFTARAN BERHASIL]\nBerhasil mendaftarkan user", nama, "\n")
    except:
        print("Gagal mendaftarkan user baru\n")

def tixid_login():
    try:
        global user_id, user_name, user_status
        print("[LOGIN USER TIX ID]")
        log_id = input("No HP -> ")
        
        sql = "SELECT * FROM user WHERE telepon = %s"
        val = (log_id, )
        mycursor.execute(sql, val)

        result = mycursor.fetchone()
        user_id = result[0]
        user_name = result[1]
        user_status = result[2]
        print("\n[LOGIN BERHASIL]\n")
    except:
        print("\n[LOGIN GAGAL]\n")

def activate_dana():
    try:
        message = "check_user;" + user_id + ";;"
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()

        if response == "empty":
            print("Gagal aktivasi dana\nTidak akun dengan nomor tersebut!")
        elif response == "exist":
            sql = "UPDATE user SET dana_status = 1 WHERE telepon = %s"
            val = (user_id, )
            mycursor.execute(sql, val)

            mydb.commit()
            global user_status
            user_status = 1
            print("Berhasil mengaktifkan dana pada akun\n", user_name)
        else:
            print("Gagal mengaktifkan dana pada akun\n", user_name)
    except:
        print("Gagal mengaktifkan dana pada akun\n", user_name)

def logout():
    global user_id, user_name, user_status

    user_id = None
    user_name = None
    user_status = 2

    client_socket.close()


def tixid_program():

    while True:
        command = input("[PILIH MENU]\n1. Cek Saldo\n2. Pesan Tiket Bioskop\n3. Batal Transaksi\n4. Cashback\n5. Exit\n\nMenu -> ")
        
        if command == "1":
            message = "check_balance;" + user_id + ";;"
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[CEK SALDO]\nBerhasil cek saldo")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "2":
            sql = "SELECT namaFilm FROM film"
            mycursor.execute(sql)
            print("Data Film: ")
            result = mycursor.fetchall()
            for num,i in enumerate(result):
                print(str(num+1)+". "+i[0])
            
            pilihFilm = input("Pilih Film dengan memasukkan Nomor Film -> ")
            nominal = input("Jumlah Tiket (1 Tiket Rp 25.000) -> ")
            pilihFilm = result[int(pilihFilm)-1][0]
            message = "transaction;" + user_id + ";" + tixid_id + ";" + nominal +";"+pilihFilm
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            elif response == "mines":
                print("Saldo dana tidak cukup!\n")
            else:
                print("\n[TRANSAKSI SUKSES]\nBerhasil Berhasil memproses transaksi")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "3":
            nominal = input("Nominal return transaksi -> ")

            message = "return;" + user_id + ";" + tixid_id + ";" + nominal
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[RETURN TRANSAKSI]\nBerhasil mereturn transaksi")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "4":
            nominal = input("Nominal cashback -> ")

            message = "cashback;" + user_id + ";" + tixid_id + ";" + nominal
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[CASHBACK]\nBerhasil memproses cashback")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "5":
            logout()
            break
        else:
            print("Maaf, perintah tidak dikenali\n")


if __name__ == '__main__':
    while True:
        reg_status = input("Apakah Anda ingin menambahkan user baru? [y/n] ")
        if reg_status == "n":
            break
        else:
            try:
                print("[DAFTAR USER BARU]\n")
                nama_daftar = input("Nama -> ")
                hp_daftar = input("No HP -> ")

                daftar_tix_id(hp_daftar, nama_daftar)
            except:
                print("Format Salah!\n")

    client_socket.connect((host, port))
    tixid_login()

    if user_status == 1:
        tixid_program()
    elif user_status == 0:
        try:
            activate_dana()
            if user_status == 1:
                tixid_program()
            else:
                logout()
        except:
            logout()
    else:
        logout()
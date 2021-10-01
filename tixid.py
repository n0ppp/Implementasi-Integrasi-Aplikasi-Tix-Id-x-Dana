'''
1. Tambah tabel bioskop (id, nama, harga)
2. Tambah tabel film (id, nama)
3. Tambah tabel jadwal (film, bioskop, jadwal(dd/mm/yy) )
4. Tambah menu top up
5. Tambah menu history
'''

# Library yang digunakan untuk melakukan komunikasi antar program dengan menggunakan socket

import socket

# Library yang digunakan agar program python dapat menggunakan database mysql

import mysql.connector

# Melakukan koneksi ke database ais_tixid
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ais_tixid"
)

# mysql cursor untuk melakukan eksekusi statement yang berkomunikasi dengan mysql database
mycursor = mydb.cursor()

# inisialisasi socket untuk client
client_socket = socket.socket()

# konfigurasi host dan port yang akan digunakan
host = socket.gethostname()
port = 5000

# deklarasi variable global
user_id = None
user_name = None
user_status = 2

# fungsi untuk mendaftarkan akun baru pada tixid
def daftar_tix_id(nohp, nama):
    try:
        sql = "INSERT INTO user (telepon, nama) VALUES (%s, %s)"
        val = (nohp, nama)
        mycursor.execute(sql, val)

        mydb.commit()
        print("[PENDAFTARAN BERHASIL]\nBerhasil mendaftarkan user", nama, "\n")
    except:
        print("Gagal mendaftarkan user baru\n")

# fungsi untuk login ke akun tixid
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

# fungsi untuk mengaktifkan akun dana pada akun tixid
def activate_dana():
    try:
        message = f"check_user;{user_id};;"
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

# fungsi untuk menampilkan list bioskop
def list_bioskop():
    try:
        print("[LIST BIOSKOP TIX ID]")
        
        sql = "SELECT * FROM bioskop"
        mycursor.execute(sql)

        result = mycursor.fetchone()
        print(result)
    except:
        print("\n[LIST BIOSKOP GAGAL]\n")

def list_tiket():
    pass

# fungsi logout akun tixid
def logout():
    global user_id, user_name, user_status

    user_id = None
    user_name = None
    user_status = 2

    client_socket.close()

# menu program tixid
def tixid_program():

    while True:
        command = input("[PILIH MENU]\n1. Cek Saldo\n2. Pesan Tiket Bioskop\n3. Top Up\n4. Cashback\n5. History\n\nMenu -> ")
        
        if command == "1":
            # message = "check_balance;" + user_id + ";;"
            message = f"check_balance;{user_id}"
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[CEK SALDO]\nBerhasil cek saldo")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "2":
            sql = "SELECT film.judul, tiket.tanggal, bioskop.nama_bioskop, bioskop.harga FROM tiket LEFT JOIN bioskop ON tiket.id_bioskop=bioskop.id_bioskop LEFT JOIN film on tiket.id_film=film.id_film"
            mycursor.execute(sql)
            print("Data Film: \nNo.\tJudul\tTanggal\tBioskop\tHarga")
            result = mycursor.fetchall()

            for num, i in enumerate(result):
                print(f"{num+1}. {i[3]}\t{i[1]}\t{i[2]}\t{i[0]}")

            pilihFilm = int(input("Pilih Film dengan memasukkan Nomor Film -> "))
            nominal = int(input("Jumlah Tiket -> "))
            bayar = result[pilihFilm-1][3]*nominal
            message = f"transaction;{user_id};{bayar}"
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
            nominal = input("Nominal Top-Up -> ")

            message = f"topup;{user_id};{nominal}"
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[TOP UP SUKSES]\nBerhasil Top-Up!")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "4":
            nominal = input("Nominal cashback -> ")

            message = f"cashback;{user_id};;{nominal}"
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()

            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[CASHBACK]\nBerhasil memproses cashback")
                print("Saldo", user_name, "saat ini adalah", response, "\n")
        elif command == "5":
            tanggal = input("Masukkan tanggal (sampai)-> ")

            message = f"history;{user_id};{tanggal}"
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print(type(response))
            response = eval(response)
            
            if response == "failed":
                print("dana sedang error!")
            else:
                print("\n[HISTORY TRANSAKSI]\nBerhasil mereturn history transaksi")
                print(response)
        elif command == "6":
            logout()
            break
        else:
            print("Maaf, perintah tidak dikenali\n")

# fungsi main yang dieksekusi pertama kali saat program tixid berjalan
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
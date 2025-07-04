import os
import time

def tampilkan_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗████████╗██╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██║████╗  ██║╚══██╔══╝╚██╗ ██╔╝
██████╔╝██║   ██║██╔████╔██║██║██╔██╗ ██║   ██║    ╚████╔╝ 
██╔═══╝ ██║   ██║██║╚██╔╝██║██║██║╚██╗██║   ██║     ╚██╔╝  
██║     ╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║   ██║      ██║   
╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝      ╚═╝   
    ''')

def tampilkan_kelompok():
    print("📋  KELOMPOK PENDAFTARAN SISWA")
    print("-" * 40)
    anggota = [
        "1. Rizky Nurpujiansyah",
        "2. Sabrina Rohimatus Sa'diyah",
        "3. Saidati Nur Rahmatilah",
        "4. Salma Kamila Insani",
        "5. Salsa Pariha",
        "6. Yayu"
    ]
    for anggota_kelompok in anggota:
        print(f"👤 {anggota_kelompok}")
    print("-" * 40)
    time.sleep(1)

def input_data_siswa():
    print("\n📝  FORM PENDAFTARAN SISWA")
    nama = input("Nama Lengkap             : ")
    nisn = input("NISN                     : ")
    tempat_lahir = input("Tempat Lahir             : ")
    tanggal_lahir = input("Tanggal Lahir (dd-mm-yyyy): ")
    nama_ayah = input("Nama Ayah                : ")
    nama_ibu = input("Nama Ibu                 : ")
    alamat = input("Alamat                   : ")
    no_telepon = input("Nomor Telepon            : ")

    data_siswa = {
        "Nama": nama,
        "NISN": nisn,
        "Tempat, Tanggal Lahir": f"{tempat_lahir}, {tanggal_lahir}",
        "Nama Ayah": nama_ayah,
        "Nama Ibu": nama_ibu,
        "Alamat": alamat,
        "Nomor Telepon": no_telepon
    }

    return data_siswa

def tampilkan_data(data):
    print("\n✅ DATA SISWA TEREGISTRASI")
    print("-" * 40)
    for key, value in data.items():
        print(f"{key:25}: {value}")
    print("-" * 40)

# Eksekusi Program
tampilkan_logo()
tampilkan_kelompok()
data = input_data_siswa()
tampilkan_data(data)


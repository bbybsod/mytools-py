#package
import datetime as dt
import os 
import pyfiglet as pg
from colorama import Fore,Style
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

text = pg.figlet_format('RASYA')
#akun
'''System'''
os.system('clear')
#information
def header():
    print(f"{Fore.LIGHTGREEN_EX}{'SELAMAT DATANG':^40}")
    print(f"{'DI SERVER':^40}")
    print(40*'-')
    print(f"{'Created by : Muhammad Rasya':^40}")
    print(f"{'Instagram : @rassyyaa_a':^40}")
    print(f"{'Github : github.com/bbybsod':^40}")
          
def time():
    print(40*'-')
    data_waktu = dt.datetime.now()
    print(f"{'INFORMATION':^40}")
    print(f"Year : {data_waktu.year}")
    print(f"Month : {data_waktu.month}")
    print(f"date : {data_waktu.day}")
    print(f"day : {data_waktu.strftime('%A')}")
    print(40*'-')

header()
time()
pengguna = input('masukan nama anda : ')

os.system('clear')
os.system('cls')

header()
time()
print(f"SELAMAT DATANG {pengguna.upper()}")

def menu():
    print('MENU')
    print('1.DATABASE ')
    print('2.REKENING')
    print('3.SPIDER LINK')
    print('4.KALKULATOR')
    print('\n')
    global command 
    command = input(f'{pengguna}@server :')
menu()

os.system('clear')
os.system('cls')
#menampilan database
akun1 = {
    'nama' : "Admin",
    'password' : "admin123"
}
akun2 = {
    'nama': "administrator",
    'password': "password123@"
}
akun3 = {
    'nama':"lfsg@001",
    'password':'123887'
}
akun4 = {
    'nama':"admin@proton.me",
    'password': 'admin233'
}

akun5 = {
    'nama': 'admin31@gmail.id',
    'password' : 'admin_aja'
}

#database akun
dataakun = {
    "00167":akun1,
    "09912":akun2,
    "00124":akun3,
    "07235":akun4,
    "97274":akun5
}
if command == "1":
    print(f"{Fore.RED} {'DATABASE SERVER':^40}")
    print('\n')
    print(f"{'KEY':15} {'NAMA':<15} {'PASSWORD':<10}")
    print(40*'-')
    for account in dataakun:
        KEY = account

        NAMA = dataakun[KEY]['nama']
        PASSWORD = dataakun[KEY]['password']
        print(f"{KEY:15} {NAMA:<15} {PASSWORD:<10}")
    print(40*'-')

elif command == "2":
    header()
    time()
    print(40*'-')
    print(f"Hi {pengguna.upper()}")
    pemasukan = int(input('masukan jumlah pemasukan anda Rp'))
    pengeluaran = int(input('masukan jumlah pengeluaran anda Rp'))
    print(f'saldo anda adalah Rp{pemasukan - pengeluaran}')

elif command == "3":
    header()
    time()
    def get_links(url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            links = set()
            for tag in soup.find_all("a", href=True ):
                full_url = urljoin(url, tag['href'])
                links.add(full_url)

            return links
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return set()
    
    def extract_params(links):
        params = set()
        for link in links:
            parsed = urlparse(link)
            if parsed.query:
                params.add(link)

        return params
    
    if __name__ == "__main__":
        target_url = input('masukan URL target : ')
        found_links = get_links(target_url)
        param_links = extract_params(found_links)

        print("\n [+] Ditemukan Link :")
        for link in found_links:
            print(link)

        print("\n [+] Ditemukan Link dengan Parameter: ")
        for link in param_links:
            print(link)

    def check_link(url):
        try:
            response = requests.get(url, timeout=5)
            print(f"[+] {url} --> {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"[-] {url} --> tidak bisa di akses")

        
    print("\n[+] Scan Status HTTP Link:")
    for link in found_links:
        check_link(link)

elif command == "4":
    header()
    time()
    def pertambahan(angka1,angka2):
        hasil = angka1+angka2
        return hasil
    def perkalian(angka1,angka2):
        hasil = angka1 * angka2
    chose = input("Masukan operasi penjumlahan [+ - / x]")
    if chose == "+":
        angka1 = int(input("masukan angka pertama : "))
        angka2 = int(input("masukan angka kedua : "))
        print(f" hasil dari {angka1} + {angka2} = {pertambahan(angka1,angka2)}")
    else:
        print('silahkan pilih operator yang benar!')


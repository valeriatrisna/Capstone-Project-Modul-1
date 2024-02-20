#trisna's capstone project

import re

MasterData = [
    {'Code': 'TR342', 'Nama': 'Trisna', 'Nomor': '081529361342',
     'email': 'valey.trisna@gmail.com', 'Jenis Kelamin': 'Wanita', 'Domisili': 'Jakarta'},
    {'Code': 'RE409', 'Nama': 'Reza', 'Nomor': '085792420409',
     'email': 'rezadwi05@gmail.com', 'Jenis Kelamin': 'Pria', 'Domisili': 'Badung'},
    {'Code': 'YU313', 'Nama': 'Yuanita', 'Nomor': '081237072313', 'email': '-','Jenis Kelamin': 'Wanita', 
     'Domisili': 'Karangasem'},
    {'Code': 'DW321', 'Nama': 'Dwi', 'Nomor': '08987654321', 'email': 'dwi.ganteng@gmai.com','Jenis Kelamin': 'Pria', 
     'Domisili': 'Badung'},
    {'Code': 'GR678', 'Nama': 'Gregorius', 'Nomor': '08712345678', 'email': 'greg-orius@gmail.com','Jenis Kelamin': 'Pria', 
     'Domisili': 'Denpasar'},
     {'Code': 'VA532', 'Nama': 'Valeria', 'Nomor': '08521276532', 'email': 'valeria.yunita@gmail.com','Jenis Kelamin': 'Wanita', 
     'Domisili': 'Denpasar'},
      {'Code': 'AU234', 'Nama': 'Aurelia', 'Nomor': '0897667234', 'email': 'aurelia556@ymail.com','Jenis Kelamin': 'Wanita', 
     'Domisili': 'Singaraja'},
      {'Code': 'FE221', 'Nama': 'Felicia', 'Nomor': '089776223221', 'email': '','Jenis Kelamin': 'Wanita', 
     'Domisili': 'Denpasar'},
      {'Code': 'RI223', 'Nama': 'Richard', 'Nomor': '087221225223', 'email': 'richard-tampan@gmail.com','Jenis Kelamin': 'Pria', 
     'Domisili': 'Badung'},
      {'Code': 'CO988', 'Nama': 'Cornelius', 'Nomor': '085623777988', 'email': 'cornell123@gmail.com','Jenis Kelamin': 'Pria', 
     'Domisili': 'Karangasem'},
      {'Code': 'RO231', 'Nama': 'Romanus', 'Nomor': '082221987231', 'email': 'roman.us@yahoo.com','Jenis Kelamin': 'Pria', 
     'Domisili': 'Karangasem'}
]

User = {
    'Lina': 'US010',
    'Ahmad': 'US015',
    'Mira': 'US017'}

from tabulate import tabulate

#FUNCTION READ DATA 
#function mencetak data dengan menggunakan input (data)
def read_data(data):
    print(tabulate(data, headers='keys', tablefmt='pretty'))

# FUNCITON CREATE DATA
#function untuk menambahkan data baru, dengan menggunakan input (data & user)
def create_data(data,user):
    while True:
        while True:
            namaBaru = input('Masukkan Nama Lengkap:').title()
            if namaBaru.isalpha():
                break
            else:
                print('Nama hanya mengandung abjad!')
        while True:
            NomorBaru = input('Masukkan Nomor: ')
            if re.fullmatch(r'\b\d{5,}', NomorBaru):
                break
            else:
                print('Nomor hanya mengandung angka min 5 digit!')
        while True:       
            EmailBaru = input('Masukkan Email: ')
            if re.fullmatch(r'\b\w+[\w\.-]*@\w+\-?\w*\.\w+\b',EmailBaru) or EmailBaru in ['-','']:
                break
            else:
                print('Masukkan format Email yang benar atau Enter apabila tidak ada!')
        while True: 
            JKBaru = input('Masukkan Jenis Kelamin Pria/ Wanita: ').title()
            if JKBaru in ('Pria', 'Wanita'):
                break
            else:
                print('Pilih Pria atau Wanita!')
        while True:
            DomisiliBaru = input('Masukkan Kota Domisili: ')
            if DomisiliBaru.isalpha() :
                break
            else:
                print('Domisili hanya mengandung abjad!')
        CodeBaru = str((namaBaru[:2].upper()))+str(NomorBaru[-3:])
        ListAppend = {'Code': CodeBaru ,
            'Nama': namaBaru,
            'Nomor': NomorBaru,
            'email': EmailBaru,
            'Jenis Kelamin' : JKBaru,
            'Domisili': DomisiliBaru}
        while True:
            val = input( f'Apakah anda yakin menambahkan data Nama : {namaBaru}, Code : {CodeBaru}, Nomor : {NomorBaru}, email : {EmailBaru}, Jenis Kelamin : {JKBaru}, Domisili : {DomisiliBaru} Y/N? ').title()
            try:
                if val == 'Y':
                    data.append(ListAppend)
                    read_data(data)
                    print('Data berhasil ditambahkan!')
                elif val == 'N':
                    print("Terima kasih")
                    return
                else:
                    print('Masukkan Y atau N.')
                break
            except:
                print('Inputan kamu salah')
        while True:
            choice = input('Apakah Anda ingin menambahkan data lain? (Y/N)').capitalize()
            if choice == 'Y':
                break
            elif choice == 'N':
                print('Terima kasih')
                return menupegawai2(data,user)
            else:
                print('Pilih Y atau N!')
                
# FUNCTION UPDATE/REPLACE DATA 
#function untuk mengupdate data dengan input (data & user), update data berdasarkan Code Unik dari tabel
def replace_data(data,user):
    read_data(data)
    lst = []
    while True:
        print('Silahkan masukkan data yang ingin ganti')
        ganti = input('Masukkan Code dari Data yang ingin Anda ganti: ').upper()
        if re.fullmatch(r'\b\w{5}',ganti):
            for i in data:
                lst.append(i['Code'])
            if ganti in lst:
                while True:
                    NamaGanti = input('Masukkan Nama: ')
                    if NamaGanti.isalpha():
                        break
                    else:
                       print('Nama hanya mengandung abjad!') 
                while True:
                    NomorGanti = input('Masukkan Nomor: ')
                    if re.fullmatch(r'\b\d{5,}', NomorGanti):
                        break    
                    else:
                        print('Nomor hanya mengandung angka min 5 digit!')
                while True:
                    EmailGanti = input('Masukkan Email: ')
                    if re.fullmatch(r'\b\w+[\w\.-]*@\w+\-?\w*\.\w+\b', EmailGanti)or EmailGanti in ['-','']:
                        break
                    else:
                        print('Masukkan format Email yang benar atau Enter apabila tidak ada!')
                while True: 
                    JKGanti = input('Masukkan Jenis Kelamin Pria/Wanita: ').title()
                    if JKGanti in ('Pria', 'Wanita'):
                        break
                    else:
                        print('Pilih Pria atau Wanita!')
                while True:
                    DomisiliGanti = input('Masukkan Kota Domisili: ').title()
                    if DomisiliGanti.isalpha() :
                        break
                    else: 
                        print('Domisili hanya mengandung abjad!')
                CodeGanti = str(NamaGanti[0:2].upper())+str(NomorGanti[-3:])
                while True:
                    confirmation1 = input(f'Apakah anda yakin mengganti data Code : {ganti} menjadi Nama : {NamaGanti}, Code : {CodeGanti}, Nomor : {NomorGanti}, email : {EmailGanti}, Jenis Kelamin : {JKGanti}, Domisili : {DomisiliGanti} Y/N ? ').title()
                    try:
                        if confirmation1 == 'Y':
                            for dict1 in data:
                                if ganti == dict1['Code']:
                                    dict1['Nama'] = NamaGanti
                                    dict1['Nomor'] = NomorGanti
                                    dict1['Code'] = CodeGanti
                                    dict1['email'] = EmailGanti
                                    dict1['Jenis Kelamin'] = JKGanti
                                    dict1['Domisili'] = DomisiliGanti
                                    read_data(data) 
                                    print('Data berhasil diubah!')    
                        elif confirmation1 == 'N':
                            print("Terima kasih")
                            return()
                        else:
                            print('Masukkan Y atau N.')
                        break
                    except:
                        print('Inputan kamu salah')
                    break
            else:
                print('Code yang Anda masukkan tidak terdaftar!')
            while True:
                choice = input('Apakah Anda ingin mengganti data lain? (Y/N)').capitalize()
                if choice == 'Y':
                    break
                elif choice == 'N':
                    print('Terima kasih')
                    return menupegawai2(data,user)
                else:
                    print('Pilih Y atau N!')
                
#FUNCTION DELETE DATA
# function untuk menghapus salah satu dictionary, dengan input (data & user), hapus data menggunakan Code Unik
deleted_data = []
def delete_data(data,user):
    read_data(data)
    while True:
        lst = [i['Code'] for i in data]
        code = input('Masukkan Code data yang ingin Anda hapus: ').upper()
        if code in lst:
            for dict1 in data:
                if dict1['Code'] == code:
                    confirmation2 = input(f'Apakah Anda yakin menghapus data {dict1}? (Y/N)').capitalize()
                    if confirmation2 == 'Y':
                        data.remove(dict1)
                        deleted_data.append(dict1)
                        read_data(data)
                        print('Data telah terhapus!')
                    elif confirmation2 == 'N':
                        print('Terima kasih')
                    else:
                        print('Masukkan Y atau N!')
        else:
            print('Code yang Anda masukkan tidak terdaftar!')
        while True:
            choice = input('Apakah Anda ingin menghapus data lain? (Y/N)').capitalize()
            if choice == 'Y':
                break
            elif choice == 'N':
                print('Terima kasih')
                return menupegawai2(data,user)
            else:
                print('Pilih Y atau N!')

#FUNCTION CALL BACK DELETED DATA
#function untuk mengembalikan kembali data yang telah terhapus dengan menggunakan input (data & dictionary dalam list dari data yang terhapus (deleted_data))
def callback_data(data, deleted_data):
    data.extend(deleted_data)
    read_data(data)
    deleted_data.clear()

#FUNCTION SEARCH DATA
#function untuk mencari dictionary dengan menggunakan input (data)
def search_data(data):
    cari = input('Masukkan Data yang Anda Cari: ')
    list_cari = []
    if re.fullmatch(r'\b\w+[\w\.-]*@\w+\-?\w*\.\w+\b',cari) or cari in ['-','']:
        cari
    else:
        cari = cari.title()
    try:
        for dict1 in data:
            for key in dict1:
                if dict1[key] == cari:
                    list_cari.append(dict1)
        read_data(list_cari)
    except:
        print('Data tidak ditemukan!')

            
#FUNCTION MENU FILTER DAYA BY
#function menampilkan menu filter data by pilihan Jenis Kelamin atau Domisili dengan menggunakan input (data)
def filter_data(data):
    while True:
        print('''Silahkan masukan filter yang akan Anda gunakan:
            1. Jenis Kelamin
            2. Domisili
            3. Kembali ke menu sebelumnya
            ''')
        opsi = input('Masukkan pilihan Anda: ')
        if opsi == '3':
            return
        elif opsi in ['1','2']:
            if opsi == '1':
                JenisKelamin = input('Masukkan Filter Pria/Wanita: ').title()
                key = 'Jenis Kelamin'
                value = JenisKelamin
                filter_dict(data,key,value)
            elif opsi == '2':
                Domisili = input('Masukkan Filter Domisili: ').title()
                key = 'Domisili'
                value = Domisili
                filter_dict(data,key,value)
        else:
            print('Masukkan pilihan 1 sd 2 atau 3 untuk kembali ke menu sebelumnya!')

#FUNCTION FILTER DATA
#function melakukan filter data (lanjutan function dari filter_data(data)) dengan menggunakan input (data, key, & value)
def filter_dict(data, key, value):
    filtered_list = []
    while True:
        try:
            for item in data: 
                if item.get(key) == value:
                    filtered_list.append(item)
            return read_data(filtered_list)
        except: 
            print('Data yang Anda masukkan tidak terdaftar!')

            
# FUNCTION MENU READ DATA BY 
#function menampilkan menu penyajian data dengan pilihan tampilkan data semua, tampilkan data dengan berurutan abjad, & data terfilter dengan menggunakan input (data)
def menu_read_data(data):
    while True:
        print('''Silahkan pilih bentuk data yang ingin ditampilkan:
              1. Tampilkan semua data
              2. Sort Data
              3. Filter Data
              4. Kembali ke menu sebelumnya
              ''')
        opsi = input('Masukkan pilihan Anda: ')
        if opsi == '4':
            return
        elif opsi in ['1','2','3']:
            try:
                if opsi =='1':
                    read_data(data)
                elif opsi =='2':
                    sort_data(data)
                elif opsi =='3':
                    filter_data(data)
            except:
                print('Masukkan pilihan 1 sd 3!')
        else:
            print('Masukkan pilihan 1 sd 3 atau 4 untuk kembali ke menu sebelumnya!')

# FUNCTION SORT DATA
#function untuk mengurutkan data dengan abjad dengan beberapa pilihan code, nama, nomor, email, jenis kelamin, domisili dengan menggunakan input (data)
def sort_data(data):
    while True:
        print('''Pilih urutkan berdasarkan abjad:
            1. Code
            2. Nama
            3. Nomor
            4. Email
            5. Jenis Kelamin
            6. Domisili
            7. Kembali ke menu sebelumnya''')
        sort = input('Masukkan pilihan Anda: ')
        if sort == '7':
            break
        elif sort in ['1','2','3','4','5','6']:
            try:
                if sort == '1':
                    data = sorted(data, key = lambda x : x['Code'])
                elif sort == '2':
                    data = sorted(data, key = lambda x : x['Nama'])
                elif sort == '3':
                    data = sorted(data, key = lambda x : x['Nomor'])
                elif sort == '4':
                    data = sorted(data, key = lambda x : x['email'])
                elif sort == '5':
                    data = sorted(data, key = lambda x : x['Jenis Kelamin'])   
                elif sort == '6':
                    data = sorted(data, key = lambda x : x['Domisili'])
                read_data(data)
            except:
                print('Masukkan pilihan 1 sd 6!')
        else:
            print('Masukkan pilihan 1 sd 6 atau 7 untuk kembali ke menu sebelumnya!')

# FUNCTION MENU LOGIN EMPLOYEE       
#function untuk login sebagai employee
def menulogin(data):
    user = input('Masukkan User Anda: ').strip()
    password = input('Masukkan Pass Anda: ').strip()
    if user in User and password == User[user]:
        print('Login berhasil!')
        menupegawai2(data,user)
    else:
        print('User atau password Anda salah!')

# FUNCTION MENU PEGAWAI
#function untuk menampilkan menu pilihan masuk sebagai pegawai seperti tampilkan data, menambahkan data, mengupdate/ganti data, menghapus data, & mengembalikan data yang terhapus, dengan menggunakan input (data & user)
def menupegawai2(data,user):
    while True:
        print(f'''
    Selamat Datang {user}
    Silahkan pilih menu:
        1. Menampilkan semua data
        2. Menambahkan data
        3. Mengganti data
        4. Menghapus data  
        5. Mengembalikan kembali data terhapus     
        6. Kembali ke menu utama
        ''')
        user_input = int(input('Masukkan Pilihan Anda: '))
        if user_input == 1:
            menu_read_data(data)
        elif user_input == 2:
            create_data(data,user)
        elif user_input == 3:
            replace_data(data,user)
        elif user_input == 4:
            delete_data(data,user)
        elif user_input == 5:
            callback_data(data,deleted_data)
        elif user_input == 6:
            mainmenu(data)
        else:
          print('Masukkan pilihan 1 sd 5!')
    
# FUNCTION MENU CUST
#function untuk menampilkan menu pilihan masuk sebagai customer/pelanggan seperti menampilkan data & mencari data
def menucust(data):
    while True:
        print(''' 
        ###Selamat Datang di Yellow Phone Book###
        Silahkan masukkan menu: 
            1. Menampilkan data
            2. Mencari data
            3. Kembali ke menu utama
              ''')
        inputcust = int(input('Silahkan masukkan pilihan Anda: '))
        if inputcust == 1:
            menu_read_data(data)
        elif inputcust == 2:
            search_data(data)
        elif inputcust == 3:
            mainmenu(data)    
        else:
            print('Masukkan pilihan 1 sd 2 atau pilih 3 untuk kembali ke menu utama!')

# FUNCTION MAIN MENU
#function main menu dimana terdapat pilihan masuk sebagai pegawai atau sebagai customer/pelanggan dengan input (data)
def mainmenu(data):
    while True:
        print('''
    ########Selamat Datang di Yellow Phone Book########
    Silahkan pilih menu: 
        1. Masuk sebagai Employee atau Pegawai
        2. Masuk Sebagai Customer atau Tamu
        3. Keluar             
            ''')
        choice1 = int(input('Silahkan masukkan pilihan anda: '))
        try:
            if choice1 == 1:
                menulogin(data)
            elif choice1 == 2:
                menucust(data)
            elif choice1 == 3:
                print('Terima kasih!')
                break
        except:
            print('Masukkan pilihan 1 sd 3!')
        break

#menjalankan funtion dengan input data = MasterData 
mainmenu(MasterData)
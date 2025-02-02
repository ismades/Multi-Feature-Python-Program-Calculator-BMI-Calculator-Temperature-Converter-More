# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:50:59 2025

@author: user
"""
# Loop utama agar menu utama selalu muncul setelah selesai menggunakan fitur
while True:
    # Menampilkan Menu Utama
    print("\n=== Operasi Kalkulator, BMI, dan Konversi Suhu ===")
    print("========== Menu Utama ==========")
    print("1. Kalkulator")
    print("2. Sistem Penilaian")
    print("3. BMI")
    print("4. Konversi Suhu")
    print("5. Warnet")
    print("6. Keluar\n")

    # Meminta input pilihan operasi dari pengguna
    A = int(input("Masukkan pilihan operasi (1-6): "))

    # ========= Nomor 1: KALKULATOR =========
    if A == 1:
        while True: # Loop agar tetap di dalam menu Kalkulator setelah perhitungan
            print("\n========== Kalkulator ==========")
            print("1. Penjumlahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            print("5. Kembali ke Menu Utama\n")  

            operasi = int(input("Masukkan Sistem Operasi (1-5): "))

            # Jika pengguna memilih operasi 1-4, lakukan perhitungan
            if operasi in [1, 2, 3, 4]:
                B = int(input("Masukkan angka pertama: "))
                C = int(input("Masukkan angka kedua: "))
                
                # Proses perhitungan berdasarkan pilihan operasi
                if operasi == 1:
                    print("Hasil Penjumlahan:", B + C)
                elif operasi == 2:
                    print("Hasil Pengurangan:", B - C)
                elif operasi == 3:
                    print("Hasil Perkalian:", B * C)
                elif operasi == 4:
                    if C != 0:
                        print("Hasil Pembagian:", B / C)
                    else:
                        print("Error: Tidak bisa dibagi dengan nol!")
            # Jika pengguna memilih kembali ke menu utama
            elif operasi == 5:
                kembali = input("Ketik 'y' untuk kembali ke menu utama atau enter untuk input ulang: ")
                if kembali.lower() == 'y':
                    break  # Keluar dari loop Kalkulator dan kembali ke menu utama
                elif kembali.lower() != 'y':
                    continue # Kembali ke menu Kalkulator untuk input ulang     
            else:
                print("Pilihan tidak valid. Coba lagi!")

    # ========= Nomor 2: SISTEM PENILAIAN =========
    elif A == 2:
        while True:
            Nilai_Tugas = int(input("\nMasukkan nilai tugas (0-100): "))
         
            # Menentukan kategori nilai berdasarkan input
            if Nilai_Tugas < 60:
                print("Kurang")
            elif Nilai_Tugas >= 60 and Nilai_Tugas <=80:
                print("Bagus")
            elif Nilai_Tugas > 80 and Nilai_Tugas <= 100:
                print("Terbaik")
            else:
                print("Yakin? Angkanya udah bener? Coba cek lagi!")

            # Opsi kembali ke menu utama atau input ulang
            kembali = input("Ketik 'y' untuk kembali ke menu utama atau enter untuk input ulang: ")
            if kembali.lower() == 'y':
                break  
            elif kembali.lower() != 'y':
                continue
            
            

    # ========= Nomor 3: BMI KALKULATOR =========
    elif A == 3:
        while True:
            Berat_Badan = float(input("\nMasukkan Berat Badan (Kg): "))
            Tinggi_Badan = float(input("Masukkan Tinggi Badan (Cm): ")) / 100  

            BMI = Berat_Badan / (Tinggi_Badan ** 2)
            
            # Menentukan kategori BMI berdasarkan hasil
            if BMI < 18.5:
               print(f"{BMI:.2f} Kurang(Kenapa? Coba perbaiki lagi asupannya!),")
            elif BMI >= 18.5 and BMI <= 24.9:
               print(f"{BMI:.2f} Norma(Hmm,Walau berat badan normal, tetap jaga pola makan yaa!)")
            elif BMI >=25.0 and BMI <=29.9:
               print(f"{BMI:.2f} Overweight(Waduh, Alamat nih!, Siap-siap obesitas kalau pola makannya gitu terus))")
            else:
               print(f"{BMI:.2f} Obesitas (Aduhh, Ayo diet, kayaknya kamu butuh extra support untuk diet, diet bukan untuk kurus, tapi menghindari penyakit yang tidak diinginkan)")
           
            # Opsi kembali ke menu utama atau input ulang
            kembali = input("Ketik 'y' untuk kembali ke menu utama atau enter untuk input ulang: ")
            if kembali.lower() == 'y':
                break  
            elif kembali.lower() != 'y':
                continue
            

    # ========= Nomor 4: KONVERSI SUHU =========
    elif A == 4:
        while True:
            print("\n========== Konversi Suhu ==========")
            print("1. C → F")
            print("2. C → R")
            print("3. C → K")
            print("4. F → C")
            print("5. F → R")
            print("6. F → K")
            print("7. R → C")
            print("8. R → F")
            print("9. R → K")
            print("10. K → C")
            print("11. K → F")
            print("12. K → R")
            print("13. Kembali ke Menu Utama\n")

            Suhu = int(input("Masukkan Pilihan (1-13): "))
            #jika memilih konversi suhu
            if Suhu in [1,2,3,4,5,6,7,8,9,10,11,12]:
                if Suhu == 1:
                    C = int(input("Masukkan Suhu:"))
                    F = C * 1.8 + 32
                    print(F,"°F")
                elif Suhu == 2:
                    C = int(input("Masukkan Suhu:"))
                    R = C * 4/5
                    print(R,"°R")
                elif Suhu == 3:
                    C = int(input("Masukkan Suhu:"))
                    K = C + 273.15
                    print(K,"°K")
                elif Suhu == 4:
                    F = int(input("Masukkan Suhu:"))
                    C = (F - 32) * 5/9
                    print(C,"°C")
                elif Suhu == 5:
                    F = int(input("Masukkan Suhu:"))
                    R = (F - 32) * 4/9
                    print(R,"°R")
                elif Suhu == 6:
                    F = int(input("Masukkan Suhu:"))
                    K = (F - 32) * 5/9 + 273.15
                    print(K,"°K")
                elif Suhu == 7:
                    R = int(input("Masukkan Suhu:"))
                    C = R * 5/4
                    print(C,"°C")
                elif Suhu == 8:
                    R = int(input("Masukkan Suhu:"))
                    F = (R * 9/4) + 32
                    print(F,"°F")
                elif Suhu == 9:
                    R = int(input("Masukkan Suhu:"))
                    K = (R * 5/4) + 273.15
                    print(K,"°K")
                elif Suhu == 10:
                    K = int(input("Masukkan Suhu:"))
                    C = K - 273.15
                    print(C,"°C")
                elif Suhu == 11:
                    K = int(input("Masukkan Suhu:"))
                    F = (K - 273.15) * 9/5 + 32
                    print(F,"°F")
                elif Suhu == 12:
                    K = int(input("Masukkan Suhu:"))
                    R = (K - 273.15) * 4/5
                    print(R,"°R")
            # Jika pengguna memilih kembali ke menu utama
            elif Suhu == 13:
                kembali = input(("Ketik 'y' untuk kembali ke menu utama atau enter untuk input ulang: "))
                if kembali.lower() == "y":
                    break 
                elif kembali != 'y':
                    continue
            else:
                print("Coba Lagi!")
                

    # ========= Nomor 5: WARNET =========
    elif A == 5:
        while True:
            Durasi = int(input("\nMasukkan Durasi (per jam): "))
            Harga_Bermain_Perjam = 8000

            print("==== Pilihan Bermain ====")
            print("1. Bawa 1 Teman Main (Diskon 30%)")
            print("2. 1 Jam atau Lebih (Tanpa Diskon)")
            print("3. Kembali ke Menu Utama\n")  

            Discount_or_Not = int(input("Pilih Jenis Durasi Bermain (1-2): "))
            if Discount_or_Not in [1,2]:
                if Discount_or_Not == 1:
                    Total_Harga = Durasi * Harga_Bermain_Perjam * 0.7  # Diskon 30%
                    print(f"Total Harga: Rp. {Total_Harga}")
                elif Discount_or_Not == 2:
                    Total_Harga = Durasi * Harga_Bermain_Perjam
                    print(f"Total Harga: Rp. {Total_Harga}")
               
            elif Discount_or_Not == 3:    
                kembali = input("Ketik 'y' untuk kembali ke menu utama atau enter untuk input ulang: ")
                if kembali.lower() == 'y':
                    break  
                elif kembali.lower() != 'y':
                    continue
            else:
                print("Pilihan Tidak Valid.")

    # ========= Nomor 6: KELUAR =========
    elif A == 6:
        print("Terima kasih telah menggunakan program ini! ")
        break  # Keluar dari program

    else:
        print("Pilihan tidak valid. Silakan coba lagi!")

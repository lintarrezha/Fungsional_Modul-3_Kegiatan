def konversi_minggu(minggu):
    def konversi_hari(hari):
        def konversi_jam(jam):
            def konversi_menit(menit):
                # Menghitung total menit berdasarkan minggu, hari, jam, dan menit
                return minggu * 7 * 24 * 60 + hari * 24 * 60 + jam * 60 + menit
            return konversi_menit
        return konversi_jam
    return konversi_hari

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]
outputdata = []

# Iterasi melalui setiap string dalam 'data'
for item in data:
    parts = item.split()  # Membagi string menjadi kata-kata
    minggu = int(parts[0])  # Mengambil jumlah minggu
    hari = int(parts[2])    # Mengambil jumlah hari
    jam = int(parts[4])     # Mengambil jumlah jam
    menit = int(parts[6])   # Mengambil jumlah menit
    total_menit = konversi_minggu(minggu)(hari)(jam)(menit)  # Menggunakan fungsi bersarang untuk menghitung total menit
    outputdata.append(total_menit)  # Menambahkan total menit ke dalam 'outputdata'

print("Data:", data)  # Mencetak data asli
print("Output Data:", outputdata)  # Mencetak hasil konversi menjadi total menit

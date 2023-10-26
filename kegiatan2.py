data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

integer_data = []  # Inisialisasi daftar untuk mengumpulkan angka-angka

# Iterasi melalui setiap string dalam 'data'
for item in data:
    parts = item.split()  # Membagi string menjadi kata-kata
    integers = list(filter(lambda x: x.isdigit(), parts))  # Menyaringg dan mengambil angka dari kata-kata
    integer_data.append(integers)  # Menambahkan angka-angka ke dalam 'integer_data'

# Mencetak daftar angka integer untuk setiap string
for item in integer_data:
    print(item)

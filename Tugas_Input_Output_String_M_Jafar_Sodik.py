
# Biodata Sederhana
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
prodi = input("Masukkan Program Studi: ")

print("\n=== BIODATA MAHASISWA ===")
print("Nama           : {}".format(nama))
print("NIM            : {}".format(nim))
print("Program Studi  : {}".format(prodi))

# Tugas manipulasi string
kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"

print("\n=== Output Manipulasi Kalimat ===")
print("a. {}".format(" ".join(kalimat.lower().split()[1:])))
print("b. {}".format(kalimat.replace("U", "").replace("I", "").replace("E", "A")))
print("c. {} {}".format(kalimat.split()[-1], " ".join(kalimat.split()[:-1])))
print("d. {}".format("".join([word[0] for word in kalimat.split()])))
print("e. {}".format(" ".join(kalimat.split()[::-1])))

# Identitas
print("\nProgram dibuat oleh:")
print("Nama : M. Jafar Sodik")
print("NIM  : 20240040062")

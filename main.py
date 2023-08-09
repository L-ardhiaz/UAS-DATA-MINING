import math
from shlex import join

# Menentukan Datamahasiswa
data_mahasiswa = [
    {"NO": "D1", "IP1": 3.20, "IP2": 3.16, "RK": 98.44},
    {"NO": "D2", "IP1": 3.43, "IP2": 3.40, "RK": 97.67},
    {"NO": "D3", "IP1": 3.40, "IP2": 3.43, "RK": 97.71},
    {"NO": "D4", "IP1": 3.40, "IP2": 3.48, "RK": 100.00},
    {"NO": "D5", "IP1": 3.42, "IP2": 3.77, "RK": 98.96},
    {"NO": "D6", "IP1": 2.84, "IP2": 3.44, "RK": 99.34},
    {"NO": "D7", "IP1": 3.03, "IP2": 3.86, "RK": 99.69},
    {"NO": "D8", "IP1": 2.82, "IP2": 3.28, "RK": 98.99},
    {"NO": "D9", "IP1": 3.61, "IP2": 3.82, "RK": 99.65},
    {"NO": "D10", "IP1": 3.61, "IP2": 3.88, "RK": 99.65},

    # {"NO": "D11", "IP1": 3.20, "IP2": 3.16, "RK": 98.44},
    # {"NO": "D12", "IP1": 3.43, "IP2": 3.40, "RK": 97.67},
    # {"NO": "D13", "IP1": 3.40, "IP2": 3.43, "RK": 97.71},
    # {"NO": "D14", "IP1": 3.40, "IP2": 3.48, "RK": 100.00},
    # {"NO": "D15", "IP1": 2.2, "IP2": 2.77, "RK": 80.16},
    # {"NO": "D16", "IP1": 1.4, "IP2": 1.44, "RK": 89.14},
    # {"NO": "D17", "IP1": 4.03, "IP2": 3.12, "RK": 72.24},
    # {"NO": "D18", "IP1": 5.82, "IP2": 3.10, "RK": 64.56},
]

# Menentukan Pusat klaster awal
C1 = [3.40, 3.43, 97.71]
C2 = [3.61, 3.82, 99.65]
print("=============================================\n")
print("Menentukan Pusat klaster awal\n")
print("Cluster C1 = ",C1)
print("Cluster C2 = ",C1)
# Fungsi untuk menghitung jarak Euclidean Distance
def euclidean_distance(point1, point2):
    return (sum((x - y) ** 2 for x, y in zip(point1, point2))) ** 0.5

# Menghitung jarak setiap data ke pusat klaster C1 dan C2
for data in data_mahasiswa:
    data["C1"] = euclidean_distance([data["IP1"], data["IP2"], data["RK"]], C1)
    data["C2"] = euclidean_distance([data["IP1"], data["IP2"], data["RK"]], C2)

# Menampilkan hasil pada menghitung jarak setiap data ke pusat kluster
print("=============================================\n")
print("Menampilkan hasil pada menghitung jarak setiap data ke pusat kluster\n")
print("NO\tIP1\t\tIP2\t\tRK\t\tC1\t\tC2")
for data in data_mahasiswa:
    print(f"{data['NO']}\t{data['IP1']:.2f}\t{data['IP2']:.2f}\t{data['RK']:.2f}\t{data['C1']:.2f}\t{data['C2']:.2f}")

# Fungsi untuk menentukan klaster berdasarkan jarak terdekat
def determine_cluster(data, C1, C2):
    if C1 and C2:  # Jika C1 dan C2 tidak kosong (ada pusat klaster)
        distance_to_C1 = euclidean_distance([data["IP1"], data["IP2"], data["RK"]], C1)
        distance_to_C2 = euclidean_distance([data["IP1"], data["IP2"], data["RK"]], C2)
        if distance_to_C1 < distance_to_C2:
            return "C1"
        else:
            return "C2"
    else:  # Jika C1 dan C2 masih kosong (belum ada pusat klaster)
        if data["C1"] < data["C2"]:
            return "C1"
        else:
            return "C2"
# Menentukan klaster untuk setiap data dan perbarui titik pusat klaster
for data in data_mahasiswa:
    data["Cluster"] = determine_cluster(data,"","")

# Memperbarui titik pusat klaster berdasarkan klaster saat ini
def update_cluster_center(cluster):
    cluster_data = [data for data in data_mahasiswa if data["Cluster"] == cluster]
    num_data = len(cluster_data)
    ip1_avg = sum(data["IP1"] for data in cluster_data) / num_data
    ip2_avg = sum(data["IP2"] for data in cluster_data) / num_data
    rk_avg = sum(data["RK"] for data in cluster_data) / num_data
    return [round(ip1_avg,2), round(ip2_avg,2), round(rk_avg,2)]

# Memperbarui titik pusat klaster berdasarkan klaster saat ini
C1 = update_cluster_center("C1")
C2 = update_cluster_center("C2")
print("===================================")
print("Menentukan cluster (kelompok) setiap baris data dan perbaharui titik pusat cluster:")
print("\nNO\tIP1\t\tIP2\t\tRK\t\tC1\t\tC2\t\tCluster")
# Menampilkan hasil
for data in data_mahasiswa:
    print(f"{data['NO']}\t{data['IP1']:.2f}\t{data['IP2']:.2f}\t{data['RK']:.2f}\t{data['C1']:.2f}\t{data['C2']:.2f}\t{data['Cluster']}")

# Menampilkan hasil Cluster Baru
print("=========================== Pusat Cluster Baru ===========================================")
print("C1 = ",C1)
print("C2 = ",C2)
print("======================================================================")
# Fungsi untuk menentukan klaster berdasarkan jarak terdekat dengan pusat klaster
# C1 =  [3.33, 3.37, 98.2]
# C2 =  [3.33, 3.75, 99.29]
prev_C1, prev_C2 = None, None
current_C1, current_C2 = C1,C2
iteration = 1
C1_member, C2_member = [],[]

while prev_C1 != current_C1 or prev_C2 != current_C2:
    print("Iterasi ",iteration," : \n")
    print("CS = Cluster Sebelumnya")
    print("CB = Cluster Baru")
    print("NO\tIP1\t\tIP2\t\tRK\t\tC1\t\tC2\t\tCS\t\tCB")
    # Menghitung ulang klaster dan pusat klaster berdasarkan klaster saat ini
    for data in data_mahasiswa:
        prev_cluster = data["Cluster"]
        data["C1"] = euclidean_distance([data["IP1"], data["IP2"], data["RK"]], current_C1)
        data["C2"] = euclidean_distance([data["IP1"], data["IP2"], data["RK"]], current_C2)
        data["Cluster"] = determine_cluster(data, current_C1, current_C2)
        if data["Cluster"] == "C1":
            C1_member.append(data["NO"])
        elif data["Cluster"] == "C2":
            C2_member.append(data["NO"])
        print(f"{data['NO']}\t{data['IP1']:.2f}\t{data['IP2']:.2f}\t{data['RK']:.2f}\t{data['C1']:.2f}\t{data['C2']:.2f}\t{prev_cluster}\t\t{data['Cluster']}")

    prev_C1, prev_C2 = current_C1, current_C2
    current_C1, current_C2 = C1, C2
    iteration += 1

print("========================= Hasil =============================================")
print("Anggota Cluster 1 (C1) = ",",".join(C1_member))
print("Anggota Cluster 2 (C2) = ",",".join(C2_member))
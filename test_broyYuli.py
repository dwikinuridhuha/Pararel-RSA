from mpi4py import MPI

def cekGanjilGenap(a, b):
	if a%b == 0:
		return 'genap'
	else:
		return 'ganjil'

def jikaGenap():
    n = int(QN/size)
    atas = rank*n
    bawah = ((rank+1)*n)-1
    print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)

def jikaGanjil():
    n = int(QN/size)
    mod = int(QN%size)

    if(rank == (size-1)):
        atas = rank*n
        bawah = (((rank+1)*n)-1)+mod
        print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)
    else:
        atas = rank*n
        bawah = ((rank+1)*n)-1
        print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# QN = int(input("masukan Nilai QN: "))
QN = 121
a = []

for x in range(QN):
	a.append(x)

# for x in range(QN):
# 	print(a[x])

cgg = cekGanjilGenap(QN, size)

if("genap" == cgg):
	n = QN/size
	atas = rank*n
	bawah = ((rank+1)*n)-1
	print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)
	for x in range(int(rank*(QN/size)), int(((rank+1)*(QN/size)))):
		print("rank :", rank, "a: ", a[x])
else:
	n = QN/size
	atas = int(rank*n)
	bawah = int(((rank+1)*n)-1)
	print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)

print("\n")

# if (rank > 0):
# 	for x in range(atas,bawah+1):
# 		print("semuadata rank 0 : ", a[x] )
# if (rank == 1):
# 	for x in range(atas,bawah+1):
# 		print("semuadata rank 1 :", a[x] )
# if (rank == 2):
# 	for x in range(atas,bawah+1):
# 		print("semuadata rank 2 :", a[x] )
# if (rank == 3):
# 	for x in range(atas,bawah+1):
# 		print("semuadata rank 3 :", a[x] )

for x in range(atas,bawah+1):
	print("semuadata rank ", rank, ": ", a[x] )

# print("size: ", size, "dan rank: ", rank, " QN: ", QN, 'CGG: ', cgg, "\n")

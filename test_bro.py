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

QN = 120
a = []

for x in range(QN):
	a.append(x)

cgg = cekGanjilGenap(QN, size)

if("genap" == cgg):
	n = QN/size
	atas = int(rank*n)
	bawah = int(((rank+1)*n)-1)
	print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)
else:
	n = QN/size
	atas = int(rank*n)
	bawah = int(((rank+1)*n)-1)
	print("rank: ", rank, "atas: ", atas, "bawa: ", bawah)

for x in range(atas, bawah+1):
	print("rank : ", rank, "a: ", a[x])

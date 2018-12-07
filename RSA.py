import math
import random

def cekGanjilGenap(a, b):
	if a%b == 0:
		return 'genap'
	else:
		return 'ganjil'

def cekPrima(num):
	if num>1:
		for i in range (2,num):
			if num%i == 0: #Bilangan bisa dibagi bilangan lain
				return 0
			else: #Bilangan Prima
				return 1
	else: #Bilangan minus, 0 atau 1
		return 0

def inputPQ():
	global P
	global Q
	x = int(input("P : "))
	y = int(input("Q : "))
	cekPrima(x)
	cekPrima(y)
	if cekPrima(x)==1 and cekPrima(y)==1:
		P = x
		Q = y
	else:
		print ("P atau Q bukan bilangan prima!\n")
		return inputPQ()

def pubKey(QN): #key e
	global e
	print ("\nMenentukan Public Key (e)")

	for x in range(2, QN):			#bagian ini yang menjadi awal untuk di pararelkan
		if math.gcd(x,QN) == 1:
			e_avail.append(x)		#bagian ini yang menjadi akhir untuk di pararelkan kemudian di taru ke variabel 'e_avail'

	print ("Nilai e yang bisa digunakan: ", e_avail)
	answer = input("\nIngin me-random nilai e? (y/n): ")
	if answer == 'y':
		e = int(random.choice(e_avail))
	else:
		e = int(input("Pilih nilai e yang tersedia di list di atas: "))
	print ("\nNilai e yang digunakan : ", e)
	return e

def inverseGCD(a, b): #inverse Modulo
	if a == 0:
		return (b, 0, 1)
	else:
		g, x, y = inverseGCD(b%a, a)
		return (g, y - (b // a) * x, x)

def pvtKey(a, QN): #key d
	global d
	if a > 0:
		d = a
	else:
		d = QN + a
	print ("Nilai d yang digunakan : ", d)

P = 0
Q = 0
inputPQ() #memasukan nilai P dan Q

N = P*Q #Nilai N
QN = (P-1)*(Q-1) #totien
e = 0 #pubKey
e_avail = [] #pubKey yang tersedia
d = 0 #pvtKey

print ("Generated N = ",N)
print ("Generated QN = ", QN)

pubKey(QN)
pvtKey(inverseGCD(e, QN)[1], QN)

######################################################

print ("\n###\n\nMetode Enkripsi RSA")
print ("Dari sisi pengirim mengetahui:")
print ("N = ", N, "e = ", e)
#print ("nilai e = ", cekGanjilGenap(e), " nilai d = ", cekGanjilGenap(d), " nilai QN = ", cekGanjilGenap(QN))

pesan = input("Masukkan Plain Text : ")
# pesan = input("Masukkan Plain Text : ")
data = list(pesan)
print ("panjang Pesan = ", len(data), " dan juga = ", cekGanjilGenap(len(data), 2))

ciperASCII = [] #penampung kode ASCII
ciperList = [] #penampung karakter dari enripsi

#bagian ini yang akan jadi di pararelkan
for x in range (len(data)):
	M = ord(data[x]) #mengubah ke ASCII
	ciper = M**e%N #proses enripsi perkarakter
	ciperChr = chr(ciper) #hasil encrip dirubah ke karakter lagi
	ciperASCII.append(ciper) #kode ASCII di masukan ke list a
	ciperList.append(ciperChr) #hasil encrip yang berupa karakter di gabungkan lagi di list b
ciperText = ''.join(ciperList) #menjadikan string dari list b

print ("Cipher Text dalam ASCII: ", ciperASCII)
print ("Cipher Text dalam Char: ", ciperText)

######################################################

print ("\n###\n\nMetode Dekripsi RSA")
print ("Dari sisi penerima mengetahui:")
print ("N = ", N, "\ne = ", e, "\nd = ", d, "\nCipher Text = ", ciperText)

decrypted = []
#bagian ini yang akan jadi di pararelkan
for x in range (len(ciperText)):
	MM = ord(ciperText[x])
	decrypt = MM**d%N
	decryptChr = chr(decrypt)
	decrypted.append(decryptChr)
decryptedStr = ''.join(decrypted)

print ("Pesan yang sudah di dekrip: ", decryptedStr)

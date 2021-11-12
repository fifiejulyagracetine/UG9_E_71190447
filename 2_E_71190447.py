nama = str(input("Nama :"))
a, b, c, d = input("Tempat tanggal lahir :").split()

print("Haloo!"," , ".join(reversed(nama.split())))
print ("Anda lahir di {} pada tanggal {} {} {}".format(a, b, c,d))
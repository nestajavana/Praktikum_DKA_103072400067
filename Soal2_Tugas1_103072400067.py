def fibonacci(n):
    if n <= 0: #mengecek n kurang atau sama dengan 0 atau tidak
        return 0 #jika iya, maka 0 (tidak valid)
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    a = 1 
    b = 1  
    
    for i in range(3, n + 1): #rumus perulangan untuk menghitung fibonacci
        c = a + b
        a = b
        b = c
    
    return b

def cetakFibonacci(n):
    if n <= 0:
        print("Tidak ada deret.") #karena n yang diminta sama dengan atau kurang dari 0 (tidak valid)
        return
    
    a = 1
    b = 1
    
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            print(1, end=" ")
        else:
            c = a + b
            print(c, end=" ")
            a = b
            b = c

n = int(input("Masukkan nilai n: ")) #input suku n untuk menentukan sampai suku ke berapa

hasil = fibonacci(n)
print("Nilai Fibonacci ke-", n, "adalah:", hasil) #nilai dari suku ke n

print("Deret Fibonacci sampai suku ke-", n, "adalah:") #print deret fibonacci dari awal sampai suku ke n
cetakFibonacci(n)
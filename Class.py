class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def hitungLuas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang}cm, dan lebar {self.lebar}cm"
    
def main():
    try:
        panjang = int(input("Masukkan input panjang: "))
        lebar = int(input("Masukkan input lebar: "))
        pp = PersegiPanjang(panjang, lebar)
        print(pp)
        if panjang > 0 and lebar > 0:
            print(f"Keliling: {pp.hitungKeliling()}cm")
            print(f"Luas: {pp.hitungLuas()}cm²")
        else:
            print("Angka yang dimasukkan harus lebih dari 0!")
    except ValueError:
        print("Masukkan yang benar!")

if __name__ == "__main__":
    main()
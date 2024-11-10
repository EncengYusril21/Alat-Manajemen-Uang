class MoneyManager:
    def __init__(self):
        self.balance = 0.0
        self.income = []
        self.expenses = []

    def add_income(self, amount, source):
        self.income.append({'amount': amount, 'source': source})
        self.balance += amount
        print(f"Pendapatan sebesar {amount} dari {source} telah ditambahkan.")

    def add_expense(self, amount, category):
        if amount > self.balance:
            print("Pengeluaran melebihi saldo saat ini!")
        else:
            self.expenses.append({'amount': amount, 'category': category})
            self.balance -= amount
            print(f"Pengeluaran sebesar {amount} untuk {category} telah ditambahkan.")

    def show_balance(self):
        print(f"Sisa saldo saat ini: {self.balance}")

    def show_income(self):
        print("\nPendapatan:")
        print(f"{'Sumber':<20} {'Jumlah':<10}")
        print("-" * 30)
        for item in self.income:
            print(f"{item['source']:<20} {item['amount']:<10}")

    def show_expenses(self):
        print("\nPengeluaran:")
        print(f"{'Kategori':<20} {'Jumlah':<10}")
        print("-" * 30)
        for item in self.expenses:
            print(f"{item['category']:<20} {item['amount']:<10}")

def main():
    manager = MoneyManager()
    while True:
        print("\n--- Alat Manajemen Uang ---")
        print("1. Tambah Pendapatan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Saldo")
        print("4. Tampilkan Pendapatan")
        print("5. Tampilkan Pengeluaran")
        print("6. Keluar")

        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            amount = float(input("Masukkan jumlah pendapatan: "))
            source = input("Masukkan sumber pendapatan: ")
            manager.add_income(amount, source)
        elif choice == '2':
            amount = float(input("Masukkan jumlah pengeluaran: "))
            category = input("Masukkan kategori pengeluaran: ")
            manager.add_expense(amount, category)
        elif choice == '3':
            manager.show_balance()
        elif choice == '4':
            manager.show_income()
        elif choice == '5':
            manager.show_expenses()
        elif choice == '6':
            print("Terima kasih telah menggunakan alat manajemen uang!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
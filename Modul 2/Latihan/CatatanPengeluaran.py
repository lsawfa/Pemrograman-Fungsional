expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# TODO 1 Buatlah Fungsi add_expense disini
add_expense = lambda expenses, date, description, amount: expenses + [{'tanggal': date, 'deskripsi': description, 'jumlah': amount}]

# TODO 2 Buatlah fungsi calculate_total_expenses disini
calculate_total_expenses = lambda expenses, date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)

# TODO 3 Buatlah fungsi get_expenses_by_date disini
get_expenses_by_date = lambda expenses, date: [expense for expense in expenses if expense['tanggal'] == date]

# TODO 4 Buatlah fungsi generate_expenses_report disini
generate_expenses_report = lambda expenses: ("\n".join([f"{expense['tanggal']}: {expense['deskripsi']} - Rp {expense['jumlah']}" for expense in expenses]))

def add_expense_interactively(expenses):
    try:
        new_expenses = add_expense(expenses, input("Masukkan tanggal pengeluaran (YYYY-MM-DD): "), input("Masukkan deskripsi pengeluaran: "), int(input("Masukkan jumlah pengeluaran: ")))
        print("Pengeluaran berhasil ditambahkan.")
        return new_expenses
    except ValueError:
        print("Jumlah pengeluaran harus berupa angka.")
        return expenses

def view_expenses_by_date(expenses):
    try:
        date = input("Masukkan tanggal (YYYY-MM-DD): ")
        expenses_on_date = get_expenses_by_date(expenses, date)
        if not expenses_on_date:
            print(f"Tidak ada pengeluaran pada tanggal {date}.")
        else:
            print(f"\nPengeluaran pada tanggal {date}:")
            for expense in expenses_on_date:
                print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
    except ValueError:
        print("Format tanggal tidak valid.")

def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    print(expenses_report)

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
get_user_input = lambda command: int(input(command))

def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            try:
                date = input("Masukkan tanggal (YYYY-MM-DD): ")
                total_expenses = calculate_total_expenses(expenses, date)
                print(f"\nTotal Pengeluaran Harian pada tanggal {date}: Rp {total_expenses}")
            except ValueError:
                print("Format tanggal tidak valid.")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == "__main__":
    main()

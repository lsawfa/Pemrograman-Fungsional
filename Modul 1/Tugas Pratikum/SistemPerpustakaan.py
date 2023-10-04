account_list = {
    "admin": {
        "username": "admin",
        "password": "umm1964"
    },
    "user": {}
}
available_books = {
        1: "Python Programming",
        2: "Introduction to Machine Learning",
        3: "Data Science for Beginners",
    }
user_books = {}

def login(account_list, username, password):
    if username == account_list["admin"]["username"] and password == account_list["admin"]["password"]:
        return "admin"
    elif any(account["username"] == username and account["password"] == password for account in account_list["user"].values()):
        return "user"
    else:
        return None

def insert_book(available_books):
    book_id = len(available_books) + 1
    book_title = input("\nMasukkan judul buku: ")
    available_books[book_id] = book_title
    print(f"Buku '{book_title}' berhasil ditambahkan dengan ID {book_id}")

def print_available_books(available_books):
    print("\nDaftar buku yang tersedia:")
    for book_id, book_title in available_books.items():
        print(f"{book_id}: {book_title}")


def borrow_book(available_books, user_books, username):
    print_available_books(available_books)
    book_id = int(input("\nMasukkan ID buku yang ingin dipinjam: "))
    if book_id in available_books:
        if username not in user_books:
            user_books[username] = {}
        if book_id not in user_books[username]:
            user_books[username][book_id] = available_books[book_id]
            print(f"Buku '{available_books[book_id]}' berhasil dipinjam oleh {username}")
            del available_books[book_id]
        else:
            print("Buku sudah dipinjam oleh Anda sebelumnya.")
    else:
        print("ID buku tidak valid.")

def print_borrowed_books(user_books, username):
    if username in user_books and user_books[username]:
        print("\nBuku yang Anda pinjam:")
        for book_id, book_title in user_books[username].items():
            print(f"{book_id}: {book_title}")
    else:
        print("Anda tidak memiliki buku yang dipinjam.")

def return_book(available_books, user_books, username):
    if username in user_books and user_books[username]:
        print_borrowed_books(user_books, username)  # Menampilkan buku yang dipinjam
        returned_book_id = int(input("\nMasukkan ID buku yang ingin dikembalikan: "))
        if returned_book_id in user_books[username]:
            available_books[returned_book_id] = user_books[username][returned_book_id]
            print(f"Buku '{user_books[username][returned_book_id]}' berhasil dikembalikan.")
            del user_books[username][returned_book_id]
        else:
            print("ID buku tidak valid.")
    else:
        print("Anda tidak memiliki buku yang dipinjam.")

def main():
    while True:
        print("Selamat Datang di Sistem Perpustakaan")
        print("1. Login")
        print("2. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            user_type = login(account_list, username, password)
            if user_type == "admin":
                while True:
                    print("\nMenu Admin")
                    print("1. Insert Data Buku Baru")
                    print("2. Show Available Book")
                    print("3. Logout")
                    admin_choice = input("Pilih opsi: ")
                    if admin_choice == "1":
                        insert_book(available_books)
                    elif admin_choice == "2":
                        print_available_books(available_books);
                    elif admin_choice == "3":
                        break
            else:
                while True:
                    print("\nMenu User")
                    print("1. Pinjam Buku")
                    print("2. Kembalikan Buku")
                    print("3. Show Borrowed Book")
                    print("4. Logout")
                    user_choice = input("Pilih opsi: ")
                    if user_choice == "1":
                        borrow_book(available_books, user_books, username)
                    elif user_choice == "2":
                        return_book(available_books, user_books, username)
                    elif user_choice == "3":
                        print_borrowed_books(user_books, username)
                    elif user_choice == "4":
                        break
                    else:
                        print("Opsi tidak valid.")
        else:
            break

if __name__ == "__main__":
    main()
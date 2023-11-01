from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def count_movies_by_genre(movies):
    genre_counts = {genre: len(list(filter(lambda x: x["genre"] == genre, movies)) ) for genre in set(map(lambda x: x["genre"], movies))}
    return genre_counts

def average_rating_by_year(movies):
    year_ratings = reduce(lambda year_ratings, movie: 
        {**year_ratings, movie["year"]: year_ratings.get(movie["year"], []) + [movie["rating"]]}, 
        movies, {})
    return {year: sum(ratings) / len(ratings) for year, ratings in year_ratings.items()}

find_highest_rated_movie = lambda movies: max(movies, key=lambda x: x["rating"])

def find_movie_by_title(movies, title):
    matching_movies = list(filter(lambda movie: movie["title"] == title, movies))
    return matching_movies[0] if matching_movies else None

while True:
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    task = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if task == "1":
        genre_counts = count_movies_by_genre(movies)
        print("Jumlah Film Berdasarkan Genre:")
        print(genre_counts)
    elif task == "2":
        year_ratings = average_rating_by_year(movies)
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        print(year_ratings)
    elif task == "3":
        highest_rated_movie = find_highest_rated_movie(movies)
        print("Film dengan Rating Tertinggi:")
        print("Informasi Film:", highest_rated_movie["title"])
        print("Rating:", highest_rated_movie["rating"])
        print("Tahun Rilis:", highest_rated_movie["year"])
        print("Genre:", highest_rated_movie["genre"])
    elif task == "4":
        title = input("Masukkan judul film yang ingin dicari: ")
        movie = find_movie_by_title(movies, title)
        if movie:
            print("Informasi Film:", movie["title"])
            print("Rating:", movie["rating"])
            print("Tahun Rilis:", movie["year"])
            print("Genre:", movie["genre"])
        else:
            print("Film dengan judul tersebut tidak ditemukan.")
    elif task == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor tugas yang valid.")
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

filtered_data = list(map(lambda item: list(map(int, filter(lambda x: x.isdigit(), item.split()))), data))

for result in filtered_data:
    print(result)
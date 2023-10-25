data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi dengan inputan weeks, days, hours, dan minutes untuk convert data ke menit dengan output minutes
# Fungsi di bawah ini menerapkan currying dan HoF tipe fungsi as return value
def convert_week(weeks):
    def convert_day(days):
        def convert_hour(hours):
            def convert_minute(minutes):
                return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
            return convert_minute
        return convert_hour
    return convert_day

#Fungsi dengan inputan item data untuk split list data sehingga didapatkan output weeks, days, hours, dan minutes
def process_item(item):
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    return convert_week(weeks)(days)(hours)(minutes)

# Penerapan map() untuk memetakan hasil dan dicasting ke list supaya ketika diprint hasilnya bisa terlihat
hasil = list(map(process_item, data))
print(hasil)
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def convert_week(weeks):
    def convert_day(days):
        def convert_hour(hours):
            def convert_minute(minutes):
                return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
            return convert_minute
        return convert_hour
    return convert_day

def process_item(item):
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    return convert_week(weeks)(days)(hours)(minutes)

hasil = list(map(process_item, data))
print(hasil)
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

list_data = []
tuple_data = ()
dict_data = {}

for item_data in random_list:
    if type(item_data) is float:
        tuple_data += (item_data,)
    elif type(item_data) is str:
        list_data.append(item_data)
    elif type(item_data) is int:
        satuan = item_data % 10
        puluhan = (item_data // 10) % 10
        ratusan = item_data // 100
        dict_data[item_data] = (ratusan, puluhan, satuan)

print("Nilai float dalam bentuk tuple:", tuple_data)
print("Nilai string dalam bentuk list:", list_data)
print("Nilai integer dalam bentuk dictionary:", dict_data)
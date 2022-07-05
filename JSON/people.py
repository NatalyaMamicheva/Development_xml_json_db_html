import json

# from pathlib import Path

#Запись в файл
# path = Path('peoples.json')
# data = json.loads(path.read_text(encoding='utf-8'))
# data['peoples'].append({'name': "Tom", 'age': 30, 'city': "Novosibirsk"})
# path.write_text(json.dumps(data), encoding='utf-8')

# Чтение файла
with open('peoples.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

for txt in text['peoples']:
    print(f"{txt['name']} {txt['age']} {txt['city']}")

#Сортировка данных в файле
# with open('peoples.json',  'r', encoding='utf-8') as f:
#     json_data = json.load(f)
#     data_list = json_data['peoples']
#
# json_data['peoples'] = sorted(data_list, key=lambda k: k['age'])
# with open('peoples.json', 'r', encoding='utf-8') as fe:
#     print(json.dumps(json_data))

# Редактирование файла
# with open('peoples.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
# for txt in data['peoples']:
#     if txt["name"] == 'Tom':
#         txt["age"] = 44
#         path = Path('peoples.json')
#         path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding='utf-8')

# Удаление данных из файла
# with open('peoples.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
# for txt in data['peoples']:
#     if txt["name"] == 'Tom':
#         del data['peoples'][-1]
#         path = Path('peoples.json')
#         path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding='utf-8')

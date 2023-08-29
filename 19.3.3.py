import requests

# Добавление питомца POST
res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'},
                    json={'id': 1616, 'category': {'id': 116, 'name': 'BritishCat'}, 'name': 'Sherlok', 'photoUrls': [],
                          'tags': [], 'status': 'available'})
print(res.text)

# Получение информации о питомцах по статусу GET
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
                   headers={'accept': 'application/json'})
print(res.text)

# Изменение информации о питомце (название категории и статус) PUT
res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'},
                    json={'id': 1616, 'category': {'id': 116, 'name': 'RussianCat'}, 'name': 'Sherlok', 'photoUrls': [],
                          'tags': [], 'status': 'pending'})
print(res.text)

# Удаление питомца DELETE
res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'}, json={'id': 1616})
print(res.text)
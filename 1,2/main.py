def take_data():
	cook_book = dict()
    with open('file.txt', 'r', encoding='utf-8') as file:
#Я сделал конкретное имя файла, т.к. для второй функции использовал take_data(), и елси бы я сделал так,
#что бы функция принимамла на вход имя файла, мне пришлось бы делать тоже самое и с get_shop_list_by_dishes(),
#А сказано что ей передаваться будут только dishes и person_count
        for line in file:
            recept_name = line.strip()
            ingredients_quantity = int(file.readline().strip())
            ingredients_list = list()
            for ingredient in range(ingredients_quantity):
                data = file.readline().strip()
                ingredient_dict = dict()
                data = data.split('|')
                ingredient_dict['ingredient_name'] = data[0]
                ingredient_dict['quantity'] = int(data[1])
                ingredient_dict['measure'] = data[2]
                ingredients_list.append(ingredient_dict)
            cook_book[recept_name] = ingredients_list
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    take_data()
    ingr_dict = dict()
    for dish in dishes:
        recept = cook_book[dish]
        for ingredient in recept:
            ingr_name = ingredient['ingredient_name'].strip()
            del ingredient['ingredient_name']
            if ingr_name in ingr_dict.keys():
                ingr_dict[ingr_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                ingr_dict[ingr_name] = ingredient
                ingr_dict[ingr_name]['quantity'] *= person_count

    return ingr_dict

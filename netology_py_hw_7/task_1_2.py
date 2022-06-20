from pprint import pprint

def recipes_reader(recipes_name: str) -> dict:
    cook_book = {}
    with open(recipes_name, encoding='utf-8') as recipes:
        for line in recipes:
            cook_book[line.strip()] = []
            for item in range(int(recipes.readline())):
                list_items = recipes.readline().split('|')
                dict_items = {'ingredient_name': list_items[0],
                                     'quantity': int(list_items[1]),
                                      'measure': list_items[2].strip()}
                cook_book[line.strip()].append(dict_items)
            recipes.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    book = recipes_reader(recipes_file_name )
    for dish in dishes:
      for ingredients in book[dish]:
          if ingredients['ingredient_name'] in  dict_ingredients:
              dict_ingredients[ingredients['ingredient_name']]['quantity'] += ingredients['quantity']*person_count
          else:
              dict_ingredients[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                             'quantity': ingredients['quantity']*person_count}
    return dict_ingredients


recipes_file_name = 'recipes.txt'

# Задача №1
print('-'*100)
book = recipes_reader(recipes_file_name)
print('Кулинарная книга:')
pprint(book, width=150, sort_dicts=False)

# Задача №2
print('-'*100)
list_dishes = ['Омлет', 'Фахитос']
persons = 7
ingredients = get_shop_list_by_dishes(list_dishes, persons)
print(f'Для приготовления: {", ".join(list_dishes).lower()}\nНа {persons} персон необходимо:')
pprint(ingredients, width=150, sort_dicts=False)
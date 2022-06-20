import os

def united_dict(path_to_catol: str) -> dict:
    file_dict = {}  
    for root, dirs, files in os.walk(path_to_catol):         
        for file in files:
            count = 0 
            all_text = ""  
            with open(os.path.join(root,file), encoding='utf-8') as text:
                    for line in text:
                        count += 1
                        all_text += line
                    file_dict[file] = (count, all_text)
    print(f'- текстовые файлы из каталога "{work_catolog}" объединены\n')
    return file_dict 

def sorted_dict(dictionary: dict) -> dict:
    sorted_tuple = sorted(dictionary.items(), key=lambda x: x[1])
    print('- файлы отсортированы по количеству строк\n')
    return dict(sorted_tuple)

def creat_file(sort_dict: dict):
    with open("result_sorted.txt", 'w+', encoding='utf-8') as text:
        for key in sort_dict:
            text.write(key)
            text.write('\n')
            text.write(str(sort_dict[key][0]))
            text.write('\n')
            text.write(sort_dict[key][1])
            text.write('\n')
    print('- создан файл "result_sorted.txt" с отсортированными данными\n')


work_catolog = 'sorted'
path_to_catologist = os.path.join(os.getcwd(), work_catolog)

unit_dict = united_dict(path_to_catologist)
sort_dict = sorted_dict(unit_dict)
creat_file(sort_dict)





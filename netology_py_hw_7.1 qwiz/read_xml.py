import xml.etree.ElementTree as ET
import collections


def read_xml(file_path, max_len_word=6, top_words=10):
    # создать обьект парсера и указать верную кодировку
    parser = ET.XMLParser(encoding='utf-8')
    # прочитать DOM-дерево документа
    tree = ET.parse(file_path, parser)
    # получить корневой элемент дерева
    root = tree.getroot()

    # название тега (на примере корневого элем)
    print("название корневого тега:", root.tag)

    # получение атрибутов тега
    print('получение атрибутов тега:', root.attrib)

    # текст внутри тега
    print('текст внутри тега:', root.text)

    description_words = []
    # поиск всех элем с помощью xpath
    xml_items = root.findall('channel/item')
    for xmli in xml_items:
        print(xmli.find('description').text)
        print('-'*30)

        description = [word for word in xmli.find('description').text.split(' ') if len(word) > max_len_word]
        description_words.extend(description)
        counter_words = collections.Counter(description_words)
    print(counter_words.most_common(top_words))


if __name__ == '__main__':
    read_xml('newsafr.xml')
    
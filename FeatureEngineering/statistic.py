from config import *


def get_item_category_list_info(data, column_name):
    '''
    用作item_category_list、item_property_list
    :param data: 
    :param column_name: 
    :return: 
    '''
    max_item_num = 0
    item_set = set()
    for item in data[column_name]:
        items = item.split(";")
        item_set = item_set | set(items)
        cur_len = len(items)
        max_item_num = cur_len if cur_len > max_item_num else max_item_num
    print(max_item_num, len(item_set))


def get_predict_category_property_info(data, column_name):
    max_item_num = 0
    category_set = set()
    property_set = set()
    for item in data[column_name]:
        items = item.split(";")
        for element in items:
            content = element.split(":")
            category, properties = content[0], content[1]
            property_set = property_set | set(properties.split(','))
            category_set.add(category)
        cur_len = len(items)
        max_item_num = cur_len if cur_len > max_item_num else max_item_num

    print(max_item_num, len(category_set), len(property_set))






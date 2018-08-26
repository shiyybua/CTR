from config import *


def _one_hot():
    '''
    部分数据量级较大，sklearn不在支持。
    :return: 
    '''
    pass


def process_item_category_list(data):
    category_0 = []
    category_1 = []
    enc = OneHotEncoder()
    for item in data['item_category_list']:
        items = item.split(";")
        category_0.append(int(items[0]))
        if len(items) >= 2:
            category_1.append(int(items[1]))
        else:
            category_1.append(-1)
    del data['item_category_list']
    print(len(set(category_1)))
    # one_hot_category_0 = enc.fit_transform(category_0)
    # one_hot_category_1 = enc.fit_transform(category_1)
    # print(one_hot_category_0)

    return


def process_predict_category_property(data):
    MAX_CATEGORY_NUM = 8
    category_properties = [None] * 8
    categories = []
    for item in data['predict_category_property']:
        items = item.split(";")
        for i, element in enumerate(items):
            if i > MAX_CATEGORY_NUM:
                break
            content = element.split(":")
            try:
                category, properties = content[0], content[1]
                categories.append(category)
                for e in properties.split(','):
                    pass
            except IndexError:
                pass


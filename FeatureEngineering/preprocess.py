from config import *


def read_data_from_csv():
    data = pd.read_csv(TRAIN_DATA, delimiter=" ")
    data[['is_trade']] = data[['is_trade']].astype(int)
    return data


def get_max_category_num(data, column_name, delimiter):
    max_item_num = 0
    for item in data[column_name]:
        items = item.split(delimiter)
        cur_len = len(items)
        max_item_num = cur_len if cur_len > max_item_num else max_item_num

    print(max_item_num)


def get_max_category_cnt(data, column_name):
    container = set()
    for item in data[column_name]:
        container.add(item)
    return len(container)


def feature_one_hot_encode(data, column_name):
    container = set()
    for item in data[column_name]:
        container.add(item)
    feature_cnt = len(container)
    one_hot = tf.one_hot(data[column_name], feature_cnt)
    return one_hot


def feature_label_encode(data, column_name):
    one_hot = LabelEncoder().fit_transform(data[column_name])
    print(one_hot)


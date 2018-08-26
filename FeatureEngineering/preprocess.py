from config import *


def read_data_from_csv():
    data = pd.read_csv(TRAIN_DATA, delimiter=" ")
    data[['is_trade']] = data[['is_trade']].astype(int)
    return data


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


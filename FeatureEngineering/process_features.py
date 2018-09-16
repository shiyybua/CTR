from config import *
import pandas as pd
from collections import defaultdict
import numpy as np


def _one_hot(column):
    '''
    部分数据量级较大，sklearn不支持，自定义one hot
    :return: 
    '''
    num_col = len(set(column))
    cur_position = 0
    feature_position = {}
    one_hot_result = []
    for e in column:
        one_hot_encoder = [0] * num_col
        if e not in feature_position.keys():
            one_hot_encoder[cur_position] = 1
            one_hot_result.append(one_hot_encoder)
            feature_position[e] = cur_position
            cur_position += 1
        else:
            one_hot_encoder[feature_position.get(e)] = 1
            one_hot_result.append(one_hot_encoder)
    return one_hot_result, feature_position


def _multi_column_one_hot(all_items):
    '''
        针对多行做one-hot
    :return: 
    '''
    pass


def _concat_two_one_hot(element_1, element_2):
    merge = []
    one_hot_length = 0
    assert len(element_1) == len(element_2)
    for e1, e2 in zip(element_1, element_2):
        merge.append(e1 + e2)
        one_hot_length = len(merge[0])
    return merge, one_hot_length


def process_item_category_list(data):
    '''
    one-hot 处理，根据事前的分布决定只取前2个category
    :param data: 
    :return: 
    '''
    category_0 = []
    category_1 = []
    for item in data['item_category_list']:
        items = item.split(";")
        category_0.append(int(items[0]))
        if len(items) >= 2:
            category_1.append(int(items[1]))
        else:
            category_1.append(-1)
    del data['item_category_list']
    one_hot_category_0, _ = _one_hot(category_0)
    one_hot_category_1, _ = _one_hot(category_1)
    concat_one_hots, one_hot_length = _concat_two_one_hot(one_hot_category_0, one_hot_category_1)
    item_category_list_one_hots = pd.DataFrame(concat_one_hots,
                                               columns=['item_category_list_%d' % i for i in range(one_hot_length)])
    data = pd.concat([data, item_category_list_one_hots], axis=1)

    return data


def item_property_list(data):
    '''
        直接使用one-hot相加
    :param data: 
    :return: 
    '''
    properties = []
    for item in data['item_property_list']:
        items = item.split(";")
        properties += items
    _, feature_position = _one_hot(properties)
    data_one_hot = []
    for item in data['item_property_list']:
        one_hot_model = [0] * len(feature_position)
        items = item.split(";")
        for e in items:
            one_hot_model[feature_position.get(e)] = 1
        data_one_hot.append(one_hot_model)

    del data['item_property_list']
    item_property_list_one_hots = pd.DataFrame(data_one_hot,
                                               columns=['item_property_list%d' % i for i in range(len(feature_position))])
    data = pd.concat([data, item_property_list_one_hots], axis=1)
    return data


def process_predict_category_property(data):
    MAX_CATEGORY_NUM = 8
    category_properties = [None] * 8
    category_to_properties = defaultdict(set)
    categories = []
    for item in data['predict_category_property']:
        items = item.split(";")
        for i, element in enumerate(items):
            if i > MAX_CATEGORY_NUM:
                break
            content = element.split(":")
            category, properties = content[0], content[1]
            categories.append(category)
            for e in properties.split(','):
                category_to_properties[category].add(e)

    one_hot_category, _ = _one_hot(categories)


def category_features_embedding(data, embedding_features, embedding_size):
    '''
    建立、初始化embedding。
    :param data: 
    :return: 
    '''
    feature_embedding = {}
    for feature in embedding_features:
        category_feature = data[feature]
        category_feature = np.asarray(category_feature)
        feature_size = len(set(category_feature))
        embeddings = np.random.uniform(0, 1, (feature_size, embedding_size))

        feature_embedding[feature] = tf.get_variable("%s_embeddings" % feature, dtype=tf.float32,
                               shape=[feature_size, embedding_size],
                               initializer=tf.constant_initializer(embeddings), trainable=True)

    return feature_embedding


def continuous_features_normalization(data):
    '''
    连续型变量normalization
    :param data: 
    :return: 
    '''
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def avg(x, max, min):
        assert (max != min)
        return (x - min) / (max - min)

    for feature in continuous_features:
        data[feature] = data[feature].apply(avg, **{'max':data[feature].max(), 'min':data[feature].min()})

    return data


def remove_used_feature(data):
    remove_features = category_more_features + category_less_features + never_used_feature
    for feature in remove_features:
        data.pop(feature)

    return data


if __name__ == '__main__':
    category_features_embedding(_, category_more_features, category_more_features_embedding_size)
    print(_one_hot([1,2,3,1]))
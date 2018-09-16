from FeatureEngineering import preprocess, statistic, process_features
from Utils import uilt
from config import *


def _statistic():
    statistic.get_item_category_list_info(data, "item_category_list")
    statistic.get_item_category_list_info(data, "item_property_list")
    statistic.get_predict_category_property_info(data, "predict_category_property")


if __name__ == '__main__':
    data = preprocess.read_data_from_csv()
    # 这种类型的用one-hot求和的方式去做。
    data = process_features.process_item_category_list(data)
    data = process_features.item_property_list(data)
    category_features_embedding = process_features.category_features_embedding(data, category_more_features,
                                                      category_more_features_embedding_size)
    category_less_features_embedding = process_features.category_features_embedding(data, category_less_features,
                                                      category_less_features_embedding_size)
    # dict: key是feature name，value是对应的embedding(shape=[feature_size, embedding_size])
    category_features_embedding.update(category_less_features_embedding)
    data = process_features.remove_used_feature(data)
    data = process_features.continuous_features_normalization(data)
    uilt.save_dataframe_to_dick(data)





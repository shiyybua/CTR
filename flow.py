from FeatureEngineering import preprocess, statistic, process_features
import numpy as np


def _statistic():
    statistic.get_item_category_list_info(data, "item_category_list")
    statistic.get_item_category_list_info(data, "item_property_list")
    statistic.get_predict_category_property_info(data, "predict_category_property")


if __name__ == '__main__':
    data = preprocess.read_data_from_csv()
    # 这种类型的用one-hot求和的方式去做。
    data = process_features.process_item_category_list(data)
    data = process_features.item_property_list(data)
    process_features.category_more_features_embedding(data)

    # print(np.asarray(data))
    # process_features.process_predict_category_property(data)




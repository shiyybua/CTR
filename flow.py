from FeatureEngineering import preprocess, statistic


if __name__ == '__main__':
    data = preprocess.read_data_from_csv()
    # 这种类型的用one-hot求和的方式去做。
    statistic.get_item_category_list_info(data, "item_category_list")
    statistic.get_predict_category_property_info(data, "predict_category_property")




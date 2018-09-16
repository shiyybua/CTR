import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf



TRAIN_DATA = 'data/mini'
PROCESSED_DATA_PATH = 'data/processed_data.txt'

'''
    数据特征分为3类：
        1. 类别较多的型特征。=》 embedding
        2. 连续型特征。   =》normalization
        3. 类别较少的特征。 =》less embedding, no pooling for saving more information.
'''
continuous_features = ['item_price_level', 'item_sales_level',
                       'item_collected_level', 'item_pv_level', 'user_age_level', 'user_star_level',
                       'context_timestamp','shop_review_num_level','shop_review_positive_rate','shop_star_level'
                       ,'shop_score_service', 'shop_score_delivery', 'shop_score_description']

category_more_features = ['item_id', 'context_id', 'shop_id', 'item_brand_id']

category_less_features = ['is_trade', 'item_city_id', 'user_gender_id', 'user_occupation_id',
                          'context_page_id']

never_used_feature = ['instance_id', 'user_id']

category_more_features_embedding_size = 256
category_less_features_embedding_size = 8


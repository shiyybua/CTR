from config import *


def _get_bucket_info(value, bucket, info):
    for i in range(0, len(bucket) - 1):
        if bucket[i] <= value < bucket[i + 1]:
            info[(bucket[i], bucket[i + 1])] = info.get((bucket[i], bucket[i + 1]), 0) + 1
            break
    if value >= bucket[-1]:
        info[(bucket[-1], 666666)] = info.get((bucket[-1], 666666), 0) + 1


def _print_bucket_info(info):
    for v_range, value in info.items():
        print("%d - %d: " % v_range, value)


def get_item_category_list_info(data, column_name, item_bucket=[1,2,3]):
    '''
    用作item_category_list、item_property_list
    :param data: 
    :param column_name: 
    :return: 
    '''
    max_item_num = 0
    item_set = set()
    bucket_info = {}
    for i, item in enumerate(data[column_name]):
        items = item.split(";")
        for e in items:
            item_set.add(e)
        # item_set = item_set | set(items) 这个操作效率太低
        cur_len = len(items)
        max_item_num = cur_len if cur_len > max_item_num else max_item_num
        _get_bucket_info(cur_len, item_bucket, bucket_info)

    print("max item length: %d,"%max_item_num, "max cnt: %d,"%len(item_set))

    _print_bucket_info(bucket_info)


def get_predict_category_property_info(data, column_name, item_bucket=[1,9,13,14]):
    max_item_num = 0
    category_set = set()
    property_set = set()
    bucket_info = {}
    for item in data[column_name]:
        items = item.split(";")
        for element in items:
            content = element.split(":")
            try:
                category, properties = content[0], content[1]
                for e in properties.split(','):
                    property_set.add(e)
                category_set.add(category)
            except IndexError:
                pass
        cur_len = len(items)
        max_item_num = cur_len if cur_len > max_item_num else max_item_num
        _get_bucket_info(cur_len, item_bucket, bucket_info)

    print("max item length: %d," % max_item_num,
          "max category cnt: %d," % len(category_set),
          "max property cnt: %d" % len(property_set))
    _print_bucket_info(bucket_info)






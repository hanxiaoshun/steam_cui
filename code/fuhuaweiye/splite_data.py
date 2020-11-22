email_data = [['NSF202006107', '佳电（上海）管理有限公司', '20-43-Q-0127  20-43-Q-0128  ', '商志松', '13523866009',
               '佳电自提河南省新乡市红旗区高新区新飞大道1789号高新区火炬园内H2座2楼2008室', ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '陈昱钢4919,', '73044679'],
              ['NSF202005781', '丹东市安全局', ' 20-45-Q-0485', '刘昱彤', '13898117239', '汇志自提辽宁省沈阳市和平区三好街物产大厦1010室',
               '备注信息：|.发货时效：正常.', '孙鑫14286,', '73044503'],
              ['NSF202005330', '北京汇志凌云数据技术有限责任公司',
               '20-44-LY-0107  20-44-LY-0108  20-44-LY-0109  20-44-LY-0110  20-44-LY-0111', '吴亮亮', '17633859385',
               '汇志自提河北省沧州市任丘市河北省任丘市中华西路红苹果双语幼儿园南侧津石高速机电项目部', ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '王晓强14101,', '73044293']]


def splite_data(email_data=[[]]):
    '''
    处理异常字符
    :param email_data:
    :return:
    '''
    email_data_by_serial_number = []
    if len(email_data) > 0:
        for data in email_data:
            data_serial_numbers = data[2].strip().split('  ')
            if len(data_serial_numbers) > 0:
                for serial_number in data_serial_numbers:
                    data[2] = serial_number
                    email_data_by_serial_number.append([j for j in data])
            else:
                email_data_by_serial_number.append(data)
                print(data)
    print(email_data_by_serial_number)
    return email_data_by_serial_number


need_merge_data_sample = [
    ['NSF202005778', '佳电（上海）管理有限公司', '20-45-L-0648', '马林平', '13701409901', '佳电自提江苏省南京市秦淮区汉中路1号国际金融中心32层AJ',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '石磊3292,', '73044515'],
    ['NSF202005904', '国家电投集团江苏电力有限公司', '20-43-Q-0138', '叶海瑞', '17751563112', '佳电自提江苏省盐城市亭湖区解放南路58号中建大厦国电投盐城',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '彭飞1958,', '73044565'],
    ['NSF202005495', '中国移动通信集团广东有限公司', '20-46-0329', '李翔宇', '13802882140', '广东省广州市天河区全球通大厦',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '李盛豪11571,', '73044585'],
    ['NSF202005495', '中国移动通信集团广东有限公司', '20-46-0330', '李翔宇', '13802882140', '广东省广州市天河区全球通大厦',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '李盛豪11571,', '73044585'],
    ['NSF202005495', '中国移动通信集团广东有限公司', '20-46-0331', '李翔宇', '13802882140', '广东省广州市天河区全球通大厦',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '李盛豪11571,', '73044585'],
    ['NSF202005495', '中国移动通信集团广东有限公司', '20-46-0332', '李翔宇', '13802882140', '广东省广州市天河区全球通大厦',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '李盛豪11571,', '73044585'],
    ['NSF202005495', '中国移动通信集团广东有限公司', '20-46-0333', '李翔宇', '13802882140', '广东省广州市天河区全球通大厦',
     ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '李盛豪11571,', '73044585']]


def merge_data(data=None):
    if data is None:
        data = []
    tmp_order = ''
    merge_data_dict = {
        # 'tmp_order': {'tmp_start_row': i, 'tmp_start_col': j, 'tmp_end_row': ii, 'tmp_end_col': jj}
    }

    if len(data) > 0:
        for i in range(0, len(data)):
            # row
            for j in range(0, len(data[i])):
                # col
                if j == 0:
                    if tmp_order != data[i][j]:
                        merge_data_dict[data[i][j]] = {'tmp_start_row': i, 'tmp_start_col': j}
                        if i > 0:
                            merge_data_dict[data[i][j]] = {
                                # 'tmp_start_row': merge_data_dict[data[i - 1][j]]['tmp_start_row'] + 1,
                                'tmp_start_row': i,
                                'tmp_start_col': j
                            }
                            if merge_data_dict[data[i - 1][j]]:
                                merge_data_dict[data[i - 1][j]].update({'tmp_end_row': (i - 1), 'tmp_end_col': j})
                    else:
                        pass
    start_row_remember = []
    for k, v in merge_data_dict.items():
        print(v['tmp_start_row'])
        start_row_remember.append(v['tmp_start_row'])
    print(merge_data_dict)
    print(start_row_remember)
    return merge_data_dict, start_row_remember


merge_data(data=need_merge_data_sample)

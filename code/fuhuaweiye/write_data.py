import os
import time
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

date_time_str = str(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
data = [['NSF202006107', '佳电（上海）管理有限公司', '20-43-Q-0127  20-43-Q-0128  ', '商志松', '13523866009',
         '佳电自提河南省新乡市红旗区高新区新飞大道1789号高新区火炬园内H2座2楼2008室', ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '陈昱钢4919,', '73044679'],
        ['NSF202005781', '丹东市安全局', ' 20-45-Q-0485  ', '刘昱彤', '13898117239', '汇志自提辽宁省沈阳市和平区三好街物产大厦1010室',
         '备注信息：|.发货时效：正常.', '孙鑫14286,', '73044503'],
        ['NSF202005330', '北京汇志凌云数据技术有限责任公司',
         '  20-44-LY-0107  20-44-LY-0108  20-44-LY-0109  20-44-LY-0110  20-44-LY-0111  ', '吴亮亮', '17633859385',
         '汇志自提河北省沧州市任丘市河北省任丘市中华西路红苹果双语幼儿园南侧津石高速机电项目部', ' 报关方式：一般贸易报关.备注信息：|.发货时效：正常.', '王晓强14101,', '73044293']]


def write2excel(data, path='excel/', filename_prefix='/fuhuaweiye_order_'):
    """
    写excel
    :param data:
    :param path:
    :param filename_prefix:
    :return:
    """
    try:
        filename = path + filename_prefix + date_time_str + '.xlsx'
        if os.path.exists(path):
            if len(os.listdir(path)) > 0:
                for file in os.listdir(path):
                    os.remove(os.path.join(path, file))
        else:
            os.makedirs(path)

        # 保存数据
        with pd.ExcelWriter(filename) as writer:  # doctest: +SKIP
            pd.DataFrame(data).to_excel(writer, sheet_name='order', index=True, header=0, na_rep='')
        return filename
    except Exception as make_excel_e:
        # input("make_excel 发生异常：" + str(make_excel_e))
        logger = 'logger'
        if os.path.exists(logger):
            if len(os.listdir(logger)) > 0:
                for file in os.listdir(logger):
                    os.remove(os.path.join(logger, file))
        else:
            os.makedirs(logger)
        with open(logger + filename_prefix + '_error.txt', 'a', encoding='utf-8') as f_err:
            f_err.write(date_time_str + ":make_excel 发生异常：" + str(make_excel_e))
        # input("发生异常请记录一下错误并按任意键退出！")
        raise make_excel_e


# write2excel(data)

# import motor
import motor.motor_asyncio
from pymongo import MongoClient
import pprint
import time


class MainMongodb(object):
    """
    mongodbUtil
    """

    def __init__(self, host, port, username=None, password=None, database=None):
        """
        初始化
        :param host:
        :param port:
        :param username:
        :param password:
        :param database:
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        pass

    def async_create_or_connect_mongodb(self):
        """
        返回数据库实例
        同步与异步两种方式
        :return:
        """
        try:
            # client = pymongo.MongoClient(host=host, port=port)
            # client = motor.motor_asyncio.AsyncIOMotorClient()
            # client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
            # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
            # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')
            # conn_url = 'mongodb://mongodb0.example.com:27017'
            # conn_url = 'mongodb://mongodb0.example.com:27017/admin'
            conn_url = 'mongodb://' + self.username + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database
            db = motor.motor_asyncio.AsyncIOMotorClient(conn_url)
            return db
            # return motor.motor_asyncio.AsyncIOMotorClient(host=host, port=port)
        except Exception as e:
            raise str(e)

    def create_or_connect_mongodb(self):
        """
        返回数据库实例、同步
        :return:
        """
        try:
            # client = MongoClient(self.host, self.port)
            client = MongoClient(host=self.host,
                                 port=self.port,
                                 username=self.username,
                                 password=self.password,
                                 authSource=self.database,
                                 authMechanism='SCRAM-SHA-256')

            return client.GD
            # return motor.motor_asyncio.AsyncIOMotorClient(host=host, port=port)
        except Exception as e:
            raise str(e)

    def create_or_connect_mongodb_without_auth(self):
        """
        返回数据库实例、同步
        :return:
        """
        try:
            client = MongoClient(self.host, self.port)
            return client.wadb
            # return motor.motor_asyncio.AsyncIOMotorClient(host=host, port=port)
        except Exception as e:
            raise str(e)

    def get_collection(self, collection_name):
        """
        返回输入的名称对应的集合
        :param collection_name:
        :return:
        """
        dbm = self.create_or_connect_mongodb()
        if collection_name == 'sms_tracking':
            collection = dbm.sms_tracking
            return collection

    def get_collection_without_auth(self, collection_name):
        """
        返回输入的名称对应的集合
        :param collection_name:
        :return:
        """
        dbm = self.create_or_connect_mongodb_without_auth()
        if collection_name == 'sms_tracking':
            collection = dbm.sms_tracking
            return collection
        elif collection_name == 'registry_tracking':
            collection = dbm.registry_tracking
            return collection
        elif collection_name == 'code_tracking':
            collection = dbm.code_tracking
            return collection
        elif collection_name == 'account_tracking':
            collection = dbm.account_tracking
            return collection
        elif collection_name == 'proxy_tracking':
            collection = dbm.proxy_tracking
            return collection

    def find_one(self, collection, **kwargs):
        """
        按条件查询单个doc,如果传入集合为空将返回默认数据
        :param collection:
        :param kwargs:
        :return:
        """
        result_obj = collection.find_one(kwargs)
        return result_obj

    def find_all(self, collection, sort=-1, limit=None, skip=0):
        """
        查询传入条件集合和全部数据
        :return:
        """
        # cursor = collection.find().sort('i').limit(1000).skip(2)
        # cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
        # for document in cursor.to_list(length=None):
        #     pprint.pprint(document)
        #
        # return collection.find().sort('i')
        cursor = collection.find()
        # cursor.sort('i', sort).skip(skip).limit(limit)  # 排序将消耗巨大性能所以不建议在大批量导出的情况下进行排序
        cursor.skip(skip).limit(limit)
        # for document in cursor.to_list(length=100):
        #     pprint.pprint(document)

        # for document in cursor:
        #     pprint.pprint(document)
        return cursor
        # return cursor.to_list(length=None)

    def find_conditions(self, collection, limit=0, **kwargs):
        """
        按条件查询，并做返回条数限制
        :param collection:
        :param limit:
        :param kwargs:
        :return:
        """
        # return collection.find(kwargs).limit(limit)
        if limit == 0:
            # cursor = collection.find(kwargs).sort('i').skip(0)
            cursor = collection.find(kwargs).skip(0)
        else:
            cursor = collection.find(kwargs).sort('i').limit(limit).skip(0)
        return cursor

    def count(self, collection, **kwargs):
        """
        返回查询的条数
        :param collection:
        :param kwargs:
        :return:
        """
        n = collection.count_documents(kwargs)
        # n = db.test_collection.count_documents({'i': {'$gt': 1000}})
        print('%s documents in collection' % n)
        return n

    def replace_id(self, collection, new_doc, **kwargs):
        """
        通过ID进行更新
        :param collection:
        :param condition:
        :param new_doc:
        :return:
        """
        _id = kwargs['_id']
        old_document = collection.find_one(kwargs)
        if old_document:
            result = collection.replace_one({'_id': _id}, new_doc)
            print('replaced %s document' % result.modified_count)
            new_document = collection.find_one({'_id': _id})
            # print('document is now %s' % pprint.pformat(new_document))
            return {'status': 'ok', 'info': str(_id) + ':: replace ok !!!'}
        else:
            return {'status': 'fail', 'info': str(_id) + ':: not exist !!!'}

    def update(self, collection, new_doc, **kwargs):
        """
        进行替换部分内容
        :param collection:
        :param condition:
        :param new_part:
        :return:
        """
        result = collection.update_one(kwargs, {'$set': new_doc})
        print('updated %s document' % result.modified_count)
        new_document = collection.find_one(kwargs)
        print('document is now %s' % pprint.pformat(new_document))

    def replace(self, collection, new_doc, **kwargs):
        """
        分步骤通过一定条件进行替换部分内容
        :param collection:
        :param condition:
        :param new_doc:
        :return:
        """
        old_document = collection.find_one(kwargs)
        _id = old_document['_id']
        result = collection.replace_one({'_id': _id}, new_doc)
        print('replaced %s document' % result.modified_count)
        new_document = collection.find_one({'_id': _id})
        print('document is now %s' % pprint.pformat(new_document))

    def update_many(self, collection, new_doc, **kwargs):
        """
        批量更新
        :param collection:
        :param condition:
        :param new_doc:
        :return:
        """
        # result4 = collection.update_many({'i': {'$gt': 100}}, {'$set': {'key': 'value'}})
        result = collection.update_many(kwargs, {'$set': new_doc})
        print('updated %s document' % result.modified_count)

    def insert_one(self, collection, new_doc):
        """
        单条插入
        :param collection:
        :param new_doc:
        :return:
        """
        try:
            result = collection.insert_one(new_doc)
            print('inserted_id %s' % repr(result.inserted_id))
            return 'ok'
        except Exception as e:
            return str(e)

    def insert_many(self, collection, new_doc):
        """
        批量添加
        :param collection:
        :param need_insert_dict_many:
        :return:
        """
        try:
            result = collection.insert_many(new_doc)
            print('inserted %d docs' % (len(result.inserted_ids),))
            return 'ok'
        except Exception as e:
            return str(e)

    def delete_many(self, collection, **kwargs):
        """
        批量删除
        :param collection:
        :param kwargs:
        :return:
        """
        # print('%s documents before calling delete_many()' % n)
        n_beforce = collection.count_documents({})
        print('%s documents before calling delete_many()' % n_beforce)
        # result4 = collection.delete_many({'i': {'$gte': 1000}})
        # result = collection.delete_many(kwargs)
        collection.delete_many(kwargs)
        # print(result.exit_code)
        n_after = collection.count_documents({})
        print('%s documents after calling delete_many()' % n_after)
        return n_beforce, n_after

    def sms_tracking(self,
                     sms_tracking,
                     sms_platform,
                     user,
                     password,
                     date_time_str,
                     pid,
                     cc,
                     mcc,
                     mnc,
                     cc_mcc_mnc,
                     nation_short_name_str,
                     login_status, login_token,
                     number_str,
                     number_status,
                     number_msg,
                     login_money,
                     verify_code,
                     verify_status):
        """
        接码平台的信息
        """
        new_doc = {'sms_platform': sms_platform,
                   'user': user,
                   'password': password,
                   'start_time': date_time_str,
                   'pid': pid,
                   'cc': cc,
                   'mcc': mcc,
                   'mnc': mnc,
                   'cc_mcc_mnc': cc_mcc_mnc,
                   'nation_short_name_str': nation_short_name_str,
                   'login_status': login_status,
                   'login_token': login_token,
                   'login_money': login_money,
                   'number_str': number_str,
                   'number_status': number_status,
                   'number_msg': number_msg,
                   'verify_code': verify_code,
                   'verify_status': verify_status,
                   'insert_time': str(time.strftime(
                       '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(sms_tracking, new_doc)

    def code_tracking(self, code_tracking, date_time_str,
                      cc,
                      number_str,
                      device_info,
                      code_cmd, code_params, code_response,
                      code_status):
        """
        短信验证码跟踪
        :param cmd_tracking:
        :param date_time_str:
        :param cc:
        :param number_str:
        :param device_info:
        :param code_cmd:
        :param code_params:
        :param code_response:
        :param code_status:
        :return:
        """
        new_doc = {'start_time': date_time_str,
                   'cc': cc,
                   'number_str': number_str,
                   'device_info': device_info,
                   'code_cmd': code_cmd,
                   'code_params': code_params,
                   'code_response': code_response,
                   'code_status': code_status,
                   'insert_time': str(time.strftime(
                       '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(code_tracking, new_doc)

    def registry_tracking(self, registry_tracking,
                          date_time_str, cc, number_str,
                          reg_cmd, reg_params, reg_response,
                          reg_status):
        """
        注册信息跟踪
        :param registry_tracking:
        :param date_time_str:
        :param cc:
        :param number_str:
        :param reg_cmd:
        :param reg_params:
        :param reg_response:
        :param reg_status:
        :return:
        """
        if "+" in number_str:
            number_str = str(number_str).replace('+', '')
            new_doc = {'start_time': date_time_str,
                       'cc': cc,
                       'number_str': number_str,
                       'number_full': number_str,
                       'reg_cmd': reg_cmd,
                       'reg_params': reg_params,
                       'reg_response': reg_response,
                       'reg_status': reg_status,
                       'reg_account': '',
                       'reg_pri_key': '',
                       'reg_pub_key': '',
                       'pushname': '',
                       'insert_time': str(time.strftime(
                           '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        else:
            new_doc = {'start_time': date_time_str,
                       'cc': cc,
                       'number_str': number_str,
                       'number_full': cc + number_str,
                       'reg_cmd': reg_cmd,
                       'reg_params': reg_params,
                       'reg_response': reg_response,
                       'reg_status': reg_status,
                       'reg_account': '',
                       'reg_pri_key': '',
                       'reg_pub_key': '',
                       'pushname': '',
                       'insert_time': str(time.strftime(
                           '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(registry_tracking, new_doc)

    def registry_tracking_before_code(self, registry_tracking,
                                      date_time_str, cc, number_str, reg_account):
        """
        注册信息跟踪
        """
        new_doc = {'start_time': date_time_str,
                   'cc': cc,
                   'number_str': number_str,
                   'number_full': reg_account,
                   'reg_cmd': '',
                   'reg_params': '',
                   'reg_response': '',
                   'reg_status': 'fail',
                   'reg_account': reg_account,
                   'reg_pri_key': '',
                   'reg_pub_key': '',
                   'pushname': '',
                   'insert_time': str(time.strftime(
                       '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(registry_tracking, new_doc)

    def registry_tracking_final(self, registry_tracking, reg_account, reg_response, reg_status):
        """
        注册信息跟踪
        """
        new_doc = {'start_time': '',
                   'cc': '',
                   'number_str': '',
                   'number_full': '',
                   'reg_cmd': '',
                   'reg_params': '',
                   'reg_response': reg_response,
                   'reg_status': reg_status,
                   'reg_account': reg_account,
                   'reg_pri_key': '',
                   'reg_pub_key': '',
                   'pushname': '',
                   'insert_time': str(time.strftime(
                       '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(registry_tracking, new_doc)

    def account_tracking(self, account_tracking,
                         date_time_str,
                         reg_account,
                         reg_pri_key,
                         reg_pub_key,
                         pushname):
        new_doc = {'start_time': date_time_str,
                   'reg_account': reg_account,
                   'reg_pri_key': reg_pri_key,
                   'reg_pub_key': reg_pub_key,
                   'pushname': pushname,
                   'insert_time': str(time.strftime(
                       '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(account_tracking, new_doc)

    def proxy_tracking(self, proxy_tracking, date_time_str, proxy_type, proxy_model, proxy_account, proxy_pwd):
        new_doc = {'proxy_type': proxy_type,
                   'proxy_model': proxy_model,
                   'proxy_account': proxy_account,
                   'proxy_pwd': proxy_pwd,
                   'patch_count': 0,
                   'apply_count': 0,
                   'insert_time': str(time.strftime(
                       '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))}
        self.insert_one(proxy_tracking, new_doc)


if __name__ == '__main__':
    mm = MainMongodb('127.0.0.1', 27017)
    mm.create_or_connect_mongodb_without_auth()
    sms_tracking = mm.get_collection_without_auth("sms_tracking")
    mm.insert_one(sms_tracking, {"name": 'ss'})
    kargs = {"name": 'ss'}
    print(mm.delete_many(sms_tracking, **kargs))

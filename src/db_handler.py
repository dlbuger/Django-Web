import pymysql as ps
import pandas as pd
from typing import Dict, List, Tuple
import warnings
import re


sql = ps.connections.Connection(
    host='localhost', user='reco', password='0711', database='Test')
# 人工成本 = pd.read_sql("SELECT * FROM 人工成本", sql)
# 员工 = pd.read_sql("SELECT * FROM 员工", sql)
# 实际成本 = pd.read_sql("SELECT * FROM 实际成本", sql)
# 项目 = pd.read_sql("SELECT * FROM 项目", sql)
# 预算成本 = pd.read_sql("SELECT * FROM 预算成本", sql)




class SearchBackend:
    @staticmethod
    def hint():
        pass

    @staticmethod
    def search_by_employee(id):
        query = f'''
            SELECT 员工.员工号, 姓名, 部门, 单位人工, 合同号, 预算人工, 实际人工, 修正1, 修正2, 修正3\
            FROM 人工成本, 员工
            WHERE 人工成本.员工号 = 员工.员工号 AND 员工.员工号={id};
            '''
        df = pd.read_sql(query, sql).to_dict('records')[0]
        return df


    @staticmethod
    def search_by_contract(id):
        query1 = f"""
            SELECT 合同号, 项目名称, 预计开始日期, 预计结束日期, 实际开始日期, 实际结束日期
            FROM 项目
            WHERE 合同号 = '{id}';
        """
        query2 = f"""
            SELECT 硬件成本, 软件成本, 差旅成本, 集成成本, 施工成本
            FROM 预算成本
            WHERE 合同号 = '{id}';
        """
        query3 = f"""
            SELECT 硬件成本, 软件成本, 差旅成本, 集成成本, 施工成本
            FROM 实际成本
            WHERE 合同号 = '{id}';
        """
        项目 = pd.read_sql(query1, sql).to_dict('records')[0]
        
        预算成本 = pd.read_sql(query2, sql)
        预算成本.columns=['预算硬件成本','预算软件成本', '预算差旅成本', '预算集成成本', '预算施工成本']
        预算成本 = 预算成本.to_dict('records')[0]

        实际成本 = pd.read_sql(query3, sql)
        实际成本.columns=['实际硬件成本','实际软件成本', '实际差旅成本', '实际集成成本', '实际施工成本']
        实际成本 = 实际成本.to_dict('records')[0]
       
        return {**项目, **预算成本, **实际成本}

    @staticmethod
    def employee_record():

        '''
            返回一个所有员工号的List, 用来判定搜索的id是否存在数据库
        '''

        query = '''
        SELECT 员工号
        FROM 员工
        '''
        return pd.read_sql(query, sql)['员工号'].values

    @staticmethod
    def program_record():
        """
            返回一个所有项目的合同号List, 用来判定搜索id是否存在于数据库
        """

        query = """
            SELECT 合同号
            FROM 项目 
        """
        return pd.read_sql(query,sql)['合同号'].values

def ExceptionHandler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            warnings.warn("执行Query失败\n%s"%str(e))
    return wrapper



class InsertBackend:
    @staticmethod
    def append_program(data: Dict) -> None:
        data = pd.Series(data)
        handler = Handler(sql)
        
        项目待添加 = data[['合同号','项目名称','预计开始日期','预计结束日期', '实际开始日期', '实际结束日期']]
        预算成本待添加 = data[['合同号', '计划硬件成本', '计划软件成本', '计划差旅成本', '计划集成成本', '计划施工成本']]
        预算成本待添加.index=['合同号', '硬件成本', '软件成本','差旅成本','集成成本','施工成本']
        实际成本待添加 = data[['合同号', '实际硬件成本', '实际软件成本', '实际差旅成本', '实际集成成本', '实际施工成本']]
        实际成本待添加.index=['合同号', '硬件成本', '软件成本','差旅成本','集成成本','施工成本']

        handler.INSERT('项目',项目待添加)
        handler.INSERT('预算成本',预算成本待添加)
        handler.INSERT('实际成本',实际成本待添加)
    
    @staticmethod
    def append_employee(data: Dict) -> None:
        data = pd.Series(data)
        handler = Handler(sql)
        员工待添加 = data[['姓名','员工号', '部门', '单位人工']]
        handler.INSERT('员工', 员工待添加)


class Handler:
    """
        传入一个pymysql的Connection对象
        e.g: ps.connections.Connection(
                            host='localhost',
                            user='reco',
                            password='0711',
                            database='Test'
                            )
    """
    def __init__(self,connection: ps.connections.Connection) -> None:
        self.connection = connection

    @ExceptionHandler
    def SELECT(self, table_name: str) -> pd.DataFrame:
        """ 
            Inputs:
                1. table_name <str>: 需要显示Table的名字
            Return:
                pandas.DataFrame
        """
        _query = "SELECT * FROM {table_name}"
        return pd.read_sql(_query, self.connection)
    
    @ExceptionHandler
    def TABLES(self) -> List:
        """ 
            显示当前数据库的所有Table名字
            Inputs:
                None
            Return:
                List[Table Name]
        """
        _query = "SHOW TABLES;"
        with self.connection.cursor() as cursor:
            cursor.execute(_query)
            callback = cursor.fetchall()
        return [x[0] for x in callback]            
    
    # @ExceptionHandler
    def INSERT(self, table_name:str, data:pd.Series) -> None:
        '''
            Inputs:
                1. table_name <str>: 要插入Table的名字  
                2. data <pandas.Series>: 待添加的数据
            Return:
                void

            NOTICE: 单个INSERT
            1. 检查传入的DataFrame的columns长度是否和数据库一直
            2. 检查传入的DataFrame的columns是否和数据库的一直
            3. 检查数据类型是否符合
        '''


        _COLUMNS = data.index.values.tolist()

        VALUES = data.values.tolist()
        COLUMNS = re.sub("\'","",str(tuple(_COLUMNS)))
        print(COLUMNS)

        with self.connection.cursor() as cursor:
            _query = f"INSERT INTO {table_name} {COLUMNS}\
                        VALUES( %s );"%("%s, " * (len(_COLUMNS)-1) + "%s")
            print(_query)
            cursor.execute(_query, VALUES)
        sql.commit()

            




















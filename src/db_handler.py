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
        query = '''
            SELECT 员工.员工号, 姓名, 部门, 单位人工, 合同号, 预算人工, 实际人工, 修正1, 修正2, 修正3\
            FROM 人工成本, 员工
            WHERE 人工成本.员工号 = 员工.员工号;
            '''
        df = pd.read_sql(query, sql)
        return df[df['员工号']==id]


    @staticmethod
    def search_by_contract(id):
        query1 = """
            SELECT 预算成本.合同号,项目名称, 硬件成本,软件成本,差旅成本,集成成本,施工成本,预计开始日期,预计结束日期,实际开始日期,实际结束日期
            FROM 预算成本 LEFT JOIN 项目 ON 预算成本.合同号=项目.合同号
            UNION
            SELECT 预算成本.合同号,项目名称, 硬件成本,软件成本,差旅成本,集成成本,施工成本,预计开始日期,预计结束日期,实际开始日期,实际结束日期
            FROM 项目 RIGHT JOIN 预算成本 ON 预算成本.合同号=项目.合同号;
            """

        query2 = """
            SELECT 实际成本.合同号,项目名称, 硬件成本,软件成本,差旅成本,集成成本,施工成本,预计开始日期,预计结束日期,实际开始日期,实际结束日期
            FROM 实际成本 LEFT JOIN 项目 ON 实际成本.合同号=项目.合同号
            UNION
            SELECT 实际成本.合同号,项目名称, 硬件成本,软件成本,差旅成本,集成成本,施工成本,预计开始日期,预计结束日期,实际开始日期,实际结束日期
            FROM 项目 RIGHT JOIN 实际成本 ON 实际成本.合同号=项目.合同号;
                 """
        return {'预算': pd.read_sql(query1, sql),'实际':pd.read_sql(query2, sql)}

    @staticmethod
    def employee_record():

        '''
            返回一个所有员工号的List, 用来判定搜索的id是否存在数据库
        '''

        query = '''
        SELECT 员工.员工号, 姓名, 部门, 单位人工, 合同号, 预算人工, 实际人工, 修正1, 修正2, 修正3\
        FROM 人工成本, 员工
        WHERE 人工成本.员工号 = 员工.员工号;
        '''
        return pd.read_sql(query, sql)['员工号'].values

def ExceptionHandler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            warnings.warn("执行Query失败\n%s"%e)
    return wrapper



class InsertBackend:
    @staticmethod
    def append_program(data: Dict) -> int:
        data = pd.Series(data)
        handler = Handler(sql)
        
        项目待添加 = data[['合同号','项目名称','计划开始时间','计划结束时间', '实际开始时间', '实际结束时间']]
        预算成本待添加 = data[['合同号', '计划硬件成本', '计划软件成本', '计划差旅成本', '计划集成成本', '计划施工成本']]
        实际成本待添加 = data[['合同号', '实际硬件成本', '实际软件成本', '实际差旅成本', '实际集成成本', '实际施工成本']]
        handler.INSERT('项目',项目待添加)
        handler.INSERT('预算成本',预算成本待添加)
        handler.INSERT('实际成本',实际成本待添加)





    # def append_program(data: Dict) -> int:
    #     data = pd.Series(data)
    #     query_项目待添加 = 'INSERT INTO 项目 (合同号, 项目名称, 预计开始日期, 实际开始日期, 预计结束日期, 实际结束日期) VALUES(%s, %s, %s, %s, %s, %s)'

    #     query_预算成本待添加 = 'INSERT INTO 预算成本 (合同号, 硬件成本, 软件成本, 差旅成本, 集成成本, 施工成本) VALUES(%s, %s, %s, %s, %s, %s)'

    #     query_实际成本带添加 = 'INSERT INTO 实际成本 (合同号, 硬件成本, 软件成本, 差旅成本, 集成成本, 施工成本) VALUES(%s, %s, %s, %s, %s, %s)'
    #     with sql.cursor() as cursor:
    #         cursor.execute(query_项目待添加,项目待添加)
    #         cursor.execute(query_预算成本待添加, 预算成本待添加)
    #         cursor.execute(query_实际成本带添加, 实际成本带添加)
    #     sql.commit()



class Check:
    """
        一些帮出判定数据的Function
    """
    @staticmethod
    @ExceptionHandler
    def checkLength(schema_data: pd.DataFrame, data: pd.Series) -> bool:
        '''
            NOTICE: 只有一个是自曾的情况下
            1. 检查长度是否一样
            2. 如果不一样 判定是否有autoincrement -> 无: 报错
        '''
        if len(schema_data) != len(data.index):
            if "auto_increment" not in schema_data['Extra'].values:
                raise ps.DatabaseError("传入数据的columns长度和Table的columns的长度不匹配,操作终止")
            return False
        return True
                
    @staticmethod
    @ExceptionHandler
    def checkDtype(schema_data: pd.DataFrame, data:pd.DataFrame) -> None:
        """
            判定数据类型是否匹配
        """
        NotImplemented

    @staticmethod
    @ExceptionHandler
    def checkDuplicated(con: ps.connections.Connection, data:pd.DataFrame) -> None:
        """
            判定是否有重复的数据
        """
        NotImplemented


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
    
    @ExceptionHandler
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
        schema = pd.read_sql(f"DESCRIBE {table_name}",self.connection)

        _length = Check.checkLength(schema, data)
        _dtype = Check.checkDtype(schema, data)
        _duplicated = Check.checkDuplicated(self.connection, data)
        if _length:
            _COLUMNS = schema.Field.values.tolist()
        else:
            _COLUMNS = schema.Field.values.tolist()[1:] # AUTO INCREMENT 在第0

        VALUES = data.values.tolist()
        COLUMNS = re.sub("\'","",str(tuple(_COLUMNS)))

        with self.connection.cursor() as cursor:
            _query = f"INSERT INTO {table_name} {COLUMNS}\
                        VALUES( %s );"%("%s, " * (len(_COLUMNS)-1) + "%s")
            cursor.execute(_query, VALUES)
        sql.commit()

            




















import pymysql as ps
import pandas as pd


sql = ps.connections.Connection(
    host='localhost', user='reco', password='0711', database='Test')
人工成本 = pd.read_sql("SELECT * FROM 人工成本", sql)
员工 = pd.read_sql("SELECT * FROM 员工", sql)
实际成本 = pd.read_sql("SELECT * FROM 实际成本", sql)
项目 = pd.read_sql("SELECT * FROM 项目", sql)
预算成本 = pd.read_sql("SELECT * FROM 预算成本", sql)

def hint(): 
    pass

def search_by_employee(id):
    query = '''
        SELECT 员工.员工号, 姓名, 部门, 单位人工, 合同号, 预算人工, 实际人工, 修正1, 修正2, 修正3\
        FROM 人工成本, 员工
        WHERE 人工成本.员工号 = 员工.员工号;
        '''
    df = pd.read_sql(query, sql)
    return df[df['员工号']==id]


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



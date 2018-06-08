#import操控数据库的模块
from sqlalchemy import create_engine
import pandas as pd
#创建引擎，sqlite是操控此类数据库的tool，文件名是Chinook.sqlite
engine=create_engine('sqlite:///Chinook.sqlite')

#基础操作（使用con，con.execute())
'''
#打印这个关系库中的表名
table_names=engine.table_names()
print(table_names)

#连接数据库
con=engine.connect()

#执行操作（从album选取所有的列）
rs=con.execute('SELECT * FROM Album')
#从Customer选取第一列
rs1=con.execute('SELECT 1 FROM Customer')

#将数据导入pandas，形成DataFrame
df=pd.DataFrame(rs.fetchall())
df2=pd.DataFrame(rs1.fetchall())
#关闭连接
con.close()

#打印df,df2
print(df)  #打印了整个表
print(df2) #打印了Customer的第一列
'''
'''


#2、个性化
#create engine
engine=create_engine('sqlite:///Chinook.sqlite')

#connect
con=engine.connect()


# Perform query and save results to DataFrame: df
rs = con.execute('SELECT LastName,Title FROM Employee')
#rs = con.execute('SELECT * FROM Employee WHERE EmployeeId>=6')
df = pd.DataFrame(rs.fetchmany(3))   #fetchmany(3)只取3行数据，并pd.DataFrame
df.columns =['LastName','Title']  #将两列column命名

# Print the length of the DataFrame df
print(len(df))  #1

# Print the head of the DataFrame df
print(df)

#   LastName                Title
# 0    Adams      General Manager
# 1  Edwards        Sales Manager
# 2  Peacock  Sales Support Agent
'''





#3、筛选、排序操作（WHERE，ORDER BY）
'''
# Create engine: engine
#engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId>=6')
    
    df = pd.DataFrame(rs.fetchall())
    
    df.columns = rs.keys()    #df的列标题为rs的key()
    
# Print the head of the DataFrame df
print(df.head())
con.close()
#输出为EmployeeId>=6的结果，并有对应列标题
'''

'''
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns=rs.keys()

# Print head of DataFrame
print(df.head())
'''






'''
#4 使用pandas的read_sql_query()读取数据
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

#使用pandas中的read_sql_query()函数读取数据，并按条件选择数据
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?
print(df.equals(df1))   #证明pandas与engine.connect结果一样

#使用WHERE 及ORDER BY
# Execute query and store records in DataFrame: df
df2=pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId>=6 ORDER BY Birthdate',engine)

# Print head of DataFrame
print(df2.head())
'''




#5、inner Join 关系表数据拼接(2种方法，指两个表有一列相同)
#create engine
engine=create_engine('sqlite:///Chinook.sqlite')
table_names=engine.table_names()
print(table_names)


#第一种：
'''
#extract data and join
#sql语法 表1中有a,b列，表2中有b,c列
#inner join：SELECT a,c FROM 1 INNER JION 2 ON 1.b=2.b
df=pd.read_sql_table('Album',engine)
df1=pd.read_sql_table('Artist',engine)
df3=pd.read_sql_query('SELECT Title,Name FROM Album INNER JOIN Artist on Album.ArtistId=Artist.ArtistId',engine)

print(df.head())
print(df1.head())
print(df3.head())
'''
'''
#第二种：
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT Title,Name FROM Album INNER JOIN Artist on Album.ArtistId=Artist .ArtistId')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
# Print head of DataFrame df
print(df.head())
'''















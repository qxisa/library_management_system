import pymysql

dbConfig = {
     'user': 'root',  # we use our local mysql credintials and implement it across the DB 
     'password': "password",  
     'host': '127.0.0.1',  
     'database': 'library1', 
}

conn = pymysql.connect(**dbConfig)
print(conn)
from connection import connect_mysql as connection_mysql
from connection import connect_postgres as connection_postgre
from connection import connect_oracle as connection_oracle
from connection import connect_mongo as connection_mongodb

d_t=""
v=""

def store_(d_t, v):
 
 cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = v_
        """.format(v_=v))

 Database obj

 if cursor.fetchall() == 1:
                    if database_type=='MySQL':
                        connection_mysql()
                        with mysql_db.conn.cursor() as cursor: 
                          cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c))
                    elif database_type=='PostgreSQL':
                        connection_postgre()
                        with postgres_db.conn.cursor() as cursor: 
                          cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c)) 
                    elif database_type=='Oracle':
                        connection_oracle()
                        with oracle_db.conn.cursor() as cursor: 
                          cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c))
                    
 else:
                    if database_type=='MySQL':
                        connection_mysql()
                        with mysql_db.conn.cursor() as cursor: 
                          cursor.execute(f'''create table vendor(Bill_No, Item))
                          cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c))
                    elif database_type=='PostgreSQL':
                        connection_postgre()
                        with postgres_db.conn.cursor() as cursor: 
                          cursor.execute(f'''create table vendor(Bill_No, Item))
                          cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c)) 
                    elif database_type=='Oracle':
                        connection_oracle()
                        with oracle_db.conn.cursor() as cursor: 
                          cursor.execute(f'''create table vendor(Bill_No, Item))
                          cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c))
                    
cursor.execute(db.Collections.find({Collection:vendor}))                        
if cursor.fetchall()==1:
                        connection_mongodb()
                        mongo_db.conn[obj][vendor].(eval(query))
                        #cursor.execute(obj.vendor.insertMany({Bill_No:id,Item:c}))


                        
                        #else:
 #                  if database_type=='MySQL' or 'PostgreSQL' or 'Oracle':
  #                     cursor.execute(f'''create table vendor(Bill_No, Item))
   #                     cursor.execute(f'''insert into vendor (Bill_No, Item) values (id, c))
    #                else:
     #                   cursor.execute(obj.vendor.insertMany({Bill_No:id,Item:c}))
      #          break

# from project import *

import streamlit as s 
import boto3
import os
import io
#from image1 import main as main_
#from store import store_ as _st_
#from main import main_ as _m_
# from Connect_AWS import connect as connect_
from image1 import login as login_
from image1 import signup as signup_
#from image1 import upload as upload_
#from Read_image import read_image as r_i
# from Connection import connect_mysql as connect_mysql_
# from Connection import connect_postgres as connect_postgres_
# from mysqlnav import database_navigator as mysql_dbnav
# from oraclenav import database_navigator as oracle_dbnav
# from postgrenav import database_navigator as postgre_dbnav
# from mongonav import database_navigator as mongo_dbnav
# from mysql_query import mysql_query as mysql_q
# from oracle_query import oracle_query as oracle_q
# from postgre_query import postgre_query as postgre_q
# #from mongo_query import mongo_query as mongo_q
# import os
from image1 import crop as crop_
from image1 import add_logo as a_l



id=""
vendor=""
c=""

s.sidebar.image(a_l(logo_path=r"C:\Users\AnshitaChugh\download.png", width=160, height=60))
menu = ["Login", "Signup"]

if "Login" not in s.experimental_get_query_params():
        choice = s.sidebar.selectbox("Select an option", menu)
        
        if choice == "Login":
            login_()
        else:
            signup_()
else:
        username = s.experimental_get_query_params()["username"][0]
        s.sidebar.empty()
        s.sidebar.selectbox("Select an option", ["upload"])
        image_file = s.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        p=crop_(username, image_file)
        session = boto3.Session(profile_name='ocr')
        textract=session.client('textract')
        save_path=f"user_data/{username}"
        os.makedirs(save_path, exist_ok=True)
        s.write(type(image_file))
        file_name = p.name.split('.')[0] 
      
        my_file=r'f"{save_path}/{file_name}_cropped.png"'

        with open(my_file,'rb') as file:
          ip_data=file.read()
        response=textract.analyze_expense(Document={'Bytes': ip_data})
        s.text(response)
#         r_i(id, vendor, c, response) 


#         s.sidebar.empty()
#         database_type = s.sidebar.selectbox("Select database type", ["MySQL", "PostgreSQL", "Oracle", "MongoDB"])
#         _st_(database_type, vendor)
        
#         with s.expander(database_type,"Accordiant"):
#          tab1, tab2 = s.tabs(["Database Navigator", "Query Page"])

#          with tab1:
#             if database_type=="MySQL":
#              s.header("MySQL")
#              mysql_dbnav()
#             elif database_type=="Oracle":
#               s.header("Oracle")
#               oracle_dbnav()
#             elif database_type=="PostgreSQL":
#               s.header("PostgreSQL")
#               postgre_dbnav()
#             elif database_type=="MongoDB":
#               s.header("MongoDB")
#               Mongo_dbnav()
#          with tab2:
#             if database_type=="MySQL":
#              s.header("MySQL")
#              mysql_q()
#             elif database_type=="Oracle":
#               s.header("Oracle")
#               oracle_q()
#             elif database_type=="PostgreSQL":
#               s.header("PostgreSQL")
#               postgre_q()
#             elif database_type=="MongoDB":
#               s.header("MongoDB")
#               Mongo_q()
            

# if s.sidebar.button("Logout"):
#         s.experimental_set_query_params(params={})


#with open(Read_image) as f:
 #   exec(f.read())


 



 


#query="""SELECT COUNT(*)
 #       FROM information_schema.tables
  #      WHERE table_name = v""".format(v=vendor)
#query1=db.Collections.find({Collection:vendor})








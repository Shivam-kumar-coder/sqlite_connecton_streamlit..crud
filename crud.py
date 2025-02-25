import streamlit as st
#import mysql.connector as cn
#import streamlit as st
#import matplotlib.pyplot as pyplot
#import pandas as pd 
import sqlite3 as sq
conn=sq.connect("register.db")
cur=conn.cursor()
cur.execute("create table if not  exists emp(id int primary key , name text, age int) ")
#a=st.text_input("enter username")
#b=st.text_input("enter your pasword"
#cnn=cn.connect(host="localhost",user="root",password="root",database="python")
#cur=cnn.cursor()
#cur.execute("create table student(id int auto_increment primary key, name text, class int, age int)")
with st.form("student registration"):
    a=st.text_input("enter your name")
    b=st.text_input("enter ypur id")
    c=st.text_input("enter your age")
    value=(b,a,c)
    query="insert into emp (id,name,age) values(?,?,?)" 
    button=st.form_submit_button("submit")
    #up_button=st.form_submit_button("update")
user_id = st.text_input('enter id')
new_name = st.text_input('enter name')
new_age = st.text_input('enter age')
if st.button('update'):
    query = "update emp set name = ? , age = ? where id = ?"
    cur.execute(query, (new_name, new_age, user_id ))
    conn.commit()
    st.success('data update successfully')
    st.balloons()
if button:
    cur.execute(query,value)
    cur.execute("commit")
    cur.execute("select * from  emp")
    st.success("data inserted")
    st.balloons()
delete_user_id = st.text_input("enter user id ")
if st.button('delete'):
    query = "delete from emp where id = ?"
    cur.execute(query, (delete_user_id,))
    conn.commit()
    st.success('delete data successfully')
    st.balloons()
    
if st.button("view data"):
    cur.execute("select * from emp")
    for i in cur:
        st.write(cur)



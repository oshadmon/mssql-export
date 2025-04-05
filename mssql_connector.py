"""
pyodbc connector - process
1. create database
2. drop database
3. create table
4. insert data
5. drop table
"""
import pyodbc

class MSSQL:
    def __init__(self, server:str, db_name):
        self.conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={db_name};Trusted_Connection=yes;'

    def create_connection(self):
        self.conn = pyodbc.connect(self.conn_str)
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def execute_select(self, query:str):
        self.cur.execute(query)
        columns = [column[0] for column in self.cur.description]
        # Fetch row data and convert to dictionary
        rows = [dict(zip(columns, row)) for row in self.cur.fetchall()]

        return rows




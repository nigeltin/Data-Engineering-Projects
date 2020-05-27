#Dropping and creating tables. Ran to reset tables before each time etl script are ran

import psycopg2

from sql_queries import create_table_queries, drop_table_queries

#Creating and connecting to the database

def create_database():
    conn = psycopg2.connect('host=localhost, dbname=studentdb')
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    cur.execute('drop database if exists intmusicdb')
    cur.execute('create database intmusicdb with encoding "utf8" template template0')
    
    #closing connection to default db
    
    conn.close()
    
    #connecting to intmusicdb
    
    conn = psycopg2.connect('host = localhost, dbname=intmusicdb')
    cur = conn.cursor()
    
    return cur, conn

def drop_tables(cur, conn):
    #drops all tables created on the db
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    #creates tables as defined
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ Function to drop and recreate intmusicdb database and all related tables.
        Usage: python creating_tables.py
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()   
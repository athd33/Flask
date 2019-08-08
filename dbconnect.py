import pymysql


def requestConnection():
    conn = pymysql.connect(host="localhost",
                            user = "root",
                            passwd="Antoine",
                            db="foodappdb")
    return conn


def requestCursor(conn):
    c = conn.cursor()
    return c
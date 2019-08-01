import pymysql


def connection():
    conn = pymysql.connect(host="localhost",
                            user = "root",
                            passwd="Antoine",
                            db="pythonprogramming")
    c = conn.cursor()
    return c, conn
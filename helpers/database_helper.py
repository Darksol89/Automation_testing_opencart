import mysql.connector

def getDatabaseQuery(sql_query):
    try:
        connection = mysql.connector.connect(
            user='root',
            password='password',
            host='127.0.0.1',
            port='3306',
            database='bitnami_opencart')
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()

        return result

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))



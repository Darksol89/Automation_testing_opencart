import mysql.connector
from helpers.database_helper import getDatabaseQuery


def test_opencart_connection():
    sql = 'SELECT * FROM oc_product WHERE model="T123"'
    assert not getDatabaseQuery(sql)



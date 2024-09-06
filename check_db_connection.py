import os
import mysql.connector
from urllib.parse import urlparse
import sys

db_uri = os.getenv('DATABASE_URI')

print("Starting database connection check...")

if not db_uri:
    print("Error: DATABASE_URI is not set")
    sys.exit(1)

try:
    # 解析DATABASE_URI
    result = urlparse(db_uri)
    db_config = {
        'user': result.username,
        'password': result.password,
        'host': result.hostname,
        'port': result.port,
        'database': result.path.lstrip('/')
    }

    # 连接到数据库
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 执行简单查询
    cursor.execute("SELECT version()")
    data = cursor.fetchone()
    print(f"Database version: {data[0]}")

    conn.close()
    print("Database connection successful.")
    sys.exit(0)
except Exception as e:
    # 取消日志，避免泄露
    # print(f"Error occurred: {str(e)}")
    sys.exit(1)

# Import the necessary packages and modules
from django.shortcuts import render
from django.http import HttpResponse
import sys
import logging
from among_us_stats import rds_config
import pymysql

# Database connection info
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
rds_host = rds_config.db_host

# set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# connect to the database
try:
    conn = pymysql.connect(host=rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error(
        "ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

# Log the connection and print a success message to the terminal
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

# set up cursor
cur = conn.cursor()


def say_hello(request):
    return render(request, 'hello.html', {'title': 'Among Us Stats - Home', 'description': 'A website to track stats for the game Among Us'})


def index(request):
    return render(request, 'index.html')


def insert(request):
    return render(request, 'insert.html')


def query(request):
    query = "SELECT DISTINCT player_name FROM match_summary;"
    cur.execute(query)
    result = cur.fetchall()
    data = []
    for row in result:
        data.append(row[0])
    return render(request, 'query.html', {'data': data})


def test_query(request):
    return HttpResponse()

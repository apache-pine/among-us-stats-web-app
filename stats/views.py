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


def main(request):
    # get the most recent games
    cur.execute(
        "SELECT * FROM match_summary WHERE match_id = (SELECT MAX(match_id) FROM match_summary)")
    last_game = cur.fetchall()
    cur.execute("SELECT * FROM player_win_count LIMIT 1;")
    pmw = cur.fetchone()
    cur.execute("SELECT * FROM player_loss_count LIMIT 1;")
    pml = cur.fetchone()
    cur.execute("SELECT * FROM player_kill_count LIMIT 1;")
    pmk = cur.fetchone()
    cur.execute("SELECT * FROM player_death_count LIMIT 1;")
    pmd = cur.fetchone()
    cur.execute("SELECT * FROM role_win_count LIMIT 1;")
    rmw = cur.fetchone()
    cur.execute("SELECT * FROM role_loss_count LIMIT 1;")
    rml = cur.fetchone()
    cur.execute("SELECT * FROM role_kill_count LIMIT 1;")
    rmk = cur.fetchone()
    cur.execute("SELECT * FROM role_death_count LIMIT 1;")
    rmd = cur.fetchone()
    return render(request, 'main.html', {'last_game': last_game, 'pmw': pmw, 'pml': pml, 'pmk': pmk, 'pmd': pmd, 'rmw': rmw, 'rml': rml, 'rmk': rmk, 'rmd': rmd})


def main_pmw(request):
    cur.execute("SELECT * FROM player_win_count;")
    pmw = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Player Total Wins', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the players with the number of matches they have won.', 'header': 'Player Win Count', 'table_header1': 'Player Name', 'table_header2': 'Win Count', 'data': pmw})


def main_pml(request):
    cur.execute("SELECT * FROM player_loss_count;")
    pml = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Player Total Losses', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the players with the number of matches they have lost.', 'header': 'Player Loss Count', 'table_header1': 'Player Name', 'table_header2': 'Loss Count', 'data': pml})


def main_pmk(request):
    cur.execute("SELECT * FROM player_kill_count;")
    pmk = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Player Total Kills', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the players with the number of kills they have made.', 'header': 'Player Kill Count', 'table_header1': 'Player Name', 'table_header2': 'Kill Count', 'data': pmk})


def main_pmd(request):
    cur.execute("SELECT * FROM player_death_count;")
    pmd = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Player Total Deaths', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the players with the number of times they have died.', 'header': 'Player Death Count', 'table_header1': 'Player Name', 'table_header2': 'Death Count', 'data': pmd})


def main_rmw(request):
    cur.execute("SELECT * FROM role_win_count;")
    rmw = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Role Total Wins', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the roles with the number of matches they have won.', 'header': 'Role Win Count', 'table_header1': 'Role Name', 'table_header2': 'Win Count', 'data': rmw})


def main_rml(request):
    cur.execute("SELECT * FROM role_loss_count;")
    rml = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Role Total Losses', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the roles with the number of matches they have lost.', 'header': 'Role Loss Count', 'table_header1': 'Role Name', 'table_header2': 'Loss Count', 'data': rml})


def main_rmk(request):
    cur.execute("SELECT * FROM role_kill_count;")
    rmk = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Role Total Kills', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the roles with the number of kills they have made.', 'header': 'Role Kill Count', 'table_header1': 'Role Name', 'table_header2': 'Kill Count', 'data': rmk})


def main_rmd(request):
    cur.execute("SELECT * FROM role_death_count;")
    rmd = cur.fetchall()
    return render(request, 'main_extra.html', {'title': 'Among Us Stats - Role Total Deaths', 'description': 'A website to track stats for games of Among Us played by Kyr_Sp33dy and other streamers. This page shows a table of the roles with the number of times they have died.', 'header': 'Role Death Count', 'table_header1': 'Role Name', 'table_header2': 'Death Count', 'data': rmd})


def insert(request):
    return render(request, 'insert.html', {})


def query(request):
    return render(request, 'query.html', {})

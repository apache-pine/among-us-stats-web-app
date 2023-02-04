from django.db import models


class MatchResults(models.Model):
    match_id = models.IntegerField()
    player_id = models.IntegerField()
    role_id = models.IntegerField()
    second_role = models.IntegerField()
    modifier_id = models.IntegerField()
    death_id = models.IntegerField()
    killed_by = models.IntegerField()
    killed_by_role = models.IntegerField()
    did_win = models.BooleanField()

    class Meta:
        db_table = 'match_results'


class Match(models.Model):
    match_id = models.IntegerField()
    match_alias = models.CharField(max_length=45)
    date_played = models.DateTimeField()
    game_version_id = models.IntegerField()

    class Meta:
        db_table = 'match'

from django.db import models


class Modifier(models.Model):
    modifier_id = models.AutoField(primary_key=True)
    modifier_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'modifier'


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=45)
    player_alias = models.CharField(max_length=45, blank=True, null=True)
    stream_url = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'player'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING)

    class Meta:
        db_table = 'role'
        unique_together = (('role_id', 'team', 'role_type'),)


class RoleType(models.Model):
    role_type_id = models.AutoField(primary_key=True)
    role_type_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'role_type'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'team'


class GameVersion(models.Model):
    game_version_id = models.AutoField(primary_key=True)
    version_name = models.CharField(max_length=45, blank=True, null=True)
    version_number = models.CharField(max_length=45)

    class Meta:
        db_table = 'game_version'


class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_alias = models.CharField(max_length=45, blank=True, null=True)
    date_played = models.DateField(blank=True, null=True)
    game_version = models.ForeignKey(GameVersion, models.DO_NOTHING)

    class Meta:
        db_table = 'match'
        unique_together = (('match_id', 'game_version'),)


class Death(models.Model):
    death_id = models.AutoField(primary_key=True)
    death_type = models.CharField(max_length=45)

    class Meta:
        db_table = 'death'


class MatchResults(models.Model):
    match = models.OneToOneField(Match, models.DO_NOTHING, primary_key=True)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    role = models.ForeignKey('Role', models.DO_NOTHING)
    second_role = models.IntegerField(blank=True, null=True)
    modifier = models.ForeignKey('Modifier', models.DO_NOTHING)
    death = models.ForeignKey(Death, models.DO_NOTHING)
    killed_by = models.IntegerField(blank=True, null=True)
    killed_by_role = models.IntegerField(blank=True, null=True)
    did_win = models.IntegerField()

    class Meta:
        db_table = 'match_results'
        unique_together = (('match', 'player', 'role', 'modifier', 'death'),)

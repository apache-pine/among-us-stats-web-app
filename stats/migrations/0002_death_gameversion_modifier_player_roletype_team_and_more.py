# Generated by Django 4.1.6 on 2023-02-04 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Death',
            fields=[
                ('death_id', models.AutoField(primary_key=True, serialize=False)),
                ('death_type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'death',
            },
        ),
        migrations.CreateModel(
            name='GameVersion',
            fields=[
                ('game_version_id', models.AutoField(primary_key=True, serialize=False)),
                ('version_name', models.CharField(blank=True, max_length=45, null=True)),
                ('version_number', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'game_version',
            },
        ),
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('modifier_id', models.AutoField(primary_key=True, serialize=False)),
                ('modifier_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'modifier',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=45)),
                ('player_alias', models.CharField(blank=True, max_length=45, null=True)),
                ('stream_url', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('role_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_type_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'role_type',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.AddField(
            model_name='matchresults',
            name='match',
            field=models.OneToOneField(default=999, on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stats.match'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='date_played',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_alias',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='matchresults',
            name='did_win',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='matchresults',
            name='killed_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matchresults',
            name='killed_by_role',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matchresults',
            name='second_role',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=45)),
                ('role_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stats.roletype')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stats.team')),
            ],
            options={
                'db_table': 'role',
                'unique_together': {('role_id', 'team', 'role_type')},
            },
        ),
        migrations.AddField(
            model_name='match',
            name='game_version',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.gameversion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchresults',
            name='death',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.death'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchresults',
            name='modifier',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.modifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchresults',
            name='player',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchresults',
            name='role',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.DO_NOTHING, to='stats.role'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together={('match_id', 'game_version')},
        ),
        migrations.AlterUniqueTogether(
            name='matchresults',
            unique_together={('match', 'player', 'role', 'modifier', 'death')},
        ),
        migrations.RemoveField(
            model_name='match',
            name='game_version_id',
        ),
        migrations.RemoveField(
            model_name='match',
            name='id',
        ),
        migrations.RemoveField(
            model_name='matchresults',
            name='death_id',
        ),
        migrations.RemoveField(
            model_name='matchresults',
            name='id',
        ),
        migrations.RemoveField(
            model_name='matchresults',
            name='match_id',
        ),
        migrations.RemoveField(
            model_name='matchresults',
            name='modifier_id',
        ),
        migrations.RemoveField(
            model_name='matchresults',
            name='player_id',
        ),
        migrations.RemoveField(
            model_name='matchresults',
            name='role_id',
        ),
    ]

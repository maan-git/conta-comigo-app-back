# Generated by Django 2.2.11 on 2020-03-29 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HelpingStatus',
            fields=[
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(db_index=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='help_requests', to='help.HelpCategory', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='HelpRequestStatus',
            fields=[
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalHelpRequestHelpers',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Creation date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('help_request', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='help.HelpRequest')),
                ('helper_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='help.HelpingStatus')),
            ],
            options={
                'verbose_name': 'historical help request helpers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalHelpRequest',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.TextField(db_index=True, verbose_name='Description')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Creation date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='help.HelpCategory', verbose_name='Category')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('owner_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='help.HelpRequestStatus', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'historical help request',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HelpRequestHelpers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('help_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help.HelpRequest')),
                ('helper_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help.HelpingStatus')),
            ],
        ),
        migrations.AddField(
            model_name='helprequest',
            name='helping_users',
            field=models.ManyToManyField(related_name='helping_requests', through='help.HelpRequestHelpers', to=settings.AUTH_USER_MODEL, verbose_name='Users helping'),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='owner_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='help_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='help_requests', to='help.HelpRequestStatus', verbose_name='Status'),
        ),
    ]
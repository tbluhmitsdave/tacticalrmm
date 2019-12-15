# Generated by Django 2.2.3 on 2019-07-07 23:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuLoadCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpuload', models.PositiveIntegerField(default=85)),
                ('status', models.CharField(default='N/A', max_length=30)),
                ('more_info', models.CharField(default='N/A', max_length=255)),
                ('email_alert', models.BooleanField(default=False)),
                ('text_alert', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpuloadchecks', to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='DiskCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disk', models.CharField(max_length=2)),
                ('threshold', models.PositiveIntegerField(default=25)),
                ('status', models.CharField(default='N/A', max_length=30)),
                ('email_alert', models.BooleanField(default=False)),
                ('text_alert', models.BooleanField(default=False)),
                ('more_info', models.TextField(null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diskchecks', to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='PingCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, null=True)),
                ('failures', models.PositiveIntegerField(default=5)),
                ('status', models.CharField(default='N/A', max_length=30)),
                ('failure_count', models.IntegerField(default=0)),
                ('email_alert', models.BooleanField(default=False)),
                ('text_alert', models.BooleanField(default=False)),
                ('more_info', models.TextField(null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pingchecks', to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='PingCheckEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(auto_now=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.PingCheck')),
            ],
        ),
        migrations.CreateModel(
            name='MemoryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_history', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), default=list, null=True, size=None)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='MemCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold', models.PositiveIntegerField(default=75)),
                ('status', models.CharField(default='N/A', max_length=30)),
                ('email_alert', models.BooleanField(default=False)),
                ('text_alert', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memchecks', to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='DiskCheckEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(auto_now=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.DiskCheck')),
            ],
        ),
        migrations.CreateModel(
            name='CpuLoadCheckEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(auto_now=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.CpuLoadCheck')),
            ],
        ),
        migrations.CreateModel(
            name='CpuHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_history', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), default=list, null=True, size=None)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpuhistory', to='agents.Agent')),
            ],
        ),
    ]
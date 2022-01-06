# Generated by Django 3.0.6 on 2020-06-04 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0002_auto_20200531_2058"),
        ("agents", "0003_agent_checks_last_generated"),
        ("automation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="policy",
            name="enforced",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="PolicyExclusions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "agents",
                    models.ManyToManyField(
                        related_name="policy_exclusions", to="agents.Agent"
                    ),
                ),
                (
                    "clients",
                    models.ManyToManyField(
                        related_name="policy_exclusions", to="clients.Client"
                    ),
                ),
                (
                    "policy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exclusions",
                        to="automation.Policy",
                    ),
                ),
                (
                    "sites",
                    models.ManyToManyField(
                        related_name="policy_exclusions", to="clients.Site"
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 2.0.9 on 2019-03-07 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markupfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Election",
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
                ("name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("nominations_open", models.DateTimeField(blank=True, null=True)),
                ("nominations_close", models.DateTimeField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Nomination",
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
                ("name", models.CharField(max_length=1024, null=True)),
                ("email", models.CharField(max_length=1024, null=True)),
                (
                    "previous_board_service",
                    models.CharField(max_length=1024, null=True),
                ),
                ("employer", models.CharField(max_length=1024, null=True)),
                (
                    "other_affiliations",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "nomination_statement",
                    markupfield.fields.MarkupField(null=True, rendered_field=True),
                ),
                (
                    "nomination_statement_markup_type",
                    models.CharField(
                        choices=[
                            ("", "--"),
                            ("html", "HTML"),
                            ("plain", "Plain"),
                            ("markdown", "Markdown"),
                            ("restructuredtext", "Restructured Text"),
                        ],
                        default="markdown",
                        editable=False,
                        max_length=30,
                    ),
                ),
                (
                    "_nomination_statement_rendered",
                    models.TextField(editable=False, null=True),
                ),
                ("accepted", models.BooleanField(default=False)),
                ("approved", models.BooleanField(default=False)),
                (
                    "election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nominations.Election",
                    ),
                ),
                (
                    "nominator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nominations_made",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Nominee",
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
                ("name", models.CharField(max_length=1024, null=True)),
                ("email", models.CharField(max_length=1024, null=True)),
                ("accepted", models.BooleanField(default=False)),
                ("approved", models.BooleanField(default=False)),
                ("slug", models.SlugField(blank=True, max_length=255, null=True)),
                (
                    "election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nominees",
                        to="nominations.Election",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nominations_recieved",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="nomination",
            name="nominee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nominations",
                to="nominations.Nominee",
            ),
        ),
    ]

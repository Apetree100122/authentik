# Generated by Django 3.0.5 on 2020-05-10 14:03

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("passbook_flows", "0003_auto_20200509_1258"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prompt",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "field_key",
                    models.SlugField(
                        help_text="Name of the form field, also used to store the value"
                    ),
                ),
                ("label", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("text", "Text"),
                            ("e-mail", "Email"),
                            ("password", "Password"),
                            ("number", "Number"),
                        ],
                        max_length=100,
                    ),
                ),
                ("required", models.BooleanField(default=True)),
                ("placeholder", models.TextField()),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="PromptStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="passbook_flows.Stage",
                    ),
                ),
                ("fields", models.ManyToManyField(to="passbook_stages_prompt.Prompt")),
            ],
            options={
                "verbose_name": "Prompt Stage",
                "verbose_name_plural": "Prompt Stages",
            },
            bases=("passbook_flows.stage",),
        ),
    ]

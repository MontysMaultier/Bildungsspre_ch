# Generated by Django 3.1 on 2020-08-10 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bildungsspre_chApplikation', '0004_auto_20200810_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ['field']},
        ),
        migrations.RenameField(
            model_name='field',
            old_name='title',
            new_name='field',
        ),
    ]

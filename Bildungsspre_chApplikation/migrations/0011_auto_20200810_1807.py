# Generated by Django 3.1 on 2020-08-10 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bildungsspre_chApplikation', '0010_auto_20200810_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='wortart',
            new_name='word_type',
        ),
    ]

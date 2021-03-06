# Generated by Django 3.1 on 2020-08-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bildungsspre_chApplikation', '0009_auto_20200810_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='source',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='wortart',
            field=models.CharField(blank=True, choices=[('ADJ', 'Adjective'), ('ADV', 'Adverb'), ('INT', 'Interjection'), ('KON', 'Konjunktion'), ('PRÄ', 'Präposition'), ('PRO', 'Pronomen'), ('SUB', 'Substantiv, Nomen'), ('VER', 'Verb')], default='SUB', max_length=3),
        ),
    ]

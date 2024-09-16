# Generated by Django 3.1 on 2021-03-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_profile_user_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_icon',
            field=models.CharField(choices=[('default', 'Default'), ('mp', 'Mystery person'), ('retro', 'Retro'), ('identicon', 'Identicon'), ('monsterid', 'Monster'), ('robohash', 'Robohash'), ('wavatar', 'Wavatar')], default='default', max_length=100),
        ),
    ]

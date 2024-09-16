# Generated by Django 3.1 on 2020-11-24 17:29

from django.db import migrations
import taggit.managers


# def add_watched_tags(apps, schema_editor):
#     # https://github.com/jazzband/django-taggit/issues/454
#
#     Profile = apps.get_model('accounts', 'Profile')
#     Tag = apps.get_model('taggit', 'Tag')
#
#     profiles = Profile.objects.all()
#     for pro in profiles:
#
#         tag_strs = [tag.lower() for tag in pro.watched_tags.split(",") if tag]
#         tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_strs]
#
#         pro.watched.remove()
#         pro.watched.add(*tags)
#         pro.save()


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('accounts', '0015_profile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='watched',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.',
                                                  through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

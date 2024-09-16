# Generated by Django 3.0.2 on 2020-02-17 22:42

from django.db import migrations, models
import hjson
import toml


def init_toml(apps, schema_editor):
    Recipes = apps.get_model('recipes', 'Analysis')
    Job = apps.get_model('recipes', 'Job')

    def remap(m):
        objs = m.objects.all()
        for obj in objs:
            # Load the data as a regular dict
            try:
                json_data = hjson.loads(obj.json_text)
            except Exception:
                continue
            toml_text = toml.dumps(json_data)
            # Bypass modifying the date on each recipe
            m.objects.filter(id=obj.id).update(json_text=toml_text)

    # Remap json_text to toml_text in recipes and jobs.
    remap(Job)
    remap(Recipes)


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_label'),
    ]
    operations = [
        migrations.RunPython(init_toml),
    ]

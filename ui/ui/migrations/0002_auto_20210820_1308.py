# Generated by Django 3.2.6 on 2021-08-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='name',
            new_name='input',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='new',
            name='name',
        ),
        migrations.AddField(
            model_name='bot',
            name='output',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='new',
            name='inputt',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='new',
            name='outputt',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]

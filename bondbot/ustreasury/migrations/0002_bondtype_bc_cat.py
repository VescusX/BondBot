# Generated by Django 4.2.10 on 2024-02-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ustreasury', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondtype',
            name='bc_cat',
            field=models.CharField(default='undefined', max_length=15),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_aplications_appliedtuition'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplications',
            name='tuitionid',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
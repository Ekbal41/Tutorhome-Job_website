# Generated by Django 4.1.1 on 2022-11-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoruser', '0003_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='depertment',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='educationlevel',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.CharField(max_length=40, null=True),
        ),
    ]

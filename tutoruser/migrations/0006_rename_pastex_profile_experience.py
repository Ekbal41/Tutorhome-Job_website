# Generated by Django 4.1.1 on 2022-11-16 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutoruser', '0005_profile_email_profile_facebook_profile_linkedin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pastex',
            new_name='experience',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usertypes_user_address_user_age_user_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('supervisor', 'Supervisor'), ('admin', 'Admin')], default='student', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(max_length=129, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='UserTypes',
        ),
    ]

# Generated by Django 3.1.4 on 2021-06-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20210606_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='education',
            field=models.CharField(choices=[('A', 'High School'), ('B', 'Associate Degree'), ('C', 'Bachelors Degree'), ('D', 'Masters Degree'), ('E', 'Doctoral Degree')], max_length=100),
        ),
    ]

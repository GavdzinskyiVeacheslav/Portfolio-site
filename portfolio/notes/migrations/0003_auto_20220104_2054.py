# Generated by Django 3.2.6 on 2022-01-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20220104_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Date of publication'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]

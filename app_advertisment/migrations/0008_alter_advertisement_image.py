# Generated by Django 4.2.3 on 2023-08-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0007_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='j.png', upload_to='advertisements/', verbose_name='Изображения'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default/light.png', upload_to='media/', verbose_name='アイコン画像'),
        ),
    ]

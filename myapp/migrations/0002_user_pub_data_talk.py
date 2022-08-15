# Generated by Django 4.0.4 on 2022-06-07 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pub_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date signed up'),
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talk', models.CharField(max_length=500)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('talk_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk_from', to=settings.AUTH_USER_MODEL)),
                ('talk_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
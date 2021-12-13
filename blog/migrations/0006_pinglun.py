# Generated by Django 3.1.2 on 2021-11-08 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20211102_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pinglun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=120, null=True)),
                ('belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pinglun_article', to='blog.article')),
                ('belong_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pinglun_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.1.2 on 2021-10-26 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_belong'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lanmu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lanmu_children', to='blog.lanmu')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='belong_lanmu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_lanmu', to='blog.lanmu'),
        ),
    ]

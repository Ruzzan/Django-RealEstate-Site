# Generated by Django 2.2 on 2019-09-02 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=120)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Home')),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-08 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('area', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Poll')),
            ],
        ),
    ]

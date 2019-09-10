# Generated by Django 2.2.5 on 2019-09-06 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciphers', '0003_auto_20190906_1527'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CipherTexts',
            new_name='CipherText',
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('keyword', models.CharField(max_length=100)),
                ('alpahabet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciphers.Alphabet')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_alter_intentsamples_product_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainingModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileModel', models.FileField(upload_to='')),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-29 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('declaring', '0007_auto_20200424_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='auto', to='user.Vehicle'),
        ),
    ]
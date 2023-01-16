# Generated by Django 4.1.5 on 2023-01-16 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobilioModelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marke', models.CharField(help_text='Automobilio marke', max_length=200, verbose_name='Marke')),
                ('modelis', models.CharField(help_text='Automobilio modelis', max_length=200, verbose_name='Modelis')),
            ],
        ),
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valstybinis_nr', models.CharField(help_text='Valstybinis numeris', max_length=200, verbose_name='Valstybinis numeris')),
                ('vin_kodas', models.CharField(help_text='VIN kodas', max_length=200, verbose_name='VIN kodas')),
                ('klientas', models.CharField(help_text='Klientas', max_length=200, verbose_name='Klientas')),
                ('modelis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.automobiliomodelis')),
            ],
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(help_text='Paslaugos pavadinimas', max_length=200, verbose_name='Pavadinimas')),
                ('kaina', models.FloatField(verbose_name='Kaina')),
            ],
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('automobilis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoservice.automobilis')),
            ],
        ),
        migrations.CreateModel(
            name='UzsakymoEilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiekis', models.IntegerField(help_text='Kiekis', verbose_name='Kiekis')),
                ('paslauga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoservice.paslauga')),
                ('uzsakymas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoservice.uzsakymas')),
            ],
        ),
    ]
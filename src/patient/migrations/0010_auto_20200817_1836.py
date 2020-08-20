# Generated by Django 3.1 on 2020-08-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20200817_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='medicine_intake',
        ),
        migrations.AddField(
            model_name='disease',
            name='medicine_intake',
            field=models.ManyToManyField(to='patient.MedicineIntake'),
        ),
        migrations.AlterField(
            model_name='medicineintake',
            name='quantity',
            field=models.CharField(choices=[('3', 'Three Time'), ('2', 'Two Time'), ('1', 'One Time')], max_length=5),
        ),
    ]
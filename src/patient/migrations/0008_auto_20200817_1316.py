# Generated by Django 3.1 on 2020-08-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_auto_20200817_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineintake',
            name='quantity',
            field=models.CharField(choices=[('2', 'Two Time'), ('3', 'Three Time'), ('1', 'One Time')], max_length=5),
        ),
        migrations.AlterField(
            model_name='patient',
            name='disease',
            field=models.ManyToManyField(blank=True, to='patient.Disease'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='prescription',
            field=models.ManyToManyField(blank=True, to='patient.MedicineIntake'),
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]

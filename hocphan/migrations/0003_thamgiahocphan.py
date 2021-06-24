# Generated by Django 3.2.2 on 2021-06-18 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quanlysinhvien', '0004_auto_20210617_1825'),
        ('hocphan', '0002_hocphan'),
    ]

    operations = [
        migrations.CreateModel(
            name='thamgiahocphan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngaybd', models.DateField()),
                ('ngaykt', models.DateField()),
                ('diem', models.FloatField(default=0)),
                ('mahk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hocphan.hocky')),
                ('mahp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hocphan.hocphan')),
                ('masv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quanlysinhvien.sinhvien')),
            ],
        ),
    ]
# Generated by Django 3.2.2 on 2021-06-17 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quanlysinhvien', '0003_alter_sinhvien_masv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sinhvien',
            old_name='masv',
            new_name='mssv',
        ),
        migrations.RenameField(
            model_name='sinhvien',
            old_name='hoten',
            new_name='tensv',
        ),
    ]
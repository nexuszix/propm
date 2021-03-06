# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20171028_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='author',
        ),
        migrations.AddField(
            model_name='land',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='approve_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='land',
            name='benifit',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='contract_enddate',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='contract_startdate',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='deposit_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='land',
            name='ngan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='phone_no',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='land',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='land',
            name='purpose',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='rai',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='rental_duration',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='land',
            name='rental_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='land',
            name='renter_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='seller',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='land',
            name='sign_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='land',
            name='wa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='land',
            name='province',
            field=models.CharField(blank=True, choices=[('กระบี่', 'กระบี่'), ('กรุงเทพมหานคร', 'กรุงเทพมหานคร'), ('กาญจนบุรี', 'กาญจนบุรี'), ('กาฬสินธุ์', 'กาฬสินธุ์'), ('กำแพงเพชร', 'กำแพงเพชร'), ('ขอนแก่น', 'ขอนแก่น'), ('จันทบุรี', 'จันทบุรี'), ('ฉะเชิงเทรา', 'ฉะเชิงเทรา'), ('ชลบุรี', 'ชลบุรี'), ('ชัยนาท', 'ชัยนาท'), ('ชัยภูมิ', 'ชัยภูมิ'), ('ชุมพร', 'ชุมพร'), ('เชียงราย', 'เชียงราย'), ('เชียงใหม่', 'เชียงใหม่'), ('ตรัง', 'ตรัง'), ('ตราด', 'ตราด'), ('ตาก', 'ตาก'), ('นครนายก', 'นครนายก'), ('นครปฐม', 'นครปฐม'), ('นครพนม', 'นครพนม'), ('นครราชสีมา', 'นครราชสีมา'), ('นครศรีธรรมราช', 'นครศรีธรรมราช'), ('นครสวรรค์', 'นครสวรรค์'), ('นนทบุรี', 'นนทบุรี'), ('นราธิวาส', 'นราธิวาส'), ('น่าน', 'น่าน'), ('บุรีรัมย์', 'บุรีรัมย์'), ('ปทุมธานี', 'ปทุมธานี'), ('ประจวบคีรีขันธ์', 'ประจวบคีรีขันธ์'), ('ปราจีนบุรี', 'ปราจีนบุรี'), ('ปัตตานี', 'ปัตตานี'), ('พระนครศรีอยุธยา', 'พระนครศรีอยุธยา'), ('พะเยา', 'พะเยา'), ('พังงา', 'พังงา'), ('พัทลุง', 'พัทลุง'), ('พิจิตร', 'พิจิตร'), ('พิษณุโลก', 'พิษณุโลก'), ('เพชรบุรี', 'เพชรบุรี'), ('เพชรบูรณ์', 'เพชรบูรณ์'), ('แพร่', 'แพร่'), ('ภูเก็ต', 'ภูเก็ต'), ('มหาสารคาม', 'มหาสารคาม'), ('มุกดาหาร', 'มุกดาหาร'), ('แม่ฮ่องสอน', 'แม่ฮ่องสอน'), ('ยโสธร', 'ยโสธร'), ('ยะลา', 'ยะลา'), ('ร้อยเอ็ด', 'ร้อยเอ็ด'), ('ระนอง', 'ระนอง'), ('ระยอง', 'ระยอง'), ('ราชบุรี', 'ราชบุรี'), ('ลพบุรี', 'ลพบุรี'), ('ลำปาง', 'ลำปาง'), ('ลำพูน', 'ลำพูน'), ('เลย', 'เลย'), ('ศรีสะเกษ', 'ศรีสะเกษ'), ('สกลนคร', 'สกลนคร'), ('สงขลา', 'สงขลา'), ('สตูล', 'สตูล'), ('สมุทรปราการ', 'สมุทรปราการ'), ('สมุทรสงคราม', 'สมุทรสงคราม'), ('สมุทรสาคร', 'สมุทรสาคร'), ('สระแก้ว', 'สระแก้ว'), ('สระบุรี', 'สระบุรี'), ('สิงห์บุรี', 'สิงห์บุรี'), ('สุโขทัย', 'สุโขทัย'), ('สุพรรณบุรี', 'สุพรรณบุรี'), ('สุราษฎร์ธานี', 'สุราษฎร์ธานี'), ('สุรินทร์', 'สุรินทร์'), ('หนองคาย', 'หนองคาย'), ('หนองบัวลำภู', 'หนองบัวลำภู'), ('อ่างทอง', 'อ่างทอง'), ('อำนาจเจริญ', 'อำนาจเจริญ'), ('อุดรธานี', 'อุดรธานี'), ('อุตรดิตถ์', 'อุตรดิตถ์'), ('อุทัยธานี', 'อุทัยธานี'), ('อุบลราชธานี', 'อุบลราชธานี')], default='', max_length=100),
        ),
    ]

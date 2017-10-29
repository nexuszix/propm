from django.db import models
from django.utils import timezone

# Create your models here.

class Land(models.Model):
	province_list = (
		('กระบี่','กระบี่'),
		('กรุงเทพมหานคร','กรุงเทพมหานคร'),
		('กาญจนบุรี','กาญจนบุรี'),
		('กาฬสินธุ์','กาฬสินธุ์'),
		('กำแพงเพชร','กำแพงเพชร'),
		('ขอนแก่น','ขอนแก่น'),
		('จันทบุรี','จันทบุรี'),
		('ฉะเชิงเทรา','ฉะเชิงเทรา'),
		('ชลบุรี','ชลบุรี'),
		('ชัยนาท','ชัยนาท'),
		('ชัยภูมิ','ชัยภูมิ'),
		('ชุมพร','ชุมพร'),
		('เชียงราย','เชียงราย'),
		('เชียงใหม่','เชียงใหม่'),
		('ตรัง','ตรัง'),
		('ตราด','ตราด'),
		('ตาก','ตาก'),
		('นครนายก','นครนายก'),
		('นครปฐม','นครปฐม'),
		('นครพนม','นครพนม'),
		('นครราชสีมา','นครราชสีมา'),
		('นครศรีธรรมราช','นครศรีธรรมราช'),
		('นครสวรรค์','นครสวรรค์'),
		('นนทบุรี','นนทบุรี'),
		('นราธิวาส','นราธิวาส'),
		('น่าน','น่าน'),
		('บุรีรัมย์','บุรีรัมย์'),
		('ปทุมธานี','ปทุมธานี'),
		('ประจวบคีรีขันธ์','ประจวบคีรีขันธ์'),
		('ปราจีนบุรี','ปราจีนบุรี'),
		('ปัตตานี','ปัตตานี'),
		('พระนครศรีอยุธยา','พระนครศรีอยุธยา'),
		('พะเยา','พะเยา'),
		('พังงา','พังงา'),
		('พัทลุง','พัทลุง'),
		('พิจิตร','พิจิตร'),
		('พิษณุโลก','พิษณุโลก'),
		('เพชรบุรี','เพชรบุรี'),
		('เพชรบูรณ์','เพชรบูรณ์'),
		('แพร่','แพร่'),
		('ภูเก็ต','ภูเก็ต'),
		('มหาสารคาม','มหาสารคาม'),
		('มุกดาหาร','มุกดาหาร'),
		('แม่ฮ่องสอน','แม่ฮ่องสอน'),
		('ยโสธร','ยโสธร'),
		('ยะลา','ยะลา'),
		('ร้อยเอ็ด','ร้อยเอ็ด'),
		('ระนอง','ระนอง'),
		('ระยอง','ระยอง'),
		('ราชบุรี','ราชบุรี'),
		('ลพบุรี','ลพบุรี'),
		('ลำปาง','ลำปาง'),
		('ลำพูน','ลำพูน'),
		('เลย','เลย'),
		('ศรีสะเกษ','ศรีสะเกษ'),
		('สกลนคร','สกลนคร'),
		('สงขลา','สงขลา'),
		('สตูล','สตูล'),
		('สมุทรปราการ','สมุทรปราการ'),
		('สมุทรสงคราม','สมุทรสงคราม'),
		('สมุทรสาคร','สมุทรสาคร'),
		('สระแก้ว','สระแก้ว'),
		('สระบุรี','สระบุรี'),
		('สิงห์บุรี','สิงห์บุรี'),
		('สุโขทัย','สุโขทัย'),
		('สุพรรณบุรี','สุพรรณบุรี'),
		('สุราษฎร์ธานี','สุราษฎร์ธานี'),
		('สุรินทร์','สุรินทร์'),
		('หนองคาย','หนองคาย'),
		('หนองบัวลำภู','หนองบัวลำภู'),
		('อ่างทอง','อ่างทอง'),
		('อำนาจเจริญ','อำนาจเจริญ'),
		('อุดรธานี','อุดรธานี'),
		('อุตรดิตถ์','อุตรดิตถ์'),
		('อุทัยธานี','อุทัยธานี'),
		('อุบลราชธานี','อุบลราชธานี'),
	)

	landId = models.CharField(max_length=20, default="", blank=True, )
	province = models.CharField(max_length=100, default="", blank=True, choices=province_list)
	district = models.CharField(max_length=100, default="", blank=True)
	subdistrict = models.CharField(max_length=100, default="", blank=True)
	rai = models.IntegerField(default=0)
	ngan = models.IntegerField(default=0)
	wa = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	seller = models.CharField(max_length=100, default="", blank=True)
	price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	purchase_date = models.CharField(max_length=100, default="", blank=True)
	purpose = models.CharField(max_length=100, default="", blank=True)
	benifit = models.CharField(max_length=100, default="", blank=True)
	renter_name = models.CharField(max_length=100, default="", blank=True)
	address = models.CharField(max_length=100, default="", blank=True)
	phone_no = models.CharField(max_length=100, default="", blank=True)
	rental_fee = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	rental_duration = models.CharField(max_length=20, default="", blank=True)
	contract_startdate = models.CharField(max_length=100, default="", blank=True)
	contract_enddate = models.CharField(max_length=100, default="", blank=True)
	approve_date = models.CharField(max_length=100, default="", blank=True)
	sign_date = models.CharField(max_length=100, default="", blank=True)
	deposit_amount = models.CharField(max_length=100, default="", blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.landId + "/" + self.province

# class MasLocation(models.Model):
# 	province = models.CharField(max_length=100)
# 	district = models.CharField(max_length=100)
# 	subdistrict = models.CharField(max_length=100)

# 	def __str__(self):
# 		return "ตำบล" + self.subdistrict + " อำเภอ" + self.district + " จังหวัด" + self.province

	# province_list = (
	# 	('กระบี่','กระบี่'),
	# 	('กรุงเทพมหานคร','กรุงเทพมหานคร'),
	# 	('กาญจนบุรี','กาญจนบุรี'),
	# 	('กาฬสินธุ์','กาฬสินธุ์'),
	# 	('กำแพงเพชร','กำแพงเพชร'),
	# 	('ขอนแก่น','ขอนแก่น'),
	# 	('จันทบุรี','จันทบุรี'),
	# 	('ฉะเชิงเทรา','ฉะเชิงเทรา'),
	# 	('ชลบุรี','ชลบุรี'),
	# 	('ชัยนาท','ชัยนาท'),
	# 	('ชัยภูมิ','ชัยภูมิ'),
	# 	('ชุมพร','ชุมพร'),
	# 	('เชียงราย','เชียงราย'),
	# 	('เชียงใหม่','เชียงใหม่'),
	# 	('ตรัง','ตรัง'),
	# 	('ตราด','ตราด'),
	# 	('ตาก','ตาก'),
	# 	('นครนายก','นครนายก'),
	# 	('นครปฐม','นครปฐม'),
	# 	('นครพนม','นครพนม'),
	# 	('นครราชสีมา','นครราชสีมา'),
	# 	('นครศรีธรรมราช','นครศรีธรรมราช'),
	# 	('นครสวรรค์','นครสวรรค์'),
	# 	('นนทบุรี','นนทบุรี'),
	# 	('นราธิวาส','นราธิวาส'),
	# 	('น่าน','น่าน'),
	# 	('บุรีรัมย์','บุรีรัมย์'),
	# 	('ปทุมธานี','ปทุมธานี'),
	# 	('ประจวบคีรีขันธ์','ประจวบคีรีขันธ์'),
	# 	('ปราจีนบุรี','ปราจีนบุรี'),
	# 	('ปัตตานี','ปัตตานี'),
	# 	('พระนครศรีอยุธยา','พระนครศรีอยุธยา'),
	# 	('พะเยา','พะเยา'),
	# 	('พังงา','พังงา'),
	# 	('พัทลุง','พัทลุง'),
	# 	('พิจิตร','พิจิตร'),
	# 	('พิษณุโลก','พิษณุโลก'),
	# 	('เพชรบุรี','เพชรบุรี'),
	# 	('เพชรบูรณ์','เพชรบูรณ์'),
	# 	('แพร่','แพร่'),
	# 	('ภูเก็ต','ภูเก็ต'),
	# 	('มหาสารคาม','มหาสารคาม'),
	# 	('มุกดาหาร','มุกดาหาร'),
	# 	('แม่ฮ่องสอน','แม่ฮ่องสอน'),
	# 	('ยโสธร','ยโสธร'),
	# 	('ยะลา','ยะลา'),
	# 	('ร้อยเอ็ด','ร้อยเอ็ด'),
	# 	('ระนอง','ระนอง'),
	# 	('ระยอง','ระยอง'),
	# 	('ราชบุรี','ราชบุรี'),
	# 	('ลพบุรี','ลพบุรี'),
	# 	('ลำปาง','ลำปาง'),
	# 	('ลำพูน','ลำพูน'),
	# 	('เลย','เลย'),
	# 	('ศรีสะเกษ','ศรีสะเกษ'),
	# 	('สกลนคร','สกลนคร'),
	# 	('สงขลา','สงขลา'),
	# 	('สตูล','สตูล'),
	# 	('สมุทรปราการ','สมุทรปราการ'),
	# 	('สมุทรสงคราม','สมุทรสงคราม'),
	# 	('สมุทรสาคร','สมุทรสาคร'),
	# 	('สระแก้ว','สระแก้ว'),
	# 	('สระบุรี','สระบุรี'),
	# 	('สิงห์บุรี','สิงห์บุรี'),
	# 	('สุโขทัย','สุโขทัย'),
	# 	('สุพรรณบุรี','สุพรรณบุรี'),
	# 	('สุราษฎร์ธานี','สุราษฎร์ธานี'),
	# 	('สุรินทร์','สุรินทร์'),
	# 	('หนองคาย','หนองคาย'),
	# 	('หนองบัวลำภู','หนองบัวลำภู'),
	# 	('อ่างทอง','อ่างทอง'),
	# 	('อำนาจเจริญ','อำนาจเจริญ'),
	# 	('อุดรธานี','อุดรธานี'),
	# 	('อุตรดิตถ์','อุตรดิตถ์'),
	# 	('อุทัยธานี','อุทัยธานี'),
	# 	('อุบลราชธานี','อุบลราชธานี'),
	# )

	# landId = models.CharField(max_length=20, default="", blank=True, )
	# province = models.CharField(max_length=100, default="", blank=True, choices=province_list)
	# district = models.CharField(max_length=100, default="", blank=True)
	# subdistrict = models.CharField(max_length=100, default="", blank=True)
	# rai = models.IntegerField(default=0)
	# ngan = models.IntegerField(default=0)
	# wa = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	# seller = models.CharField(max_length=100, default="", blank=True)
	# price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	# purchase_date = models.CharField(max_length=100, default="", blank=True)
	# purpose = models.CharField(max_length=100, default="", blank=True)
	# benifit = models.CharField(max_length=100, default="", blank=True)
	# renter_name = models.CharField(max_length=100, default="", blank=True)
	# address = models.CharField(max_length=100, default="", blank=True)
	# phone_no = models.CharField(max_length=100, default="", blank=True)
	# rental_fee = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	# rental_duration = models.CharField(max_length=20, default="", blank=True)
	# contract_startdate = models.CharField(max_length=100, default="", blank=True)
	# contract_enddate = models.CharField(max_length=100, default="", blank=True)
	# approve_date = models.CharField(max_length=100, default="", blank=True)
	# sign_date = models.CharField(max_length=100, default="", blank=True)
	# deposit_amount = models.CharField(max_length=100, default="", blank=True)
	# created_date = models.DateTimeField(default=timezone.now)

	# def __unicode__(self):
	# 	return self.landId + "/" + self.province




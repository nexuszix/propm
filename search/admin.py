from django.contrib import admin
from .models import Land
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
# class LandAdmin(admin.ModelAdmin):
# 	list_display = ('province', 'district', 'subdistrict', 'landId', 'renter_name',)
# 	# list_filter = ('province',)
# 	search_fields = ['province', 'district', 'subdistrict', 'landId', 'renter_name',]
# 	# list_editable = ('district', 'subdistrict',)

class LandResource(resources.ModelResource):
	class Meta:
		model = Land

@admin.register(Land)
class LandAdmin(ImportExportModelAdmin):
	resource_class = LandResource
	list_display = ('province', 'district', 'subdistrict', 'landId', 'renter_name',)
# # 	list_filter = ('province',)
	search_fields = ['province', 'district', 'subdistrict', 'landId', 'renter_name',]


admin.site.site_header = "THG Property Management System"




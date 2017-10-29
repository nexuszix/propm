from import_export import resources
from .models import Land

class LandResource(resources.ModelResource):
    class Meta:
        model = Land
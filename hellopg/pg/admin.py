from django.contrib import admin
from pg.models import UploadPG,Profile

class UploadPGAdmin(admin.ModelAdmin):
    list_display=['location','pgname','pgtype','pglocation','pgdescription','pgprice','pgcondition','pgmeals','ownername','pgmobile','ammenities1','ammenities3','ammenities3','ammenities4','ammenities5','ammenities6','ammenities7','ammenities8','ammenities9','ammenities10','pgimage1','pgimage2','pgimage3','user_id']

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','profile_pic']

admin.site.register(UploadPG,UploadPGAdmin)
admin.site.register(Profile,ProfileAdmin)

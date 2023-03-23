from django.contrib import admin
from user.models import MasterContents,User,heavyvehicleaddress, Device,Request_labour_contructor, Request_SubContractor, labour_contructor,NormalUser, heavyvehivalregistration,Request_driver_Operator,Request_Heavy_Vehical, driveroperatorregistration, subcontractorregistration, Requirement, VedioUplaod

admin.site.register(Device)
admin.site.register(MasterContents)
admin.site.register(Request_driver_Operator)
admin.site.register(Request_labour_contructor)
admin.site.register(Request_SubContractor)
admin.site.register(User)
admin.site.register(heavyvehicleaddress)

class NormalUserAdmin(admin.ModelAdmin):
    list_display = ['Id', 'name']
admin.site.register(NormalUser,NormalUserAdmin)

class VedioUploadAdmin(admin.ModelAdmin):
    list_display = ['Id', 'image_uplaod', 'vediourl']
admin.site.register(VedioUplaod, VedioUploadAdmin)


class requestrequirementAdmin(admin.ModelAdmin):
    list_display = ['Id', 'title', 'description', 'requirement_image']
admin.site.register(Requirement,requestrequirementAdmin)



admin.site.register(Request_Heavy_Vehical)

#admin.site.register(subcontractorregistration)

admin.site.register(labour_contructor)

# class labourcontractoradmin(admin.ModelAdmin):
#     list_display = ['Id','labourcontractorname', 'labourwork', 'lobourinnumber', 'mobile_number',]

# admin.site.register(labour_contructor,labourcontractoradmin)

class heavyvehivalregistrationAdmin(admin.ModelAdmin):
    list_display = ['Id', 'vehical_name', 'ownername', 'vehicleregistrationnumber', 'vehicle_image',]

admin.site.register(heavyvehivalregistration,heavyvehivalregistrationAdmin)


class subcontractorregistrationAdmin(admin.ModelAdmin):
    list_display = ['Id', 'contractorname', 'firmname', 'expriencesinyear', 'license_number', 'subcontractor_image',]
admin.site.register(subcontractorregistration, subcontractorregistrationAdmin)


class driveroperatorregistrationAdmin(admin.ModelAdmin):
    list_display = ['Id', 'vehicalname', 'expriencesinyear', 'driveroperatorname', 'alternet_mobilenumber', 'heavy_license','driver_image']
admin.site.register(driveroperatorregistration, driveroperatorregistrationAdmin)


from django.contrib import admin
from user.models import MasterContents, Device,Request_labour_contructor, Request_SubContractor, labour_contructor, heavyvehivalregistration,Request_driver_Operator,Request_Heavy_Vehical, driveroperatorregistration, subcontractorregistration, Requirement


admin.site.register(Request_driver_Operator)
admin.site.register(Request_labour_contructor)
admin.site.register(Request_SubContractor)


class requestrequirementAdmin(admin.ModelAdmin):
    list_display = ['Id', 'title', 'description', 'requirement_image']
admin.site.register(Requirement,requestrequirementAdmin)


class reqeustheavyvehicalAdmin(admin.ModelAdmin):
    list_display = ['Id', 'vehicle_name','company_name', 'vehicle_number', 'model_number', 'ownername', 'Aadhar_number','vehicle_image','manufectoring_date',]

admin.site.register(Request_Heavy_Vehical,reqeustheavyvehicalAdmin)


#admin.site.register(subcontractorregistration)



class labourcontractoradmin(admin.ModelAdmin):
    list_display = ['Id','labourcontractorname', 'labourwork', 'lobourinnumber', 'mobile_number', 'contractorAadhar_number', 'created_by', 'is_active']

admin.site.register(labour_contructor,labourcontractoradmin)

class heavyvehivalregistrationAdmin(admin.ModelAdmin):
    list_display = ['Id', 'vehical_name', 'vehical_number', 'model_number', 'ownername', 'Aadhar_number', 'vehicle_image']

admin.site.register(heavyvehivalregistration,heavyvehivalregistrationAdmin)


class subcontractorregistrationAdmin(admin.ModelAdmin):
    list_display = ['Id', 'contractorname', 'firmname', 'expriencesinyear', 'license_number', 'Aadhar_number', 'subcontractor_image',]
admin.site.register(subcontractorregistration, subcontractorregistrationAdmin)


class driveroperatorregistrationAdmin(admin.ModelAdmin):
    list_display = ['Id', 'vehicalname', 'expriencesinyear', 'driveroperatorname', 'Aadhar_number', 'alternet_mobilenumber', 'license_number','driver_image']
admin.site.register(driveroperatorregistration, driveroperatorregistrationAdmin)




# class mastercontentsAdmin(admin.ModelAdmin):
#     list_display = ['Id', 'key', 'value', 'relate_to']
#admin.site.register(MasterContents, mastercontentsAdmin)

# class deviceAdmin(admin.ModelAdmin):
#     list_display = ['device_id', 'refresh_token', 'device_type', 'aws_arn', 'created_by', 'created_at','is_active']

#admin.site.register(Device)

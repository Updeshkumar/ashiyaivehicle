from django.db import models
from rest_framework import status
from config.configConstants import UserType



class MasterContents(models.Model):
    Id = models.AutoField(primary_key=True)
    key = models.CharField(max_length = 200)
    value = models.CharField(max_length = 200)
    relate_to = models.IntegerField()
    class Meta:
        db_table = 'user_mastercontents'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    country_code = models.IntegerField(91, null=True,blank=True)
    mobile_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=4,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(default=False, null=True)
    email_id = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=20,null=False,blank=False, default="USER")
    profile_pic = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=1,null=False)
    is_delete = models.BooleanField(default=0,null=False)
    gender = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'user'

#  This class is use for create the preference model
class Device(models.Model):

    device_id = models.AutoField(primary_key=True)
    refresh_token = models.CharField(max_length=500,default=False, null=True)
    device_type = models.CharField(max_length=20)
    device_token = models.CharField(max_length=255,default=False, null=True)
    aws_arn = models.CharField(max_length=255, null=True)
    created_by =  models.ForeignKey(User, db_column = 'created_by',related_name='device_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1,null=False)
    
    class Meta:
        db_table = 'device'


#  labour contracot registrations

class labour_contructor(models.Model):
    Id = models.AutoField(primary_key=True)
    labourcontractorname = models.CharField(max_length=300)
    labourwork = models.CharField(max_length=200)
    emailId = models.CharField(max_length=100)
    lobourinnumber = models.CharField(max_length=500)
    mobile_number = models.CharField(max_length=12)
    skilledlabour =  models.IntegerField(null=False,blank=False)
    unskilledlabour = models.IntegerField(blank=False)
    professionallabour = models.IntegerField(null=False)
    Aadharnumberfrontimage = models.CharField(max_length=25)
    alternativemobilenumber = models.CharField(max_length=15)
    Aadharnumberbackimage = models.CharField(max_length=25)
    labour_image = models.CharField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)


    class Meta:
        db_table = 'labour_contructor'


class heavyvehicleaddress(models.Model):
    Id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    state_id = models.IntegerField()
    district_id = models.IntegerField()
    city_id = models.IntegerField()
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)
    

    class Meta:
        db_table = 'heavyvehicleaddress'


class upload_lobour_document(models.Model):
    Id = models.AutoField(primary_key=True)
    labourgroupphoto = models.CharField(max_length=255, blank=True, null=True)
    uploadlabourphoto = models.CharField(max_length=255, blank=True, null=True)
    uploadaadharcard = models.CharField(max_length=255, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)


    class Meta:
        db_table = "upload_lobour_document"


################ Normal User Registration ########
class NormalUser(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)



    class Meta:
        db_table = "normaluser"


            # ###################Heavy Vehical Registrations #####################


class heavyvehivalregistration(models.Model):
    Id = models.AutoField(primary_key=True, )
    vehical_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length = 100)
    emailId = models.CharField(max_length=50)
    ownername = models.CharField(max_length=300)
    vehicleregistrationnumber = models.CharField(max_length=20)
    Aadharnumberfrontimage = models.CharField(max_length=250)
    Aadharnumberbackimage = models.CharField(max_length=250)
    vehicle_image = models.FileField(max_length=1000)
    manufacture_date = models.CharField(max_length=100)
    alternativemobilenumber = models.CharField(max_length=20)
    vehiclemodelnumber = models.CharField(max_length=100)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "heavyvehivalregistration"




class heavyvehicaladdressupload(models.Model):
    Id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    houseblockstreet = models.CharField(max_length=100)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)
    

    class Meta:
        db_table = 'heavyvehicaladdressupload'


class heavyvehicaldocumentupload(models.Model):
    Id = models.AutoField(primary_key=True)
    uploadvehicalphoto = models.CharField(max_length=255, blank=True, null=True)
    uploadaadharcard = models.CharField(max_length=255, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "heavyvehicaldocumentupload"


#############driver operator registrations class #####################

class driveroperatorregistration(models.Model):
    Id = models.AutoField(primary_key=True, )
    vehicalname = models.CharField(max_length=200)
    expriencesinyear = models.IntegerField(blank=False, null=False)
    driveroperatorname = models.CharField(max_length=200)
    Aadharnumberfrontimage = models.CharField(max_length=25)
    Aadharnumberbackimage = models.CharField(max_length=25)
    alternet_mobilenumber = models.IntegerField()
    heavy_license = models.CharField(max_length=50)
    emailId = models.CharField(max_length=50)
    mobilenumber = models.CharField(max_length=20)
    license_image = models.CharField(max_length=500)
    driver_image = models.CharField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "driveroperatorregistration"

#############Sub contractor  registrations class #####################

class subcontractorregistration(models.Model):
    Id = models.AutoField(primary_key=True, )
    contractorname = models.CharField(max_length=100)
    firmname = models.CharField(max_length=500)
    typeofwork = models.CharField(max_length=100)
    emailId = models.CharField(max_length=50)
    expriencesinyear = models.IntegerField(blank=False, null=False)
    license_number = models.CharField(max_length=50)
    Aadharnumberfrontimage = models.CharField(max_length=25)
    Aadharnumberbackimage = models.CharField(max_length=25)
    mobilenumber = models.CharField(max_length=20)
    subcontractor_image = models.FileField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "subcontractorregistration"
        

class Request_SubContractor(models.Model):
    Id = models.AutoField(primary_key=True, )
    contractorname = models.CharField(max_length=100)
    firmname = models.CharField(max_length=500) 
    typeofwork = models.CharField(max_length=100)
    expriencesinyear = models.IntegerField(blank=False, null=False)
    license_number = models.CharField(max_length=50)
    emailId = models.CharField(max_length=100)
    Aadharnumberfrontimage = models.CharField(max_length=25)
    Aadharnumberbackimage = models.CharField(max_length=25)
    mobilenumber = models.CharField(max_length=20)
    subcontractor_image = models.FileField(max_length=500, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)
    class Meta:
        db_table = "request_subcontractor"
        
        
class Requirement(models.Model):
    Id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    requirement_image = models.CharField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    #image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "requirement"
        
class VedioUplaod(models.Model):
    Id = models.AutoField(primary_key=True)
    image_uplaod = models.CharField(max_length=500)
    vediourl = models.CharField(max_length=100)
    class Meta:
        db_table = "vedioupload"


        
        
################# Request Api ###############

class Request_Heavy_Vehical(models.Model):
    Id = models.AutoField(primary_key=True, )
    vehical_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    vehical_number = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    vehicleregistrationnumber = models.CharField(max_length=100)
    ownername = models.CharField(max_length=300)
    Aadharnumberfrontimage = models.CharField(max_length=25)
    Aadharnumberbackimage = models.CharField(max_length=25)
    vehicle_image =  models.FileField(max_length=255, blank=True, null=True)
    manufacture_date = models.CharField(max_length=100)
    alternativemobilenumber = models.CharField(max_length=20)
    vehiclemodelnumber = models.CharField(max_length=50)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "request_heavy_vehical"
        
class Request_labour_contructor(models.Model):
    Id = models.AutoField(primary_key=True)
    labourcontractorname = models.CharField(max_length=300)
    labourwork = models.CharField(max_length=200)
    emailId = models.CharField(max_length=100)
    skilled_labour = models.IntegerField()
    professional_labour = models.IntegerField()
    unskilled_labour = models.IntegerField()
    lobourinnumber = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=20)
    alternativemobilenumber = models.CharField(max_length=20)
    contractorAadhar_number = models.CharField(max_length=20)
    Aadharnumberfrontimage = models.CharField(max_length=25)
    Aadharnumberbackimage = models.CharField(max_length=25)
    labour_image = models.CharField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)


    class Meta:
        db_table = 'request_labour_contructor'
        
class Request_driver_Operator(models.Model):
    Id = models.AutoField(primary_key=True, )
    vehicalname = models.CharField(max_length=200)
    expriencesinyear = models.IntegerField(blank=False, null=False)
    driveroperatorname = models.CharField(max_length=200)
    emailId = models.CharField(max_length=100)

    Aadharnumberfrontimage = models.CharField(max_length=25)
    Aadharnumberbackimage = models.CharField(max_length=25)
    mobilenumber = models.CharField(max_length=20)
    alternet_mobilenumber = models.IntegerField()
    license_number = models.CharField(max_length=50)
    driver_image = models.CharField(max_length=500, blank=True, null=True)
    license_image = models.CharField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "request_driver_operator"


class insertrecordsp(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


    class Meta:
        db_table = "emptable"
        

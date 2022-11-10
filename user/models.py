from django.db import models
from rest_framework import status
from config.configConstants import UserType

# Create your models here.

# This class is used to create the User model
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
    #device_token = models.CharField(max_length=255,default=False, null=True)
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
    lobourinnumber = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=20)
    contractorAadhar_number = models.CharField(max_length=20)
    labour_image = models.CharField(max_length=500,blank=True, null=True)

    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)


    class Meta:
        db_table = 'labour_contructor'


class user_address(models.Model):
    Id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    houseblockstreet = models.CharField(max_length=100)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)
    

    class Meta:
        db_table = 'user_address'


class upload_lobour_document(models.Model):
    Id = models.AutoField(primary_key=True)
    labourgroupphoto = models.CharField(max_length=255, blank=True, null=True)
    uploadlabourphoto = models.CharField(max_length=255, blank=True, null=True)
    uploadaadharcard = models.CharField(max_length=255, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)


    class Meta:
        db_table = "upload_lobour_document"


            # ###################Heavy Vehical Registrations #####################


class heavyvehivalregistration(models.Model):
    Id = models.AutoField(primary_key=True, )
    vehical_name = models.CharField(max_length=200)
    vehical_number = models.CharField(max_length=500)
    model_number = models.CharField(max_length=500)
    ownername = models.CharField(max_length=300)
    Aadhar_number = models.CharField(max_length=20)
    vehicle_image = models.CharField(max_length=500)

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
    Aadhar_number = models.CharField(max_length=20)
    alternet_mobilenumber = models.IntegerField()
    license_number = models.CharField(max_length=50)
    driver_image = models.FileField(max_length=500, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "driveroperatorregistration"

#############Sub contractor  registrations class #####################

class subcontractorregistration(models.Model):
    Id = models.AutoField(primary_key=True, )
    contractorname = models.CharField(max_length=100)
    firmname = models.CharField(max_length=500)
    expriencesinyear = models.IntegerField(blank=False, null=False)
    license_number = models.CharField(max_length=50)
    Aadhar_number = models.CharField(max_length=20)
    subcontractor_image = models.CharField(max_length=500, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "subcontractorregistration"


################# Request Api ###############

class Request_Heavy_Vehical(models.Model):
    Id = models.AutoField(primary_key=True, )
    vehical_name = models.CharField(max_length=200)
    vehical_number = models.CharField(max_length=500)
    model_number = models.CharField(max_length=500)
    ownername = models.CharField(max_length=300)
    Aadhar_number = models.CharField(max_length=20)
    image =  models.CharField(max_length=255, blank=True, null=True)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    class Meta:
        db_table = "Request_Heavy_Vehical"


class Requirement(models.Model):
    Id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_by =  models.IntegerField()
    is_active = models.BooleanField(default=1,null=False)

    #image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "requirement"




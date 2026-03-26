# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Countries(models.Model):
    country_id = models.TextField(primary_key=True)
    country_name = models.TextField()
    region = models.ForeignKey('Regions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.TextField()
    location = models.ForeignKey('Locations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departments'


class Dependents(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    relationship = models.TextField()
    employee = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dependents'


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField()
    email = models.TextField()
    phone_number = models.TextField(blank=True, null=True)
    hire_date = models.TextField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.TextField()  # This field type is a guess.
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employees'


# class Jobs(models.Model):
#     job_id = models.AutoField(primary_key=True)
#     job_title = models.TextField()
#     min_salary = models.TextField()
#     max_salary = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'jobs'

from django.db import models


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)

    # Asosiy ma'lumotlar
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()

    # Kompaniya ma'lumotlari
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)

    # Ish turi
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('remote', 'Remote'),
        ('internship', 'Internship'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    # Maosh
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    currency = models.CharField(max_length=10, default='USD')

    # Talablar
    requirements = models.TextField()
    experience_level = models.CharField(max_length=100)  # Junior, Mid, Senior

    # Sana va holat
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # Qo‘shimcha
    contact_email = models.EmailField()
    website = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'jobs'
        ordering = ['-posted_at']


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    city = models.TextField()
    state_province = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locations'


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'regions'

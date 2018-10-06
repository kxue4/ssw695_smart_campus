from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        db_table = 'auth_group'
        managed = False


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_group_permissions'
        managed = False
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'
        managed = False


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user_groups'
        managed = False
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user_user_permissions'
        managed = False
        unique_together = (('user', 'permission'),)


class Airquality(models.Model):
    id = models.IntegerField(primary_key=True)
    air_quality_level = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_airquality'


class Campusbuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    building_name = models.CharField(max_length=120)
    created_at = models.DateTimeField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_campusbuilding'


class Decibel(models.Model):
    id = models.IntegerField(primary_key=True)
    decibel_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_decibel'


class Humidity(models.Model):
    id = models.IntegerField(primary_key=True)
    humidity_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_humidity'


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = 'core_location'


class Pressure(models.Model):
    id = models.IntegerField(primary_key=True)
    pressure_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_pressure'


class Sensortype(models.Model):
    id = models.IntegerField(primary_key=True)
    sensor_type = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = 'core_sensortype'


class Singleboardcomputer(models.Model):
    id = models.IntegerField(primary_key=True)
    single_board_computer_name = models.CharField(max_length=220)
    operating_system = models.CharField(max_length=220)
    address = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    single_board_computer_type_id = models.ForeignKey('Singleboardcomputertype', on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_singleboardcomputer'


class Singleboardcomputertype(models.Model):
    id = models.IntegerField(primary_key=True)
    computer_type = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = 'core_singleboardcomputertype'


class Temperature(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_temperature'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=220)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'core_user'


class Data(models.Model):
    mac = models.CharField(max_length=17, blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    pres = models.FloatField(blank=True, null=True)
    hum = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)
    db = models.FloatField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


class Zerodata(models.Model):
    mac = models.CharField(max_length=17, blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    pres = models.FloatField(blank=True, null=True)
    hum = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)
    db = models.FloatField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zeroData'

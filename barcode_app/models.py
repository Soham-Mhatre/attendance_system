from django.db import models

class Barcode(models.Model):
    data = models.CharField(max_length=255)
    scanned_at = models.DateTimeField(auto_now_add=True)


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class TimeSlot(models.Model):
    name = models.CharField(max_length=50)
    day = models.CharField(max_length=10, default='Monday')
    start_time = models.TimeField()
    end_time = models.TimeField()


class SGs1s2(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Sg0001s101s102(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
def create_dynamic_table(table_name):
    class DynamicSG(models.Model):
        name = models.CharField(max_length=100)
        rollno = models.CharField(max_length=100)
        present = models.BooleanField(default=False)

        def __str__(self):
            return self.name

    DynamicSG._meta.db_table = table_name
    return DynamicSG

from django.db import models

class DynamicTable(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=10)
    present=models.BooleanField()

    def __str__(self):
        return self.name

class barcode_app_sg0001s5s6(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class barcode_app_s3s4(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class s3s4(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Rb0002s13s14(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Rb0002s91s92(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
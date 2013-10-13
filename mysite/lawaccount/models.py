from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

tablePrefix = "LA_"

SEX_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)

class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name = 'Last Name')
    mobile_number = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    nric_fin = models.CharField(max_length=10, verbose_name='NRIC/FIN')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = tablePrefix + "client"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('lawaccount:clientListView')


class ServiceLog(models.Model):
    client = models.ForeignKey(Client)
    log_subject = models.CharField(max_length=50, verbose_name='Service')
    log_desc = models.TextField(verbose_name="Description")
    srvc_charge = models.DecimalField(verbose_name='Charge Amount',max_digits=19,decimal_places=2)
    gst_amount = models.DecimalField(verbose_name='GST Amount',max_digits=19,decimal_places=2)
    start_date = models.DateField(verbose_name="Service Start Date")
    end_date = models.DateField(verbose_name='Service End Date')
    svc_status = models.CharField(verbose_name='Status', max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = tablePrefix + "servicelog"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.start_date + ' ' + self.log_subject

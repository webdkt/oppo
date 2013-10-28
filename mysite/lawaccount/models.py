from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

tablePrefix = "LA_"

SEX_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)

ACC_TYPE = (
    ('I',"Individual"),
    ('C','Corporate')
)




class Account(models.Model):
    acc_name = models.CharField(max_length=100,verbose_name='Account Name')
    acc_type = models.CharField(max_length=1,verbose_name='Account Type',choices=ACC_TYPE)
    primary_phone = models.CharField(max_length=20,verbose_name='Primary Phone',blank=True)
    address1 = models.CharField(max_length=100,verbose_name='Address 1',blank=True)
    address2 = models.CharField(max_length=100,verbose_name='Address 2',blank=True)
    postal_code = models.CharField(max_length=10,verbose_name='Postal Code',blank=True)
    email = models.CharField(max_length=100,verbose_name='Email',blank=True)
    fax = models.CharField(max_length=20,verbose_name='Fax',blank=True)
    website = models.CharField(max_length=100,verbose_name='Website',blank=True)
    reg_no = models.CharField(max_length=50,verbose_name='Registration No',blank=True)
    industry = models.CharField(max_length=50,verbose_name='Industry',blank=True)
    employee_num = models.CharField(max_length=20,verbose_name='# of Employee',blank=True)
    first_name = models.CharField(max_length=50, verbose_name='First Name',blank=True)
    last_name = models.CharField(max_length=50, verbose_name = 'Last Name',blank=True)
    mobile = models.CharField(max_length=50, verbose_name = 'Mobile',blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,verbose_name='Gender',blank=True)
    nric_fin = models.CharField(max_length=10, verbose_name='NRIC/FIN',blank=True)
    home_phone = models.CharField(max_length=20,verbose_name='Primary Phone',blank=True)
    country = models.CharField(max_length=50,verbose_name='Country',blank=True)
    title = models.CharField(max_length=10,verbose_name='Title',blank=True)
    job_title = models.CharField(max_length=10,verbose_name='Job Title',blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = tablePrefix + "account"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.acc_name

    def get_absolute_url(self):
        return reverse('lawaccount:accountListView')



class Contact(models.Model):
    account = models.ForeignKey(Account)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name = 'Last Name')
    mobile = models.CharField(max_length=50, verbose_name = 'Mobile')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name='Gender')
    nric_fin = models.CharField(max_length=10, verbose_name='NRIC/FIN')
    home_phone = models.CharField(max_length=20,verbose_name='Primary Phone')
    country = models.CharField(max_length=50,verbose_name='Country')
    title = models.CharField(max_length=10,verbose_name='Title')
    job_title = models.CharField(max_length=50,verbose_name='Job Title')
    primary_phone = models.CharField(max_length=20,verbose_name='Primary Phone')

    class Meta:
        db_table = tablePrefix + "contact"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first_name + ' ' + self.last_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Product Name')
    catagory_name = models.CharField(max_length=20, verbose_name='Catagory')
    unit_price = models.DecimalField(verbose_name='Unit Price', max_digits=19,decimal_places=2)
    description = models.TextField(verbose_name='Desciprtion')
    status = models.CharField(max_length=10, verbose_name='Status')

    class Meta:
        db_table = tablePrefix + "product"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.product_name


class Invoice(models.Model):
    account = models.ForeignKey(Account)
    inovice_no = models.CharField(max_length=30, verbose_name="Invoice No.",primary_key = True)
    invoice_date = models.DateField(verbose_name="Invoice Date")
    description = models.CharField(max_length=200, verbose_name='Description')
    status = models.TextField(verbose_name="Status")
    amount = models.DecimalField(verbose_name='Total Amount',max_digits=19,decimal_places=2)
    gst_amount = models.DecimalField(verbose_name='GST Amount',max_digits=19,decimal_places=2)
    total_adjustment =  models.DecimalField(verbose_name = 'Adjustment', max_digits=19, decimal_places=2)
    sum_amount = models.DecimalField(verbose_name='Total Summary',max_digits=19,decimal_places=2)
    payment_status = models.CharField(max_length=20, verbose_name = 'Payment Status')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Product, through='InvoiceItem')

    class Meta:
        db_table = tablePrefix + "invoice"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.inovice_no



class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice)
    item = models.ForeignKey(Product)
    sequence_no = models.IntegerField(verbose_name='#')
    quantity = models.IntegerField(verbose_name = 'Quantity')
    discount = models.DecimalField(verbose_name = 'Discount', max_digits=3, decimal_places=2)
    adjustment = models.DecimalField(verbose_name = 'Adjustment', max_digits=19, decimal_places=2)
    product_name = models.CharField(max_length=100, verbose_name='Product Name')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = tablePrefix + "invoiceitem"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.id + '(' + self.sequence_no + ')'

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

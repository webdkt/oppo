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

RACES = (
    ('Caucasian',"Caucasian"),
    ('Chinese','Chinese'),
    ('Indian',"Indian"),
    ('Malay','Malay'),
    ('Others','Others'),
)

COUNTRY = (
    ('Afghanistan',                           'Afghanistan'),
    ('AlandIslands',                          'AlandIslands'),
    ('Albania',                               'Albania'),
    ('Algeria',                               'Algeria'),
    ('AmericanSamoa',                         'AmericanSamoa'),
    ('Andorra',                               'Andorra'),
    ('Angola',                                'Angola'),
    ('Anguilla',                              'Anguilla'),
    ('Antarctica',                            'Antarctica'),
    ('AntiguaandBarbuda',                     'AntiguaandBarbuda'),
    ('Argentina',                             'Argentina'),
    ('Armenia',                               'Armenia'),
    ('Aruba',                                 'Aruba'),
    ('Australia',                             'Australia'),
    ('Austria',                               'Austria'),
    ('Azerbaijan',                            'Azerbaijan'),
    ('Bahamas',                               'Bahamas'),
    ('Bahrain',                               'Bahrain'),
    ('Bangladesh',                            'Bangladesh'),
    ('Barbados',                              'Barbados'),
    ('Belarus',                               'Belarus'),
    ('Belgium',                               'Belgium'),
    ('Belize',                                'Belize'),
    ('Benin',                                 'Benin'),
    ('Bermuda',                               'Bermuda'),
    ('Bhutan',                                'Bhutan'),
    ('Bolivia,PlurinationalStateof',          'Bolivia,PlurinationalStateof'),
    ('Bonaire,SintEustatiusandSaba',          'Bonaire,SintEustatiusandSaba'),
    ('Bosniaand Herzegovina',                  'Bosniaand Herzegovina'),
    ('Botswana',                              'Botswana'),
    ('BouvetIsland',                          'BouvetIsland'),
    ('Brazil',                                'Brazil'),
    ('British Indian Ocean Territory',           'British Indian Ocean Territory'),
    ('Brunei Darussalam',                      'Brunei Darussalam'),
    ('Bulgaria',                              'Bulgaria'),
    ('BurkinaFaso',                           'BurkinaFaso'),
    ('Burundi',                               'Burundi'),
    ('Cambodia',                              'Cambodia'),
    ('Cameroon',                              'Cameroon'),
    ('Canada',                                'Canada'),
    ('CapeVerde',                             'CapeVerde'),
    ('CaymanIslands',                         'CaymanIslands'),
    ('CentralAfricanRepublic',                'CentralAfricanRepublic'),
    ('Chad',                                  'Chad'),
    ('Chile',                                 'Chile'),
    ('China',                                 'China'),
    ('ChristmasIsland',                       'ChristmasIsland'),
    ('Cocos(Keeling)Islands',                 'Cocos(Keeling)Islands'),
    ('Colombia',                              'Colombia'),
    ('Comoros',                               'Comoros'),
    ('Congo',                                 'Congo'),
    ('Congo,TheDemocraticRepublicofThe',      'Congo,TheDemocraticRepublicofThe'),
    ('CookIslands',                           'CookIslands'),
    ('CostaRica',                             'CostaRica'),
    ("CoteD'ivoire",                          "CoteD'ivoire"),
    ('Croatia',                               'Croatia'),
    ('Cuba',                                  'Cuba'),
    ('Curacao',                               'Curacao'),
    ('Cyprus',                                'Cyprus'),
    ('CzechRepublic',                         'CzechRepublic'),
    ('Denmark',                               'Denmark'),
    ('Djibouti',                              'Djibouti'),
    ('Dominica',                              'Dominica'),
    ('DominicanRepublic',                     'DominicanRepublic'),
    ('Ecuador',                               'Ecuador'),
    ('Egypt',                                 'Egypt'),
    ('ElSalvador',                            'ElSalvador'),
    ('EquatorialGuinea',                      'EquatorialGuinea'),
    ('Eritrea',                               'Eritrea'),
    ('Estonia',                               'Estonia'),
    ('Ethiopia',                              'Ethiopia'),
    ('FalklandIslands(Malvinas)',             'FalklandIslands(Malvinas)'),
    ('FaroeIslands',                          'FaroeIslands'),
    ('Fiji',                                  'Fiji'),
    ('Finland',                               'Finland'),
    ('France',                                'France'),
    ('FrenchGuiana',                          'FrenchGuiana'),
    ('FrenchPolynesia',                       'FrenchPolynesia'),
    ('FrenchSouthernTerritories',             'FrenchSouthernTerritories'),
    ('Gabon',                                 'Gabon'),
    ('Gambia',                                'Gambia'),
    ('Georgia',                               'Georgia'),
    ('Germany',                               'Germany'),
    ('Ghana',                                 'Ghana'),
    ('Gibraltar',                             'Gibraltar'),
    ('Greece',                                'Greece'),
    ('Greenland',                             'Greenland'),
    ('Grenada',                               'Grenada'),
    ('Guadeloupe',                            'Guadeloupe'),
    ('Guam',                                  'Guam'),
    ('Guatemala',                             'Guatemala'),
    ('Guernsey',                              'Guernsey'),
    ('Guinea',                                'Guinea'),
    ('Guinea-bissau',                         'Guinea-bissau'),
    ('Guyana',                                'Guyana'),
    ('Haiti',                                 'Haiti'),
    ('HeardIslandandMcdonaldIslands',         'HeardIslandandMcdonaldIslands'),
    ('HolySee(VaticanCityState)',             'HolySee(VaticanCityState)'),
    ('Honduras',                              'Honduras'),
    ('HongKong',                              'HongKong'),
    ('Hungary',                               'Hungary'),
    ('Iceland',                               'Iceland'),
    ('India',                                 'India'),
    ('Indonesia',                             'Indonesia'),
    ('Iran,IslamicRepublicof',                'Iran,IslamicRepublicof'),
    ('Iraq',                                  'Iraq'),
    ('Ireland',                               'Ireland'),
    ('IsleofMan',                             'IsleofMan'),
    ('Israel',                                'Israel'),
    ('Italy',                                 'Italy'),
    ('Jamaica',                               'Jamaica'),
    ('Japan',                                 'Japan'),
    ('Jersey',                                'Jersey'),
    ('Jordan',                                'Jordan'),
    ('Kazakhstan',                            'Kazakhstan'),
    ('Kenya',                                 'Kenya'),
    ('Kiribati',                              'Kiribati'),
    ("Korea,DemocraticPeople'sRepublicof",    "Korea,DemocraticPeople'sRepublicof"),
    ('Korea,Republicof',                      'Korea,Republicof'),
    ('Kuwait',                                'Kuwait'),
    ('Kyrgyzstan',                            'Kyrgyzstan'),
    ("LaoPeople'sDemocraticRepublic",         "LaoPeople'sDemocraticRepublic"),
    ('Latvia',                                'Latvia'),
    ('Lebanon',                               'Lebanon'),
    ('Lesotho',                               'Lesotho'),
    ('Liberia',                               'Liberia'),
    ('Libya',                                 'Libya'),
    ('Liechtenstein',                         'Liechtenstein'),
    ('Lithuania',                             'Lithuania'),
    ('Luxembourg',                            'Luxembourg'),
    ('Macao',                                 'Macao'),
    ('Macedonia,TheFormerYugoslavRepublicof', 'Macedonia,TheFormerYugoslavRepublicof'),
    ('Madagascar',                            'Madagascar'),
    ('Malawi',                                'Malawi'),
    ('Malaysia',                              'Malaysia'),
    ('Maldives',                              'Maldives'),
    ('Mali',                                  'Mali'),
    ('Malta',                                 'Malta'),
    ('MarshallIslands',                       'MarshallIslands'),
    ('Martinique',                            'Martinique'),
    ('Mauritania',                            'Mauritania'),
    ('Mauritius',                             'Mauritius'),
    ('Mayotte',                               'Mayotte'),
    ('Mexico',                                'Mexico'),
    ('Micronesia,FederatedStatesof',          'Micronesia,FederatedStatesof'),
    ('Moldova,Republicof',                    'Moldova,Republicof'),
    ('Monaco',                                'Monaco'),
    ('Mongolia',                              'Mongolia'),
    ('Montenegro',                            'Montenegro'),
    ('Montserrat',                            'Montserrat'),
    ('Morocco',                               'Morocco'),
    ('Mozambique',                            'Mozambique'),
    ('Myanmar',                               'Myanmar'),
    ('Namibia',                               'Namibia'),
    ('Nauru',                                 'Nauru'),
    ('Nepal',                                 'Nepal'),
    ('Netherlands',                           'Netherlands'),
    ('NewCaledonia',                          'NewCaledonia'),
    ('NewZealand',                            'NewZealand'),
    ('Nicaragua',                             'Nicaragua'),
    ('Niger',                                 'Niger'),
    ('Nigeria',                               'Nigeria'),
    ('Niue',                                  'Niue'),
    ('NorfolkIsland',                         'NorfolkIsland'),
    ('NorthernMarianaIslands',                'NorthernMarianaIslands'),
    ('Norway',                                'Norway'),
    ('Oman',                                  'Oman'),
    ('Pakistan',                              'Pakistan'),
    ('Palau',                                 'Palau'),
    ('PalestinianTerritory,Occupied',         'PalestinianTerritory,Occupied'),
    ('Panama',                                'Panama'),
    ('PapuaNewGuinea',                        'PapuaNewGuinea'),
    ('Paraguay',                              'Paraguay'),
    ('Peru',                                  'Peru'),
    ('Philippines',                           'Philippines'),
    ('Pitcairn',                              'Pitcairn'),
    ('Poland',                                'Poland'),
    ('Portugal',                              'Portugal'),
    ('PuertoRico',                            'PuertoRico'),
    ('Qatar',                                 'Qatar'),
    ('Reunion',                               'Reunion'),
    ('Romania',                               'Romania'),
    ('RussianFederation',                     'RussianFederation'),
    ('Rwanda',                                'Rwanda'),
    ('SaintBarthelemy',                       'SaintBarthelemy'),
    ('SaintHelena,AscensionandTristandaCunha','SaintHelena,AscensionandTristandaCunha'),
    ('SaintKittsandNevis',                    'SaintKittsandNevis'),
    ('SaintLucia',                            'SaintLucia'),
    ('SaintMartin(Frenchpart)',               'SaintMartin(Frenchpart)'),
    ('SaintPierreandMiquelon',                'SaintPierreandMiquelon'),
    ('SaintVincentandTheGrenadines',          'SaintVincentandTheGrenadines'),
    ('Samoa',                                 'Samoa'),
    ('SanMarino',                             'SanMarino'),
    ('SaoTomeandPrincipe',                    'SaoTomeandPrincipe'),
    ('SaudiArabia',                           'SaudiArabia'),
    ('Senegal',                               'Senegal'),
    ('Serbia',                                'Serbia'),
    ('Seychelles',                            'Seychelles'),
    ('SierraLeone',                           'SierraLeone'),
    ('Singapore',                             'Singapore'),
    ('SintMaarten(Dutchpart)',                'SintMaarten(Dutchpart)'),
    ('Slovakia',                              'Slovakia'),
    ('Slovenia',                              'Slovenia'),
    ('SolomonIslands',                        'SolomonIslands'),
    ('Somalia',                               'Somalia'),
    ('SouthAfrica',                           'SouthAfrica'),
    ('SouthGeorgiaandTheSouthSandwichIslands','SouthGeorgiaandTheSouthSandwichIslands'),
    ('SouthSudan',                            'SouthSudan'),
    ('Spain',                                 'Spain'),
    ('SriLanka',                              'SriLanka'),
    ('Sudan',                                 'Sudan'),
    ('Suriname',                              'Suriname'),
    ('SvalbardandJanMayen',                   'SvalbardandJanMayen'),
    ('Swaziland',                             'Swaziland'),
    ('Sweden',                                'Sweden'),
    ('Switzerland',                           'Switzerland'),
    ('SyrianArabRepublic',                    'SyrianArabRepublic'),
    ('Taiwan,ProvinceofChina',                'Taiwan,ProvinceofChina'),
    ('Tajikistan',                            'Tajikistan'),
    ('Tanzania,UnitedRepublicof',             'Tanzania,UnitedRepublicof'),
    ('Thailand',                              'Thailand'),
    ('Timor-leste',                           'Timor-leste'),
    ('Togo',                                  'Togo'),
    ('Tokelau',                               'Tokelau'),
    ('Tonga',                                 'Tonga'),
    ('TrinidadandTobago',                     'TrinidadandTobago'),
    ('Tunisia',                               'Tunisia'),
    ('Turkey',                                'Turkey'),
    ('Turkmenistan',                          'Turkmenistan'),
    ('TurksandCaicosIslands',                 'TurksandCaicosIslands'),
    ('Tuvalu',                                'Tuvalu'),
    ('Uganda',                                'Uganda'),
    ('Ukraine',                               'Ukraine'),
    ('UnitedArabEmirates',                    'UnitedArabEmirates'),
    ('UnitedKingdom',                         'UnitedKingdom'),
    ('UnitedStates',                          'UnitedStates'),
    ('UnitedStatesMinorOutlyingIslands',      'UnitedStatesMinorOutlyingIslands'),
    ('Uruguay',                               'Uruguay'),
    ('Uzbekistan',                            'Uzbekistan'),
    ('Vanuatu',                               'Vanuatu'),
    ('Venezuela,BolivarianRepublicof',        'Venezuela,BolivarianRepublicof'),
    ('VietNam',                               'VietNam'),
    ('VirginIslands,British',                 'VirginIslands,British'),
    ('VirginIslands,U.S.',                    'VirginIslands,U.S.'),
    ('WallisandFutuna',                       'WallisandFutuna'),
    ('WesternSahara',                         'WesternSahara'),
    ('Yemen',                                 'Yemen'),
    ('Zambia',                                'Zambia'),
    ('Zimbabwe',                              'Zimbabwe'),


)


class Customer(models.Model):
    NAME_PREFIX = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
    )

    M_STATUS = (
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
        ('Widowed','Widowed'),
        ('Other','Other'),
    )

    nric = models.CharField(max_length=10,verbose_name='NRIC/FIN')
    nationality = models.CharField(max_length=30,verbose_name='Nationality',choices=COUNTRY)
    first_name = models.CharField(max_length=30,verbose_name='First Name')
    last_name = models.CharField(max_length=30,verbose_name='Last Name')
    middle_name = models.CharField(max_length=30,verbose_name='Middle Name',blank=True)
    birth_date = models.DateField(max_length=30,verbose_name='Date of Birth',blank=True)
    sex = models.CharField(max_length=1,verbose_name='Sex',blank=True,choices=SEX_CHOICES)
    prefix = models.CharField(max_length=10,verbose_name='Title',blank=True,choices=NAME_PREFIX)
    employer= models.CharField(max_length=50,verbose_name='Employer',blank=True)
    occupation= models.CharField(max_length=50,verbose_name='Occupation',blank=True)
    race= models.CharField(max_length=30,verbose_name='race',blank=True, choices=RACES)
    maritial_status= models.CharField(max_length=15,verbose_name='Maritial Status',blank=True,choices=M_STATUS)
    home_address1= models.CharField(max_length=50,verbose_name='Address',blank=True)
    home_address2= models.CharField(max_length=50,verbose_name='',blank=True)
    home_city= models.CharField(max_length=50,verbose_name='City',blank=True)
    home_country= models.CharField(max_length=50,verbose_name='Country',blank=True,choices=COUNTRY)
    home_zip= models.CharField(max_length=10,verbose_name='ZIP',blank=True)
    home_phone= models.CharField(max_length=30,verbose_name='Phone',blank=True)
    office_address1= models.CharField(max_length=50,verbose_name='Address',blank=True)
    office_address2= models.CharField(max_length=50,verbose_name='',blank=True)
    office_city= models.CharField(max_length=50,verbose_name='City',blank=True)
    office_country= models.CharField(max_length=50,verbose_name='Country',blank=True, choices=COUNTRY)
    office_zip= models.CharField(max_length=10,verbose_name='ZIP',blank=True)
    office_phone= models.CharField(max_length=30,verbose_name='Phone',blank=True)
    mobile_phone1= models.CharField(max_length=30,verbose_name='Mobile',blank=True)
    mobile_phone2= models.CharField(max_length=30,verbose_name='Alternative Mobile',blank=True)
    personal_fax= models.CharField(max_length=30,verbose_name='FAX',blank=True)
    personal_email= models.CharField(max_length=30,verbose_name='Personal Email',blank=True)
    office_email= models.CharField(max_length=30,verbose_name='Work Email',blank=True)

    class Meta:
        db_table = tablePrefix + "customer"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('lawaccount:genericListView',kwargs={'model_name': 'customer'})

class File(models.Model):
    FILE_TYPE=(
        ('Type A','Type A'),
        ('Type B','Type B'),
    )
    customer = models.ForeignKey(Customer, verbose_name='Customer')
    file_no = models.CharField(max_length=20, verbose_name='File #')
    file_type = models.CharField(max_length=20, verbose_name='File Type',choices=FILE_TYPE)
    secretary = models.CharField(max_length=40,verbose_name='Secretary')
    start_date = models.DateField(verbose_name='Start Date')

    class Meta:
        db_table = tablePrefix + "customerfile"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.file_no

    def get_absolute_url(self):
        return reverse('lawaccount:genericListView',kwargs={'model_name': 'file'})







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

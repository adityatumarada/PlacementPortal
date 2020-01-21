from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    btech = '01'
    mtech = '41'
    phd = '61'
    msc = '21'
    msr = '43'
    ma = '22'
    bdes = '02'
    mdes = '42'
    error = '00'

    program_values = (
        (btech, 'BTech'),
        (mtech, 'MTech'),
        (phd, 'PhD'),
        (msc, 'MSc'),
        (msr, 'MS-R'),
        (ma, 'MA'),
        (bdes, 'BDes'),
        (mdes, 'MDes'),
        (error, 'Error')
    )

    cse = '01'
    ece = '02'
    me = '03'
    ce = '04'
    dd = '05'
    bsbe = '06'
    cl = '07'
    cst = '22'
    eee = '08'
    ma = '23'
    ph = '21'
    rt = '54'
    hss = '41'
    enc = '51'
    env = '52'
    nt = '53'
    lst = '55'

    department_values = (
        (cse, 'Computer Science & Engineering'),
        (ece, 'Electronics & Communication Engineering'),
        (me, 'Mechanical Engineering'),
        (ce, 'Civil Engineering'),
        (dd, 'Design'),
        (bsbe, 'Biosciences & Bioengineering'),
        (cl, 'Chemical Engineering'),
        (cst, 'Chemical Science & Technology'),
        (eee, 'Electronics & Electrical Engineering'),
        (ma, 'Mathematics & Computing'),
        (ph, 'Engineering Physics'),
        (rt, 'Rural Technology'),
        (hss, 'Humanities & Social Sciences'),
        (enc, 'Centre for Energy'),
        (env, 'Centre for Environment'),
        (nt, 'Centre for Nanotechnology'),
        (lst, 'Centre for Linguistic Science & Technology'),
        (error, 'Error')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    program = models.CharField(max_length=2, choices=program_values)
    department = models.CharField(max_length=3, choices=department_values)
    bio = models.TextField(max_length=1000)
    contact = models.IntegerField(max_length=10)

    def __str__(self):
        return self.user.name


class Experience(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='user_name')
    company = models.CharField(max_length=30)
    profile = models.CharField(max_length=30)
    cpi = models.DecimalField(decimal_places=5, max_digits=7)
    experience_tech = models.TextField(max_length=1000)
    experience_hr = models.TextField(max_length=1000)
    experience_tips = models.TextField(max_length=1000)

    def __str__(self):
        return self.user.name + '-' + self.company

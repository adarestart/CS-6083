from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm
from app01.utils.encrypt import md5



'''class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", 'account', 'create_time', "gender", "depart"]


class PrettyModelForm(BootStrapModelForm):
    # 验证：方式1
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.PrettyNum
        # fields = "__all__"
        # exclude = ['level']
        fields = ["mobile", 'price', 'level', 'status']

    # 验证：方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="手机号")
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    # 验证：方式2
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        # print(self.instance.pk)
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile
'''


class AdminIndividualFormViewAll(BootStrapModelForm):
    street = forms.CharField(disabled=True, label="Street")
    city = forms.CharField(disabled=True, label="City")
    zipcode = forms.CharField(disabled=True, label="Zipcode")
    email = forms.CharField(disabled=True, label="Email")
    phone = forms.CharField(disabled=True, label="Phone")
    FirstName = forms.CharField(disabled=True, label="First Name")
    MiddleName = forms.CharField(disabled=True, label="Middle Name")
    LastName = forms.CharField(disabled=True, label="Last Name")
    InsuranceCompany = forms.CharField(disabled=True, label="Insurance Company")
    InsuranceNumber = forms.CharField(disabled=True, label="Insurance Number")
    rate = forms.CharField(disabled=True, label="Coupon Rate")
    StartDate = forms.CharField(disabled=True, label="Start Date")
    EndDate = forms.CharField(disabled=True, label="End Date")

    class Meta:
        model = models.IndividualInfo
        fields = ["FirstName", "MiddleName", "LastName", "street", "city", "zipcode", "email", "phone",
                  "InsuranceCompany", "InsuranceNumber", "rate", "StartDate", "EndDate"]


class AdminIndividualEdit(BootStrapModelForm):
    rate = forms.DecimalField(min_value=0, max_value=1, label="rate")
    StartDate = forms.CharField(disabled=True, label="Start Date")

    class Meta:
        model = models.IndividualInfo
        fields = ["FirstName", "MiddleName", "LastName", "street", "city", "zipcode", "email", "phone",
                  "InsuranceCompany", "InsuranceNumber", "rate", "StartDate", "EndDate"]

    def clean_phone(self):
        mobile = self.cleaned_data["phone"]
        if len(mobile) < 9:
            raise ValidationError("Wrong Format")

        exists = models.IndividualInfo.objects.exclude(id=self.instance.pk).filter(phone=mobile).exists()
        if exists:
            raise ValidationError("Phone Number Exists")
        return mobile

    def clean_email(self):
        mail = self.cleaned_data["email"]
        exists = models.IndividualInfo.objects.exclude(id=self.instance.pk).filter(email=mail).exists()
        if exists:
            raise ValidationError("Email Address Exists")
        return mail


class AdminIndividualAdd(BootStrapModelForm):
    rate = forms.DecimalField(min_value=0, max_value=1, label="rate")

    class Meta:
        model = models.IndividualInfo
        fields = ["FirstName", "MiddleName", "LastName", "street", "city", "zipcode", "email", "phone",
                  "InsuranceCompany", "InsuranceNumber", "rate", "StartDate", "EndDate"]

    def clean_phone(self):
        mobile = self.cleaned_data["phone"]
        if len(mobile) < 9:
            raise ValidationError("Wrong Format")
        exists = models.IndividualInfo.objects.filter(phone=mobile).exists()
        if exists:
            raise ValidationError("Phone Number Already Exists")
        return mobile

    def clean_email(self):
        mail = self.cleaned_data["email"]
        exists = models.IndividualInfo.objects.filter(email=mail).exists()
        if exists:
            raise ValidationError("Email Address Already Exists")
        return mail


class AdminCorporateAdd(BootStrapModelForm):
    rate = forms.DecimalField(min_value=0, max_value=1, label="rate")

    class Meta:
        model = models.CorporationUser
        fields = [
            "street", "city", "zipcode", "email", "phone", "employ_id", "corporation_name", "rate"]

    def clean_email(self):
        mail = self.cleaned_data["email"]
        exists = models.CorporationUser.objects.filter(email=mail).exists()
        if exists:
            raise ValidationError("Email Address Already Exists")
        return mail

    def clean_id(self):
        eid = self.cleaned_data["employ_id"]
        exists = models.CorporationUser.objects.filter(employ_id=id).exists()
        if exists:
            raise ValidationError("Employ id Address Already Exists")
        return eid

    def clean_phone(self):
        mobile = self.cleaned_data["phone"]
        if len(mobile) < 9:
            raise ValidationError("Wrong Format")
        exists = models.CorporationUser.objects.filter(phone=mobile).exists()
        if exists:
            raise ValidationError("Phone Number Already Exists")
        return mobile


class AdminCorporateViewAll(BootStrapModelForm):
    street = forms.CharField(disabled=True, label="Street")
    city = forms.CharField(disabled=True, label="City")
    zipcode = forms.CharField(disabled=True, label="Zipcode")
    email = forms.CharField(disabled=True, label="Email")
    phone = forms.CharField(disabled=True, label="Phone")
    rate = forms.CharField(disabled=True, label="Coupon Rate")
    corporation_name = forms.CharField(disabled=True, label="Corporation ID")
    employ_id = forms.CharField(disabled=True, label="Employ ID")

    class Meta:
        model = models.CorporationUser
        fields = [
            "street", "city", "zipcode", "email", "phone", "employ_id", "corporation_name", "rate"]


class AdminCorporateEdit(BootStrapModelForm):
    rate = forms.DecimalField(min_value=0, max_value=1, label="rate")
    employ_id = forms.CharField(disabled=True, label="Employ ID")
    corporation_name = forms.CharField(disabled=True, label="Corporation ID")

    class Meta:
        model = models.CorporationUser
        fields = [
            "street", "city", "zipcode", "email", "phone", "employ_id", "corporation_name", "rate"]

    def clean_email(self):
        mail = self.cleaned_data["email"]
        exists = models.CorporationUser.objects.exclude(self.instance.pk).filter(email=mail).exists()
        if exists:
            raise ValidationError("Email Address Already Exists")
        return mail

    def clean_phone(self):
        mobile = self.cleaned_data["phone"]
        if len(mobile) < 9:
            raise ValidationError("Wrong Format")
        exists = models.CorporationUser.objects.exclude(self.instance.pk).filter(phone=mobile).exists()
        if exists:
            raise ValidationError("Phone Number Already Exists")
        return mobile


class AdminAdd(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="Confirm the password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_username(self):
        uid = self.cleaned_data["username"]
        exists = models.Admin.objects.filter(username=uid).exists()
        if exists:
            raise ValidationError("Username Already Exists")
        return uid

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("Password Does Not Match")
        return confirm


class AdminLogin(BootStrapForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput,
        required=True
    )

    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    code = forms.CharField(
        label="CAPTCHA",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


class OfficeAdd(BootStrapModelForm):
    class Meta:
        model = models.Office
        fields = ["name", "street", "city", "zipcode", "phone"]

    def clean_name(self):
        uname = self.cleaned_data["name"]
        exists = models.Office.objects.filter(name=uname).exists()
        if exists:
            raise ValidationError("Office Name Already Exists")
        return uname

    def clean_phone(self):
        number = self.cleaned_data["phone"]
        exists = models.Office.objects.filter(phone=number).exists()
        if exists:
            raise ValidationError("Phone Number Already Exists")
        return number


class OfficeEdit(BootStrapModelForm):
    class Meta:
        model = models.Office
        fields = ["name", "street", "city", "zipcode", "phone"]

    def clean_name(self):
        uname = self.cleaned_data["name"]
        exists = models.Office.objects.exclude(id=self.instance.pk).filter(name=uname).exists()
        if exists:
            raise ValidationError("Office Name Already Exists")
        return uname

    def clean_phone(self):
        number = self.cleaned_data["phone"]
        exists = models.Office.objects.exclude(id=self.instance.pk).filter(phone=number).exists()
        if exists:
            raise ValidationError("Phone Number Already Exists")
        return number


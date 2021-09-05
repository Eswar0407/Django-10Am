from django import forms

class EmployeeRegistrationForm(forms.Form):

    desg = (('Manager','MANAGER'),
           ('Developer', 'DEVELOPER'),
            ('Qa', 'QA')

    )

    idno = forms.IntegerField(label="EMPLOYEE NUMBER")
    name = forms.CharField(label="Employee Name")
    salary = forms.FloatField(label="Employee Salary")

    designation1 = forms.ChoiceField(label="Employee Designation",choices=desg)  #dropdown List
    designation2 = forms.ChoiceField(label="Employee Designation",choices=desg,widget=forms.RadioSelect)  #select one

    c = forms.CharField(label="C Language Developer",widget=forms.CheckboxInput) #select multiple in chechboxes
    Python = forms.CharField(label="Python Developer",widget=forms.CheckboxInput)
    Java = forms.CharField(label="Java Developer",widget=forms.CheckboxInput)

    photo = forms.ImageField(label="Employee Photo")

    dob = forms.DateField(label="Employee Date Of Birth",widget=forms.DateInput)
    email = forms.EmailField(label="Employee Email ID")
    password = forms.CharField(label="Employee Password",widget=forms.PasswordInput)
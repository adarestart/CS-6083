from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AdminIndividualFormViewAll, AdminIndividualEdit, AdminIndividualAdd, AdminCorporateAdd, \
    AdminCorporateViewAll, AdminCorporateEdit, AdminAdd, AdminLogin, OfficeAdd, OfficeEdit

from app01.utils.code import check_code
from io import BytesIO


# Create your views here.


def admin_individual(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.IndividualInfo.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_individual.html', context)


def admin_individual_view_all(request, nid):
    row_object = models.IndividualInfo.objects.filter(id=nid).first()
    form = AdminIndividualFormViewAll(instance=row_object)
    return render(request, 'admin_view_all.html', {'form': form})


def admin_individual_edit(request, nid):
    row_object = models.IndividualInfo.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = AdminIndividualEdit(instance=row_object)
        return render(request, 'admin_edit.html', {'form': form})
    form = AdminIndividualEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/individual_user/')
    return render(request, 'admin_edit.html', {'form': form})


def admin_add_individual(request):
    if request.method == 'GET':
        form = AdminIndividualAdd()
        return render(request, 'admin_add_individual.html', {'form': form})
    form = AdminIndividualAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/individual_user/')
    return render(request, 'admin_add_individual.html', {'form': form})


def admin_individual_delete(request, nid):
    models.IndividualInfo.objects.filter(id=nid).delete()
    return redirect('/admin/individual_user/')


def admin_corporate(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["employ_id"] = search_data

    queryset = models.CorporationUser.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_corporate.html', context)


def admin_corporate_add(request):
    if request.method == 'GET':
        form = AdminCorporateAdd()
        return render(request, 'admin_add_corporate.html', {'form': form})
    form = AdminCorporateAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/corporate_user/')
    return render(request, 'admin_add_corporate.html', {'form': form})


def admin_corporate_view_all(request, nid):
    row_object = models.CorporationUser.objects.filter(id=nid).first()
    form = AdminCorporateViewAll(instance=row_object)
    return render(request, 'admin_corporate_view_all.html', {'form': form})


def admin_corporate_edit(request, nid):
    row_object = models.CorporationUser.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = AdminCorporateEdit(instance=row_object)
        return render(request, 'admin_corporate_edit.html', {'form': form})

    form = AdminCorporateEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/corporate_user/')
    return render(request, 'admin_corporate_edit.html', {'form': form})


def admin_corporate_delete(request, nid):
    models.CorporationUser.objects.filter(id=nid).delete()
    return redirect('/admin/corporate_user/')


def admin_add(request):
    if request.method == 'GET':
        form = AdminAdd()
        return render(request, 'admin_add.html', {'form': form})

    form = AdminAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/login/')
    return render(request, 'admin_add.html', {'form': form})


def admin_login(request):
    if request.method == 'GET':
        form = AdminLogin()
        return render(request, 'admin_login.html', {'form': form})
    form = AdminLogin(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "Wrong Code")
            return render(request, 'admin_login.html', {'form': form})

        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "Wrong Username or Password")
            return render(request, 'admin_login.html', {'form': form})
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/individual_user/")
    return render(request, 'admin_login.html', {'form': form})


def image_code(request):
    img, code_string = check_code()
    request.session['image_code'] = code_string
    # request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def admin_logout(request):
    request.session.clear()
    return redirect('/admin/login/')


def office_show(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.Office.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_office.html', context)


def office_add(request):
    if request.method == 'GET':
        form = OfficeAdd()
        return render(request, 'office_add.html', {'form': form})

    form = OfficeAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/office/')
    return render(request, 'office_add.html', {'form': form})


def office_edit(request, nid):
    row_object = models.Office.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = OfficeEdit(instance=row_object)
        return render(request, 'office_edit.html', {'form': form})
    form = OfficeEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/office/')
    return render(request, 'office_edit.html', {'form': form})


def office_delete(request, nid):
    models.Office.objects.filter(id=nid).delete()
    return redirect('/admin/office/')


def individual(request):
    return render(request, 'individual.html')


import sys
from django.contrib import messages
from django.db.models.signals import post_save
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
from shaura.models import AccountUser
from shaura.signals import check_nim
from shaura.forms import StudentRegisterForm

# Create your views here.
def readStudent(request):
    data = AccountUser.objects.all()
    context = {'data_list': data}
    return render(request, 'index.html', context)

@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            post_save.disconnect(check_nim)
            form.fullname = form.cleaned_data.get("fullname")
            form.nim = form.cleaned_data.get("nim")
            form.email = form.cleaned_data.get("email")
            post_save.send(
                sender=AccountUser,
                created=None,
                instance=form,
                dispatch_uid="check_nim"
            )
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('myFirstApp:read-data-student')
    else:
        form = StudentRegisterForm()

    return render(request, 'form.html', {'form': form})

@csrf_protect
def updateStudent(request, id):
    student = get_object_or_404(AccountUser, account_user_related_user=id)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, instance=student)
        if form.is_valid():
            student.account_user_fullname = form.cleaned_data.get("fullname")
            student.account_user_student_number = form.cleaned_data.get("nim")
            student.account_user_related_user = form.cleaned_data.get("email")
            student.save()
            messages.success(request, 'Data Berhasil diperbarui')
            return redirect('myFirstApp:read-data-student')
    else:
        form = StudentRegisterForm(instance=student)

    return render(request, 'form.html', {'form': form})

@csrf_protect
def deleteStudent(request, id):
    student = get_object_or_404(AccountUser, account_user_related_user=id)
    user = get_object_or_404(User, username=id)
    if request.method == 'POST':
        student.delete()
        user.delete()
        messages.success(request, 'Data Berhasil dihapus')
        return redirect('myFirstApp:read-data-student')
    return render(request, 'confirm_delete.html', {'student': student})

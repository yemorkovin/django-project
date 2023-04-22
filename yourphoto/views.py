from turtle import title
from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from yourphoto.forms import Auth, Filter_form, PanelUpdate, Registration
from yourphoto.models import City_list, Photo_list, Photo_Profile, Users


def index(request):
    context = {}
    if 'login' in request.session:
        context['login'] = request.session['login']
    return render(request, 'index.html', context=context)


def auto_bool(request):
    if Photo_Profile.objects.filter(Q(login__exact = request.GET.get['login']) and Q(photo_profile__exact = '')):
        return True
    else:
        return False


def auto(request):
    context = {}
    if request.method == 'POST':
        form = Auth(request.POST)
        if form.is_valid():
            if auto_bool(request):
                request.session['login'] = request.POST['login']
                request.session['password'] = request.POST['password']

                
    else:
        form = Auth
    context["form"] = form
    if 'login' in request.session:
        context['login'] = request.session['login']
    return render(request, 'auto.html', context=context)


def contacts(request):
    context = {}
    if 'login' in request.session:
        context['login'] = request.session['login']
    return render(request, 'contacts.html')

def save_user(request):
    user = Users()
    user.status = request.POST['status']
    user.full_name = request.POST['full_name']
    user.tel = request.POST['phone']
    user.city = request.POST['city']
    user.email = request.POST['email']
    user.login = request.POST['login']
    user.password = request.POST['password']
    user.save()
    



def registration(request):
    context = {}
    send_mail(
        subject='Добро пожаловать в наш интернет-магазин!',
        message=f', вы успешно зарегистрировались!',
        from_email=None,
        recipient_list=['admin@yemorkovin.ru'],
    )
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            if Users.objects.filter(login=request.POST['login']).exists():
                context['message'] = "Error login"
            else:
                save_user(request)
                context['message'] = "YOU REGISTRATION"
                save_user(request)
                context['message'] = "YOU REGISTRATION"

    else:
        form = Registration
    context["form"] = form
    if 'login' in request.session:
        context['login'] = request.session['login']
    

    return render(request, 'registration.html', context=context)


def exit(request):
    if 'login' in request.session:
        del request.session['login']
        del request.session['password']
    return redirect('/')


def filter(request):
    context = {}
    if request.method == 'POST':
        form = Filter_form(request.POST)
        if form.is_valid():
            users = Users.objects.filter(Q(city__exact = request.POST['city']))
            context['users'] = users
        
    else:
        form = Filter_form
        users = Users.objects.filter(Q(status__exact = "YS"))
        context['users'] = users
    context["form"] = form
    if 'login' in request.session:
        context['login'] = request.session['login']
    # context['users'] = users


    return render(request, "filter.html", context=context)


def user(request):
    context = {}
    images = Photo_list.objects.filter(Q(login__exact = request.GET.get('login')))
    user = Users.objects.filter(Q(login__exact = request.GET.get('login')))

    context['photo_profile'] = Photo_Profile.objects.filter(Q(login__exact = request.GET.get('login')))

    context['user'] = user
    context['images'] = images

    return render(request, "user.html", context=context)

def update_data(request):
    user_id = Users.objects.filter(Q(login__exact = request.POST['login']))[0]
    user = Users(id=user_id.id)
    user.status = request.POST['status']
    user.full_name = request.POST['full_name']
    user.tel = request.POST['phone']
    user.city = request.POST['city']
    user.email = request.POST['email']
    user.login = request.POST['login']
    user.password = request.POST['password']
    user.save()

def panel(request):
    #user = super().save(request)

    if 'login' in request.session:
        context = {}
        if 'login' in request.session:
            context['login'] = request.session['login']

        if request.method == 'POST' and request.FILES:
            if Photo_Profile.objects.filter(login = request.session['login']).exists():
                user_id = Users.objects.filter(Q(login__exact = request.session['login'])).values("id")[0]["id"]

                file = request.FILES['file']
                f = FileSystemStorage()
                f_name = f.save(file.name, file)
                url_file = f.url(f_name)

                photo_list = Photo_Profile(id = user_id)
            
                photo_list.login = request.session['login']
                photo_list.photo_profile = url_file
                photo_list.save()
            else:
                file = request.FILES['file']
                f = FileSystemStorage()
                f_name = f.save(file.name, file)
                url_file = f.url(f_name)
                photo_list = Photo_Profile()
            
                photo_list.login = request.session['login']
                photo_list.photo_profile = url_file
                photo_list.save()
            form = PanelUpdate(request.POST)
            if form.is_valid():
                update_data(request)

        else:
            user_cur = Users.objects.filter(Q(login__exact=request.session['login']))
            form = PanelUpdate
            context['users'] = user_cur
        context["form"] = form
        context["images"] = Photo_Profile.objects.filter(Q(login__exact=request.session['login']))[1:]
        # context['users'] = users

        return render(request, "panel.html", context=context)
    else:
        return redirect("/")

def add_photo(request):
    context = {}
    if request.method == "POST" and request.FILES:
        file = request.FILES['file']
        f = FileSystemStorage()
        f_name = f.save(file.name, file)
        url_file = f.url(f_name)
        photo_list = Photo_list()
        photo_list.full_name = request.POST['title']
        photo_list.photo = url_file
        photo_list.login = request.session['login']
        photo_list.save()
    if 'login' in request.session:
        context['login'] = request.session['login']
        

    image_list = Photo_list.objects.filter(Q(login__exact=request.session['login']))
    context['photos'] = image_list
    return render(request, "addPhoto.html", context=context)

def delete(request):
    id = request.GET.get('id')
    delete_photo = Photo_list.objects.get(id = id)
    delete_photo.delete()
    return redirect('add_photo')

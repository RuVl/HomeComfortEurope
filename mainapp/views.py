import validators
from django.contrib.auth import login

from django.shortcuts import render, get_object_or_404
from .models import UserProfileModel, CompanyModel, CollectionModel, ProductType, ProductItem


main_context = {}


def get_collections_menu():
    collections_menu = CollectionModel.objects.all()
    return collections_menu


def get_types_sorted_by_collections(pk):
    product_types_menu = ProductType.objects.filter(collection=pk)
    return product_types_menu


def get_products_sorted_by_types(pk):
    products_sorted_by_types = ProductItem.objects.filter(type=pk)
    return products_sorted_by_types


def get_product(request, pk):
    product = ProductItem.objects.get(pk=pk)
    context = {
        'title': 'Heritage Furniture - Design For Living',
        'links_menu': get_collections_menu(),
        'product': product,
        'type': product.objects.get(type=product.type)
    }
    return render(request, 'product.html', context=context)

def index(request):
    context = {
        'title': 'Heritage Furniture - Design For Living',
        'links_menu': get_collections_menu(),
        # 'subcategory_meny': get_types_sorted_by_collections()
    } | main_context

    return render(request, 'index.html', context=context)


def valid(data: dict):
    if not validators.email(data.get('email')) or \
            not validators.truthy(data.get('firstName')) or \
            not validators.truthy(data.get('lastName')) or \
            not validators.truthy(data.get('phone')) or \
            not validators.truthy(data.get('password')) or \
            data.get('password') != data.get('confirmPassword'):
        return False
    return True


def register(request):
    if request.method == 'GET':
        context = {
                      'title': 'Register'
                  } | main_context

        return render(request, 'register.html', context=context)
    elif request.method == 'POST':
        if not valid(request.POST):
            print("Not Valid")
            context = {
                          'title': 'Register',
                          'not_valid': 'true'
                      } | main_context

            return render(request, 'register.html', context=context)

        first_name = request.POST['firstName']
        last_name = request.POST['lastName']

        username = request.POST['email']
        phone = request.POST['phone']

        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        company_name_ = request.POST['CompanyName']
        sel_company_type = request.POST['SelCompanyType']
        sel_acc_title = request.POST['selAccTitle']
        user = UserProfileModel(
            username=username,
            email=username,
            phone_number=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        if company_name_ is not None:
            company = CompanyModel(
                company_name=company_name_,
                company_type=sel_company_type,
                owner=user,
                title=sel_acc_title

            )
            company.save()
        login(request, user)
        return index(request)
        # TODO Создать пользователя
        # Отправка сообщения на почту НЕ нужна!


def login_(request):
    if request.method == 'GET':
        context = {
                      'title': 'Existing Trade Customers Login'
                  } | main_context

        return render(request, 'register.html', context=context)
    elif request.method == 'POST':
        email = request.POST['emailId']
        password = request.POST['usrpassword']
        user = UserProfileModel.objects.get(email=email, password=password)
        login(request, user)
        main_context['is_authenticated'] = request.user.is_authenticated
        return index(request)
        # TODO Залогинить пользователя


def become_a_stocklist(request):
    if request.method == 'GET':
        # TODO сюда вставить данные пользователя, если он сейчас залогинился, иначе - отправить его на страницу регистрации
        # Если каких-то данных нет - оставь ''
        context = {
                      'title': 'Design For Living',
                      'firstName': '',
                      'lastName': '',
                      'email': '',
                      'phone': '',
                      'postCode': ''
                  } | main_context

        return render(request, '../../../HomeComfortEurope/mainapp/templates/become_a_stocklist.html', context=context)
    elif request.method == 'POST':
        return index(request)


# Complete
def search_result(request):
    context = {
        'title': 'Search result',
        'links_menu': get_collections_menu()
    } | main_context
    return render(request, 'search_result.html', context=context)


def news(request):
    context = {
        'title': 'News',
        'links_menu': get_collections_menu()
    } | main_context

    return render(request, 'news.html', context=context)


# Complete
def concrete_news(request, concrete: str):
    context = {
                  'title': concrete.replace('_', ' '),
                  'links_menu': get_collections_menu()
              } | main_context

    return render(request, f'news/{concrete}.html', context=context)


# Complete
def about_us(request):
    context = {
        'title': 'Our Story',
        'links_menu': get_collections_menu()
    } | main_context

    return render(request, 'our_story.html', context=context)


# Complete
def ethos(request):
    context = {
                  'title': 'Our Story',
                  'links_menu': get_collections_menu()
              } | main_context

    return render(request, 'ethos.html', context=context)


# Complete
def design_studio(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_collections_menu()
              } | main_context

    return render(request, 'design_studio.html', context=context)


# Complete
def fulfilment(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_collections_menu()
              } | main_context

    return render(request, 'fulfilment.html', context=context)


# Complete
def privacy_policy(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_collections_menu()
              } | main_context

    return render(request, 'privacy_policy.html', context=context)


# Complete
def cookies(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_collections_menu()
              } | main_context

    return render(request, 'cookies.html', context=context)


# def get_links_menu():
#         links_menu = CollectionModel.objects.filter(is_deleted=False)
#         return links_menu


# def get_category(pk):
#         collection = get_object_or_404(CollectionModel, pk=pk)
#         return collection



import logging

import validators
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import UserProfileModel, CompanyModel, CollectionModel, ProductType, ProductItem


main_context = {}


def get_header():
    collections = CollectionModel.objects.all()
    types = ProductType.objects.all()
    header = {'collections': collections, 'types': types}
    return header


def get_types_sorted_by_collections(request, pk):
    # product_types_menu = ProductType.objects.filter(collection=pk)
    context = {
        'title': 'Heritage Furniture - Design For Living',
        'links_menu': get_header(),
        'types': ProductType.objects.filter(collection=pk),
        'collection': CollectionModel.objects.get(pk=pk)
    }

    return render(request, 'category.html', context=context)


def get_products_sorted_by_type(request, pk):
    products_sorted_by_types = ProductItem.objects.filter(type=pk)
    context = {
        'title': 'Heritage Furniture - Design For Living',
        'links_menu': get_header(),
        'products': products_sorted_by_types,
        'type': ProductType.objects.get(pk=pk),
        'collection': ProductType.objects.get(pk=pk).collection
    }
    return render(request, 'subcategory.html', context=context)


def get_product(request, pk):
    product = ProductItem.objects.get(pk=pk)
    context = {
        'title': 'Heritage Furniture - Design For Living',
        'links_menu': get_header(),
        'product': product,
        'type': ProductType.objects.get(pk=product.type.pk)
    }
    return render(request, 'product.html', context=context)


def index(request):
    context = {
        # 'user_status': request.user.is_authenticated,
        'title': 'Heritage Furniture - Design For Living',
        'links_menu': get_header(),
        # 'subcategory_meny': get_types_sorted_by_collections()
    } | main_context

    return render(request, 'index.html', context=context)


def valid_user_register(data: dict):
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
                      'title': 'Register',
                      # 'user_status': request.user.is_authenticated,
                      'links_menu': get_header(),
                  } | main_context

        return render(request, 'register.html', context=context)
    elif request.method == 'POST':
        if not valid_user_register(request.POST):
            logging.warning('Not valid data!')
            context = {
                'title': 'Register',
                'links_menu': get_header(),
                'valid_msg': 'Not valid data!'
            } | main_context

            return render(request, 'register.html', context=context)

        first_name = request.POST['firstName']
        last_name = request.POST['lastName']

        username = request.POST['email']
        phone = request.POST['phone']

        password = request.POST['password']

        company_name_ = request.POST.get('CompanyName')
        sel_company_type = request.POST.get('SelCompanyType') or '---'
        sel_acc_title = request.POST.get('selAccTitle') or '---'

        try:
            user = UserProfileModel(
                username=username,
                email=username,
                phone_number=phone,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()

            if validators.truthy(company_name_):
                company = CompanyModel(
                    company_name=company_name_,
                    company_type=sel_company_type,
                    owner=user,
                    title=sel_acc_title
                )
                company.save()
            login(request, user)
            return index(request)
        except:
            logging.warning('Already registered!')
            context = {
                'title': 'Register',
                'links_menu': get_header(),
                'valid_msg': 'Already registered!'
            } | main_context

            return render(request, 'register.html', context=context)


def valid_user(data: dict):
    if not validators.email(data.get('emailId')) or not validators.truthy(data.get('usrpassword')):
        return False
    return True


def login_(request):
    if request.method == 'GET':
        context = {
                      'title': 'Existing Trade Customers Login',
                      'links_menu': get_header(),
                  } | main_context

        return render(request, 'register.html', context=context)
    elif request.method == 'POST':
        if not valid_user(request.POST):
            logging.warning('Not valid data!')
            context = {
                          'title': 'Register',
                          'links_menu': get_header(),
                          'valid_msg': 'Not valid data!'
                      } | main_context

            return render(request, 'register.html', context=context)

        email = request.POST['emailId']
        password = request.POST['usrpassword']

        user = UserProfileModel.objects.get(email=email, password=password)

        try:
            login(request, user)
        except UserProfileModel.DoesNotExist:
            logging.warning('User does not exist.')
            context = {
                          'title': 'Register',
                          'links_menu': get_header(),
                          'valid_msg': 'Firstly register'
                      } | main_context

            return render(request, 'register.html', context=context)

        main_context['user'] = request.user

        return index(request)


        user = UserProfileModel.objects.get(username=email, password=password)
        if user is not None:
            login(request, user)
            main_context['is_authenticated'] = request.user.is_authenticated
        return index(request)


# Complete
def search_result(request):
    context = {
        'title': 'Search result',
        'links_menu': get_header()
    } | main_context
    return render(request, 'search_result.html', context=context)


# Complete
def news(request):
    context = {
        # 'user_status': request.user.is_authenticated,
        'title': 'News',
        'links_menu': get_header()
    } | main_context

    return render(request, 'news.html', context=context)


# Complete
def concrete_news(request, concrete: str):
    context = {
                  # 'user_status': request.user.is_authenticated,
                  'title': concrete.replace('_', ' '),
                  'links_menu': get_header()
              } | main_context

    return render(request, f'news/{concrete}.html', context=context)


# Complete
def about_us(request):
    context = {
        # 'user_status': request.user.is_authenticated,
        'title': 'Our Story',
        'links_menu': get_header()
    } | main_context

    return render(request, 'our_story.html', context=context)


# Complete
def ethos(request):
    context = {
                  'title': 'Our Story',
                  'links_menu': get_header()
              } | main_context

    return render(request, 'ethos.html', context=context)


# Complete
def design_studio(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_header()
              } | main_context

    return render(request, 'design_studio.html', context=context)


# Complete
def fulfilment(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_header()
              } | main_context

    return render(request, 'fulfilment.html', context=context)


# Complete
def privacy_policy(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_header()
              } | main_context

    return render(request, 'privacy_policy.html', context=context)


# Complete
def cookies(request):
    context = {
                  'title': 'Design For Living',
                  'links_menu': get_header()
              } | main_context

    return render(request, 'cookies.html', context=context)


def user_profile(request):
    context = {}
    if request.user.is_authenticated:
        user = UserProfileModel.objects.get(pk=request.user.pk)
        context['user_data'] = user
        if user.interested_in_stocking or user.is_dealer:
            context['company_data'] = CompanyModel.objects.get(owner=user)
        return render(request, 'profile.html', context=context)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

# def get_links_menu():
#         links_menu = CollectionModel.objects.filter(is_deleted=False)
#         return links_menu


# def get_category(pk):
#         collection = get_object_or_404(CollectionModel, pk=pk)
#         return collection

import validators

from django.shortcuts import render


main_context = {}


def index(request):
    context = {
        'title': 'Heritage Furniture - Design For Living'
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

        sel_title = request.POST['SelTitle']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']

        email = request.POST['email']
        phone = request.POST['phone']

        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        company_name = request.POST['CompanyName']
        sel_company_type = request.POST['SelCompanyType']
        sel_acc_title = request.POST['selAccTitle']

        # TODO Создать пользователя
        # Отправка сообщения на почту НЕ нужна!


def login(request):
    if request.method == 'GET':
        context = {
            'title': 'Existing Trade Customers Login'
        } | main_context

        return render(request, 'register.html', context=context)
    elif request.method == 'POST':
        email = request.POST['emailId']
        password = request.POST['usrpassword']

        # TODO Залогинить пользователя


def forgot_password():
    pass


# Complete
def search_result(request):
    context = {
        'title': 'Search result'
    } | main_context
    return render(request, 'search_result.html', context=context)


def become_a_stocklist():
    pass


def news(request):
    context = {
        'title': 'News'
    } | main_context

    return render(request, 'news.html', context=context)


def concrete_news(request, news: str):
    context = {
        'title': news.replace('_', ' ')
    } | main_context

    return render(request, f'news/{news}.html', context=context)


# Complete
def about_us(request):
    context = {
        'title': 'Our Story'
    } | main_context

    return render(request, 'our_story.html', context=context)


def ethos():
    pass


def design_studio():
    pass


def fulfilment():
    pass


def privacy_policy():
    pass


def cookies():
    pass


def contact_us():
    pass

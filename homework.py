# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.

def function_name_param(func, *args):
    funname = func.__name__.replace('_', ' ').capitalize()
    print(funname, *args)

def open_browser(browser_name):
    function_name_param(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    function_name_param(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    function_name_param(find_registration_button_on_login_page, page_url, button_text)

open_browser(browser_name = "Chrome")
go_to_companyname_homepage(page_url='https://google.com')
find_registration_button_on_login_page(page_url = 'https://google.com', button_text='Поиск в Google')

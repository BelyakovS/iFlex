from conftest import login, passw

org_name = 'Беляков'

class TestMainPage1():

    # Авторизация
    def test_auth(self, browser):

        browser.find_by_id('basic_tenant').click()
        browser.find_by_text('Россия').click()

        browser.find_by_id('basic_username').fill(login)
        browser.find_by_id('basic_password').fill(passw)

        browser.find_by_text('Войти').click()

        # assert browser.is_text_present('Ошибка авторизации')

    # Поиск аккаунтов по названию
    def test_search_acc(self, browser):
        browser.find_by_text('Поиск').click()

        browser.find_element_by_xpath("//input[@type='text'][@id='organization.fullName']").fill(org_name)

        browser.find_by_text('Применить').click()

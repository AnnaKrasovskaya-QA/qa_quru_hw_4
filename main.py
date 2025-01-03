from selene import browser

def test_filling_out_the_form(open_browser):
    browser.element('#firstName').type('Anna')
    browser.element('#lastName').type('Ivanova')
    browser.element('#userEmail').type('AnnaIvanova@mail.ru')
    browser.quit()
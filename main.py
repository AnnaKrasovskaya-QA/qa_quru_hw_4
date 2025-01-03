from selene import browser
from selenium import webdriver


driver_options = webdriver.ChromeOptions()
driver_options.page_load_strategy = 'eager'
browser.config.driver_options = driver_options

def test_filling_out_the_form(open_browser):
    browser.element('#firstName').type('Anna')
    browser.element('#lastName').type('Ivanova')
    browser.element('#userEmail').type('AnnaIvanova@mail.ru')
    browser.element('[for = gender-radio-2]').click()
    browser.element('#userNumber').type('8978675432')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="10"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2001"]').click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture')



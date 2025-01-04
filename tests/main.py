import os.path

from selene import browser, by, have

first_name = 'Anna'
last_name = 'Ivanova'
user_email = 'AnnaIvanova@mail.ru'
gender = 'Female'
user_number = '8978675432'
birth_year = '2001'
birth_month = 'November'
birth_day = '19'
subjects_type = 'Maths'
hobbies = 'Sports'
upload_picture = '123.png'
current_address = 'Russia Moscow Lenina street house 5'
state = 'Rajasthan'
city = 'Jaipur'


def test_filling_out_the_form(open_browser):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(user_email)
    browser.element('[for = gender-radio-2]').click()
    browser.element('#userNumber').type(user_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="10"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2001"]').click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').type(subjects_type).press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(upload_picture))
    browser.element('#currentAddress').type(current_address)
    browser.element('#state').click().element(by.text(state)).click()
    browser.element('#city').click().element(by.text(city)).click()
    browser.element('#submit').click()

    browser.element('.modal-content').should(have.text('Student Name')).should(have.text(f'{first_name} {last_name}'))
    browser.element('.modal-content').should(have.text('Student Email')).should(have.text(user_email))
    browser.element('.modal-content').should(have.text('Gender')).should(have.text(gender))
    browser.element('.modal-content').should(have.text('Mobile')).should(have.text(user_number))
    browser.element('.modal-content').should(have.text('Date of Birth')).should(
        have.text(f'{birth_day} {birth_month},{birth_year}'))
    browser.element('.modal-content').should(have.text('Subjects')).should(have.text(subjects_type))
    browser.element('.modal-content').should(have.text('Hobbies')).should(have.text(hobbies))
    browser.element('.modal-content').should(have.text('Picture')).should(have.text(upload_picture))
    browser.element('.modal-content').should(have.text('Address')).should(have.text(current_address))
    browser.element('.modal-content').should(have.text('State and City')).should(have.text(f'{state} {city}'))

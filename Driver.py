from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get('https://generalssb-prod.ec.royalholloway.ac.uk/BannerExtensibility/customPage/page/RHUL_Attendance_Student')

f = open('credentials.txt')
username = f.readline()
password = f.readline()
f.close()


try:
    username_box = driver.find_element_by_id('userNameInput')
    username_box.send_keys(username)

    password_box = driver.find_element_by_id('passwordInput')
    password_box.send_keys(password)

    login_button = driver.find_element_by_id('submitButton')
    login_button.click()
    try:
        register_attendance_online_button = driver.find_element_by_id('pbid-buttonFoundHappeningNowButtonsTwoOnline')
        register_attendance_online_button.click()

    except ElementNotInteractableException as exception:
        print("You are already signed in!")

except NoSuchElementException as exception:
    print("Credentials given in credentials.txt are incorrect.")



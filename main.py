from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep

un = "admin"
password = "password"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://10.1.1.1/auth.html")


# will wait up to 30 seconds to find an element before failing
driver.implicitly_wait(5)

main_window = driver.current_window_handle

# SonicWall Login
driver.switch_to.frame('authFrm')
driver.find_element_by_name("userName").send_keys(un)
driver.find_element_by_name("pwd").send_keys(password)
driver.find_element_by_name("Submit").click()


def run_command(cmd):
    sleep(2)
    cmd


run_command(driver.switch_to.frame(driver.find_element_by_name('logoFrame')))
run_command(driver.find_element_by_id('nav_manage').click())
run_command(driver.switch_to.parent_frame())
run_command(driver.switch_to.frame(
    driver.find_element_by_name('outlookFrame')))
run_command(driver.find_element_by_id('j1_104_anchor').click())
run_command(driver.find_element_by_id('j1_111_anchor').click())
run_command(driver.switch_to.parent_frame())
run_command(driver.switch_to.frame(driver.find_element_by_name('tabFrame')))
run_command(driver.find_element_by_name("cfgButt").click())
run_command(driver.switch_to.window(driver.window_handles[1]))
run_command(driver.find_element_by_name('ok').click())
run_command(driver.switch_to.window(main_window))
run_command(driver.close())

driver.find_element_by_xpath()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#
# # import Action chains
# from selenium.webdriver.common.action_chains import ActionChains
#
# # import KEYS

# from selenium.webdriver.common.keys import Keys
#
# # create webdriver object
#
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# action = ActionChains(driver)
#
# action.move_to_element(driver.find_elements(By.XPATH,'//i[@class="gfg-icon gfg-icon_arrow-down gfg-icon_header"]')[1]).perform()
# action.move_to_element(driver.find_element(By.XPATH,'(//i[@class="gfg-icon gfg-icon_arrow-right"])[12]')).perform()
# action.move_to_element(driver.find_element(By.XPATH,"(//a[contains(text(),'Python')])[4]")).perform()
# driver.find_element(By.XPATH,"(//a[contains(text(),'Python')])[4]").click()

class Jira_Automation:

    def __init__(self):
        global driver
        self.url="https://jira.devtools.intel.com/browse/"
        self.expected_story_points = 2  # find from excel and convert to int
        self.jira_id = "ADAD-22774"  # find from excel and convert to string
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.implicitly_wait(10)

    def open_url(self):
        driver.get("{}{}".format(self.url,self.jira_id))
        driver.maximize_window()
        time.sleep(10)
        self.check_story_points()

    def update_story_points(self):
        # updating the jira values
        driver.find_element(By.XPATH,'//span [@class="icon aui-icon aui-icon-small aui-iconfont-edit"]').click()
        driver.find_element(By.ID,"customfield_11204").clear()
        driver.find_element(By.ID, "customfield_11204").send_keys(self.expected_story_points)
        driver.find_element(By.ID,"edit-issue-submit").click()
        driver.quit()

    def check_story_points(self):
        self.story_points = int(
            driver.find_element(By.XPATH, '//div[@class="value type-float editable-field inactive"]').text)
        if self.story_points != self.expected_story_points:
            print("story points are not updated, so updating now")
            self.update_story_points()
        else:
            print("story already points set to {}".format(self.expected_story_points))
            driver.quit()

obj=Jira_Automation()
obj.open_url()

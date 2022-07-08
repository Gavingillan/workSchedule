from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import userInfo

def getShift(day:int,month:int,year:int):
    with webdriver.Edge() as driver:
        driver.get("https://amc.cloud.infor.com/etm/login.jsp?config=false&locale=EN")
        driver.find_element(By.ID, "loginField").send_keys(userInfo.user_name)
        driver.find_element(By.ID, "passwordField").send_keys(userInfo.password)
        driver.find_element(By.ID, "loginButton").click()
        driver.get(f"https://amc.cloud.infor.com/etm/time/timesheet/etmTnsDay.jsp?date={month}.{day}.{year}")

        try:
            time = driver.find_element(By.XPATH, "//*[@id='scheduleViewTable']/tbody/tr[2]/td[3]/div/div/div[1]").text
            shift = driver.find_element(By.XPATH, "//*[@id='scheduleViewTable']/tbody/tr[2]/td[3]/div/div/div[2]").text
            return time, shift
        except NoSuchElementException:
            return "", "OFF"

if __name__ == "__main__":
    print(getShift(8, 7, 2022))
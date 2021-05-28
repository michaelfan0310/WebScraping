from selenium import webdriver

chrome_drive_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)



driver.get(
    "https://www.worldometers.info/coronavirus/")

global_data = driver.find_element_by_class_name("maincounter-number")
print(f"\nGlobal_data: {global_data.text}\n")

total_death = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td[5]')
print(f"total_death: {total_death.text}\n")

USA_data = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[3]')
print(f"USA_data:  {USA_data.text}\n")

Canada_today=driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[28]/td[4]')
print(f"CANADA_today: {Canada_today.text}\n")

Canda_total=driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[28]/td[3]')
print(f"Canada_total: {Canda_total.text}\n")

Indian_today = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td[4]')
print(f"INDIAN_today: {Indian_today.text}\n")
Indian_total=driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td[3]')
print(f"Indian_total: {Indian_total.text}\n")

file=open("covid_data.txt", "w+")
file.write(f"Global_data: {global_data.text}\n"
           f"USA_data:  {USA_data.text}\n"
           f"CANADA_today: {Canada_today.text}\n"
           f"Canada_total: {Canda_total.text}\n"
           f"INDIAN_today: {Indian_today.text}\n"
           f"Indian_total: {Indian_total.text}\n")

file.close()


driver.close()

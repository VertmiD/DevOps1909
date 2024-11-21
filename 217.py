from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
#def my_test(values_to_check, expected):
d.get("file:///G:/My%20Drive/%D7%9C%D7%99%D7%9E%D7%95%D7%93%D7%99%D7%9D/DEVOPS%20Experts/Lesson%204/tip_calc/tip_calc/index.html")
d.find_element(by="id", value="billamt").send_keys("100")
d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
d.find_element(by="id", value="peopleamt").send_keys("5")
d.find_element(by="id", value="calculate").click()
expected = "4.00"
actual = d.find_element(by="id", value="tip").text
is_visible = d.find_element(by="id", value="tip").is_displayed()
if expected != actual:
    print("No good :-(")
else:
    print("Good job! :-)")
assert actual == expected
assert is_visible

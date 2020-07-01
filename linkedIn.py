from selenium import webdriver
import csv
import time

username=input("Enter your Linkedin username :")
password=input("Enter your Password:")

PATH = "D:\PythonC\my_stuff\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/posts/matchai_covid19-hiring-tech-activity-6652411320551464960-Gh_1")

button=driver.find_element_by_xpath("//*[@class='comments__see-more']")
button.click()

userid=driver.find_element_by_id("username");
userid.send_keys(username)

pswid=driver.find_element_by_id("password")
pswid.send_keys(password)

login=driver.find_element_by_xpath("//*[@type='submit']")
login.click()

time.sleep(10)
hasLoadMore = True
while hasLoadMore:
    print("inside while")
    time.sleep(10)
    try:
        print("inside try")
        if driver.find_element_by_xpath("//button[@class='comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']"):
            driver.find_element_by_xpath("//button[@class='comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']").click()
    except:
        print("exception")
        hasLoadMore = False

emails=driver.find_elements_by_css_selector("p a")
names=driver.find_elements_by_css_selector("h3 span")
with open('linkedmails.csv','w',newline='') as f:
	fieldnames=['Emails']
	thewriter=csv.DictWriter(f,fieldnames=fieldnames)
	thewriter.writeheader()
	for ele in emails:
		if (ele.text.find('@')!=-1):
			thewriter.writerow({'Emails':ele.text})

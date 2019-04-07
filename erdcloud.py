
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('selenium')
install_and_import('csv')
install_and_import('js2py')
install_and_import('re')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")
#
## UserAgent값을 바꿔줍시다!
#options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


#options = webdriver.ChromeOptions()
#options.binary_location = './chromedriver/chromedriver_linux64/chromedriver'
#chrome_driver_binary = '/'

print('chrome_options')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--allow-insecure-localhost");


chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")

chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('./chromedriver/chromedriver_linux64/chromedriver',chrome_options=chrome_options)
print('driver finished')


#driver = webdriver.Chrome('./chromedriver/chromedriver_win32/chromedriver')
#driver = webdriver.Chrome('/home/yunjy/python3/erdcloud/chromedriver/chromedriver_linux64/chromedriver')
driver.implicitly_wait(1)
driver.get('https://www.erdcloud.com/login')
print("driver.get('https://www.erdcloud.com/login')")
print(driver.page_source.encode('utf-8'))
#time.sleep(2)
driver.find_element_by_id('email').send_keys("pfs.tmax@gmail.com")
#time.sleep(2)
driver.implicitly_wait(10)
print("id")
#time.sleep(2)
driver.find_element_by_name('password').send_keys("ifrs")
print("pw")
#time.sleep(2)
#time.sleep(5)
#driver.implicitly_wait(30)
print('start to find_element_by_xpath')
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__blaze-root"]/div/div/div[2]/div[2]/div/div[2]/ul/li/a'))).click()
driver.find_element_by_id('log-in-button').click()
   
#driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/div[2]/div/div[2]/ul/li/a').click()
print("find_element_by_xpath")
#driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/section[3]/div/div[1]/div/div/button[3]').click()
print('start to find link_text FS')
driver.find_element_by_link_text('FS').click()
print('finished')
print('start to find class js-btn-export')
driver.find_element_by_class_name('js-btn-export').click()
print('finished')
print('start to find class js-btn-sql-preview')
driver.find_element_by_class_name('js-btn-sql-preview').click()
print('finished')
#driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/section[6]/div/div[2]/a[1]').click()
print('start to find tag textarea[1]')
mytext=driver.find_elements_by_tag_name('textarea')[1].get_attribute('value')
mytext=driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/section[6]/div/div[1]/textarea').get_attribute('value')
print('finished')
print(mytext)
print(type(mytext))

myStr=mytext.replace('\t','').replace(';','').replace('`','')
tblArray=myStr.split('CREATE')
tblArray.pop(0)
tblArray[-1]=tblArray[-1].split("ALTER")[0]
totalTblArray2D=[]
for tblarray in tblArray:
    tempArray = tblarray.split('\n')
    myArray=[]
    filtered=[]
    for temparray in tempArray:
        myArray.append(temparray.replace('TABLE','').replace('VARCHAR(255)','').replace('NOT NULL','').replace('NULL','').replace(',','').replace('(','').replace(')',''))
        while "" in myArray:
            myArray.remove("")
        for k in range(len(myArray)):
            myArray[k]="".join(myArray[k].split())
        Filtered = myArray
    for j in range(len(Filtered)-1):
        totalTblArray2D.append([Filtered[0], Filtered[j+1]])
print(totalTblArray2D)
print(len(totalTblArray2D))




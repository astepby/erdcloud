
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

driver = webdriver.Chrome('./chromedriver/chromedriver_win32/chromedriver')
driver.implicitly_wait(1)
driver.get('https://www.erdcloud.com/login')

driver.find_element_by_id('email').send_keys("pfs.tmax@gmail.com")
driver.implicitly_wait(10)
driver.find_element_by_name('password').send_keys("")
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/div[2]/div/div[2]/ul/li/a').click()

driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/section[3]/div/div[1]/div/div/button[3]').click()
driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/section[6]/div/div[2]/a[1]').click()
mytext=driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div/div[2]/section[6]/div/div[1]/textarea').get_attribute('value')
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




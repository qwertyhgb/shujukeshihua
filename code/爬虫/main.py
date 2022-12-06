import selenium
from selenium import webdriver
import time
import xlwt
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By

wait_time = 180
datalist = []

# 网址
url = f'https://you.ctrip.com/sight/shitai2624/1408445.html'

# 使用谷歌驱动打开浏览器
path = "C:/Users/LM216/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
driver.implicitly_wait(10)

# 寻找每一个节点
for i in range(0, 107):
    try:
        wait.until(lambda driver: driver.find_elements(By.XPATH, "//div[@class='commentItem']/div["
                                                                 "@class='contentInfo']/div/span"))
        col = driver.find_elements(By.XPATH, "//div[@class='commentItem']/div[@class='contentInfo']/div/span")  # 评分
        wait.until(lambda driver: driver.find_elements(By.XPATH, "//div[@class='commentItem']//div["
                                                                 "@class='commentDetail']"))
        col2 = driver.find_elements(By.XPATH, "//div[@class='commentItem']//div[@class='commentDetail']")
        wait.until(lambda driver: driver.find_elements(By.XPATH, "//div[@class='commentItem']//div["
                                                                 "@class='commentTime']"))
        col3 = driver.find_elements(By.XPATH, "//div[@class='commentItem']//div[@class='commentTime']")
        for j in range(0, len(col)):
            data = []
            data.append(col[j].text)
            data.append(col2[j].text)
            data.append(col3[j].text)
            datalist.append(data)
    except Exception as error:
        print(error)
    try:
        wait = ui.WebDriverWait(driver, wait_time)
        button = driver.find_element(By.XPATH, "//li[@title='下一页']")
        button.click()
    except Exception as error:
        print(error)

# 保存数据
book = xlwt.Workbook(encoding="utf-8", style_compression=0)
sheet = book.add_sheet('石台牯牛降景区评价', cell_overwrite_ok=True)
colls = ("评分", "评价", "时间")
for i in range(0, 3):
    sheet.write(0, i, colls[i])
for i in range(0, len(datalist)):
    data = datalist[i]
    for j in range(0, 3):
        sheet.write(i + 1, j, data[j])

book.save("E:/MyCode/jupyterFile/数据可视化/code/爬虫/文本.txt")

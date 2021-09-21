from selenium import webdriver
import time
from datetime import datetime
import datetime
import json
def core_function(real_start, real_end):
    driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
    lib = 'http://zuowei.cczu.edu.cn/'
    cookies_1 = {
        "hostOnly": True,
        "httpOnly": True,
        "name": "JSESSIONID",
        "path": "/",
        "secure": False,
        "session": True,
        "value": "***************************"
    }# 这个cookie已作废
    driver.get(lib)
    driver.delete_all_cookies()
    driver.add_cookie(cookies_1)
    # driver.refresh()
    driver.get(lib)
    driver.find_element_by_xpath("//a[contains(text(),'常用座位')]").click()
    driver.find_element_by_id('seat_8083').click()  # 这个座位也要按照自己的常用位置而改
    time.sleep(3)
    st1 = '/html/body/div[5]/div[1]/div[2]/dl/ul/li/a[@time = '
    st2 = ']'
    st = st1+str(real_start)+st2
    et1 = '/html/body/div[5]/div[1]/div[3]/dl/ul/li/a[@time='
    et2 = ']'
    et = et1+str(real_end)+et2
    driver.find_element_by_xpath(st).click()
    time.sleep(1)
    driver.find_element_by_xpath(et).click()
    driver.find_element_by_xpath('//*[@id="reserveBtn"]').click()

def timebh(hours, minutes):
    minutes_time = hours*60+minutes
    return minutes_time

def core_function2(selectTime, choiceRoom,letsStart, letsEnd,tableStart, tableEnd):
    driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
    lib = 'http://zuowei.cczu.edu.cn/'
    cookies_1 = {
        "hostOnly": True,
        "httpOnly": True,
        "name": "JSESSIONID",
        "path": "/",
        "secure": False,
        "session": True,
        "value": "**************************"
    }  # 这个cookie已作废
    driver.get(lib)
    driver.delete_all_cookies()
    driver.add_cookie(cookies_1)
    # driver.refresh()
    driver.get(lib)
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[1]/a').click()  # 自选作位
    driver.find_element_by_xpath('//*[@id="display_onDate"]').click()
    # time.sleep(1)
    data1 = '//*[@id="options_onDate"]/a['
    data2 = ']'
    data = data1+str(selectTime)+data2
    driver.find_element_by_xpath(data).click()  # 选择日期
    driver.find_element_by_xpath('//*[@id="display_building"]').click()
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="options_building"]/a[2]').click()  # 选择校区，虽然现在没有校区可选
    driver.find_element_by_xpath('//*[@id="display_room"]').click()
    # time.sleep(1)
    floor1 = '//*[@id="options_room"]/a['
    floor2 = ']'
    floor = floor1+str(choiceRoom)+floor2
    driver.find_element_by_xpath(floor).click()  # 选择楼层/南北区
    driver.find_element_by_xpath('//*[@id="display_hour"]').click()
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="options_hour"]/a[2]').click()  # 选择时间长度，都用这个了，还不选个最长的？
    driver.find_element_by_xpath('//*[@id="display_startMin"]').click()
    # time.sleep(1)
    startT1 = '//*[@id="options_startMin"]/a['# 问题代码
    startT2 = ']'
    startT = startT1+str(tableStart)+startT2
    driver.find_element_by_xpath(startT).click()  # a从1-97，指的是从null,0,15这样
    driver.find_element_by_xpath('//*[@id="display_endMin"]').click()
    # time.sleep(1)
    endT1 = '//*[@id="options_endMin"]/a['# 问题代码
    endT2 = ']'
    endT = endT1+str(tableEnd)+endT2

    driver.find_element_by_xpath(endT).click()  # 结束时间
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()  # 查询
    time.sleep(2)
    try:
        zuowei = driver.find_element_by_css_selector('.free').click()
    except Exception as e:
        print('没找到对不起')
        # zuowei = driver.find_elements_by_css_selector('.free')
    # for i in zuowei:
    #       print(i.text)
    time.sleep(3)
    st1 = '/html/body/div[5]/div[1]/div[2]/dl/ul/li/a[@time = '
    st2 = ']'
    st = st1+str(letsStart)+st2
    et1 = '/html/body/div[5]/div[1]/div[3]/dl/ul/li/a[@time='
    et2 = ']'
    et = et1+str(letsEnd)+et2
    driver.find_element_by_xpath(st).click()
    time.sleep(1)
    driver.find_element_by_xpath(et).click()
    driver.find_element_by_xpath('//*[@id="reserveBtn"]').click()

if __name__ == '__main__':
    studyData = input('请输入学习时间：今天（1）或明天（2）')
    now4 = datetime.datetime.now()
    now1 = datetime.timedelta(days=1, )
    now3 = datetime.timedelta(hours=now4.hour, minutes=now4.minute, seconds=now4.second, microseconds=now4.microsecond)
    now2 = now4 + now1 - now3

    studyFloor = input('学习楼层：不限：0；二楼北区：1；二楼南区：2；五楼北区：3；五楼南区：4；六楼：5；三楼阅读空间：6')
    hours, minutes = map(int, input('请输入开始时间。格式为：9：30；最好为整数').split(':'))
    start_hour = timebh(hours, minutes)
    startHour = int(start_hour)
    end_hours, end_minutes = map(int, input('请输入结束时间，注意最长为4小时:').split(':'))
    end_hour = timebh(end_hours, end_minutes)
    endHour = int(end_hour)
    print(type(hours))
    print(type(minutes))
    print(endHour, startHour)
    # real_start = 30-startHour % 30+startHour
    # real_end = 30-endHour % 30+endHour
    table_start = startHour/15+1
    table_end = endHour / 15 + 1
    while True:
        now = datetime.datetime.now()
        if startHour - endHour <= 240 and now ==now4:
            core_function2(studyData, studyFloor,  startHour, endHour, table_start, table_end)
        else:
            print('这太久了，这活干不了！')












'''
if __name__ == '__main__':#
    hours, minutes = input('请输入开始时间。格式为：9：30；最好为整数').split(':')
    start_hour = timebh(hours, minutes)
    end_hours, end_minutes = input('请输入结束时间，注意最长为4小时').split(':')
    end_hour = timebh(end_hours, end_minutes)
    real_start=30-start_hour%30+start_hour
    real_end=30-end_hour%30+end_hour
    if real_start - real_end <= 240:
        core_function(real_start, real_end)
    else:
        print('这太久了，这活干不了！')
'''




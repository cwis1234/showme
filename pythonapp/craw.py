import tkinter
from tkinter import ttk
from selenium import webdriver
import urllib.request
import os
def clickStart():
    a = strpath.get()
    print(a)
    crawling(a)
    return


def crawling(webpath):
    path = "D:/driver/chromedriver"
    driver = webdriver.Chrome(path)
    driver.get(webpath)
    driver.set_window_size(1920, 3000)
    li_list = driver.find_elements_by_tag_name("li")
    nov_list = []
    for i in li_list:
        nov_list.append(i.get_attribute("data-productid"))
    nov_list = nov_list[:-5]
    print(nov_list)

    imgdir = "D:/image/mok"
    ind = 0
    for i in nov_list[0:3]:
        nov_path = "https://page.kakao.com/viewer?productId=" + i
        driver.get(nov_path)

        driver.implicitly_wait(3)
        fir_elem = driver.find_element_by_class_name("jsx-36836804.iconWrap.iconWrap_pc")
        sec_elem = driver.find_element_by_class_name("jsx-36836804")
        sec_elem.click()
        # 첫 클릭 끝

        fir_elem = driver.find_element_by_class_name("jsx-720725770.jsx-2517120121.pageCount pageCount_pc")
        count = fir_elem.text
        real_count = int(count.split('/')[1])
        print(count)

        for j in range(1, real_count+1):
            fir_elem = driver.find_element_by_class_name(
                "jsx-2926717397.horizontalContentsBox.horizontalContentsBox_pc")
            img_list = fir_elem.find_elements_by_tag_name("img")
            cur_img = img_list[1]
            gg = imgdir+'/'+str(ind)+'.png'
            cur_img.screenshot(gg)
            btn_nxt = img_list[2]
            btn_nxt.click()
            driver.implicitly_wait(3)
            ind += 1
        print("end")
    return


window = tkinter.Tk()

window.title("탐색기")
# window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text="주소", anchor="nw")
label.grid(column=0, row=0)

strpath = tkinter.Entry(window)
strpath.grid(column=1, row=0)

btn = tkinter.Button(window, text="가져오기", command=clickStart)
btn.grid(column=2, row=0)

window.mainloop()
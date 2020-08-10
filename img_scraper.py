from tkinter import *
from naver_img import open_browser, get_imgs
from tkinter import messagebox


root = Tk()
root.title("이미지 크롤러")
root.geometry("400x250")

#variable
date = StringVar()
choices = ['전체', '1일', '1주일', '1개월', '6개월', '1년']
date.set('전체')

keyword = StringVar()
num = IntVar()
face = IntVar()


#functions
def change_dropdown(*args):
    if date.get() == '전체':
        datetype=0
    elif date.get() == '1일':
        datetype=1
    elif date.get() == '1주일':
        datetype=2
    elif date.get() == '1개월':
        datetype=3
    elif date.get() == '6개월':
        datetype=4
    elif date.get() == '1년':
        datetype=5
    return datetype
def start_crawl():
    QUERY = keyword.get()
    NUM = num.get()
    DATETYPE = date.get()
    FACETYPE = face.get()

    IMGS = open_browser(QUERY, NUM, DATETYPE, FACETYPE)
    get_imgs(IMGS, keyword.get())
    messagebox.showinfo('정보', '크롤링 완료!')
#label
keyword_label = Label(root, text="키워드:")
keyword_label.grid(row=0, column=0, padx=5, pady=5)

num_label = Label(root, text="수량:")
num_label.grid(row=1, column=0, padx=5, pady=5)

date_label = Label(root, text="기간")
date_label.grid(row=3, column=0, padx=5, pady=5)

#popupmenu
popupMenu = OptionMenu(root, date, *choices)
popupMenu.grid(row = 3, column =1)
date.trace('w', change_dropdown)

#check
recent_check = Checkbutton(root, text="인물중심", variable=face)
recent_check.grid(row=2, column=0, columnspan=2, pady=5)

#entry
keyword_entry = Entry(root, width=10, textvariable=keyword)
keyword_entry.grid(row=0, column=1, pady=5)

num_entry = Entry(root, width=10,textvariable=num)
num_entry.grid(row=1, column=1, pady=5)

#button
search_btn = Button(root, text="크롤링 시작!", command=start_crawl)
search_btn.grid(row=4, column=0, columnspa=2, pady=5)

root.mainloop()
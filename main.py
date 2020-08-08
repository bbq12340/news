import google
import naver
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import csv

root = tk.Tk()
root.title("기사 크롤러")
root.geometry("400x400")

keyword = tk.StringVar()
pages = tk.IntVar()
recent = tk.IntVar()

def start_crawl():
    print("Start Crawling")
    CSVFILE = f'{keyword.get()}.csv'
    try:
        if recent.get() == 0:
            google_df = google.search_google(pages.get(), keyword.get())
            naver_df = naver.search_naver(pages.get(), keyword.get())
            if len(google_df.index) == 0 or len(naver_df.index) == 0:
                messagebox.showinfo("정보", "짧은 시간 내에 요청 수가 너무 많습니다.")
            frames = [google_df, naver_df]
            result = pd.concat(frames, ignore_index=True)
            result.to_csv(CSVFILE, encoding='utf-8')
            messagebox.showinfo("정보", "크롤링 완료!")
        elif recent.get() == 1:
            google_df = google.search_google(pages.get(), keyword.get(), enable_recent=True)
            naver_df = naver.search_naver(pages.get(), keyword.get(), enable_recent=True)
            frames = [google_df, naver_df]
            if len(google_df.index) == 0 or len(naver_df.index) == 0:
                messagebox.showinfo("정보", "짧은 시간 내에 요청 수가 너무 많습니다.")
            result = pd.concat(frames, ignore_index=True)
            result.to_csv(CSVFILE, encoding='utf-8')
            messagebox.showinfo("정보", "크롤링 완료!")
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(f"https://www.google.com/search?q={keyword.get()}&source=lnms&tbm=fin")
    except IndexError:
        messagebox.showerror("에러", "구글 또는 네이버의 페이지를 넘어가는 요청의 수입니다.")
#label
keyword_label = tk.Label(root, text="키워드:")
keyword_label.grid(row=0, column=0, padx=5, pady=5)

page_label = tk.Label(root, text="페이지 수:")
page_label.grid(row=1, column=0, padx=5, pady=5)


#entry
keyword_entry = tk.Entry(root, textvariable=keyword)
keyword_entry.grid(row=0, column=1, pady=5)

pages_entry = tk.Entry(root, textvariable=pages)
pages_entry.grid(row=1, column=1, pady=5)

#check
recent_check = tk.Checkbutton(root, text="최신순", variable=recent)
recent_check.grid(row=2, column=0, columnspan=2, pady=5)

#button
search_btn = tk.Button(root, text="크롤링 시작!", command=start_crawl)
search_btn.grid(row=3, column=0, columnspa=2, pady=5)



root.mainloop()




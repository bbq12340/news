import google
import naver
import pandas as pd
import tkinter as tk

root = tk.Tk()
root.title("기사 크롤러")
root.geometry("400x400")

keyword = tk.StringVar()
pages = tk.IntVar()
recent = tk.IntVar()

def start_crawl():
    print("Start Crawling")
    try:
        if recent.get() == 0:
            google_df = google.search_google(pages.get(), keyword.get())
            naver_df = naver.search_naver(pages.get(), keyword.get())
            frames = [google_df, naver_df]
            result = pd.concat(frames, ignore_index=True)
            result.to_csv('sheet.csv')
            print("finished")
        elif recent.get() == 1:
            google_df = google.search_google(pages.get(), keyword.get(), enable_recent=True)
            naver_df = naver.search_naver(pages.get(), keyword.get(), enable_recent=True)
            frames = [google_df, naver_df]
            result = pd.concat(frames, ignore_index=True)
            result.to_csv('sheet.csv')
            print("finished")
    except IndexError:
        print("구글 또는 네이버의 페이지를 넘어가는 요청의 수입니다.")
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




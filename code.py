import os
import tkinter as tk
from tkinter import filedialog

def save_video_filenames():
    # Mở hộp thoại chọn thư mục chứa video
    video_directory = filedialog.askdirectory(title="Chọn thư mục chứa video")
    if not video_directory:
        print("Không có thư mục nào được chọn.")
        return
    
    # Mở hộp thoại chọn thư mục lưu file txt
    save_directory = filedialog.askdirectory(title="Chọn thư mục lưu danh sách video")
    if not save_directory:
        print("Không có thư mục nào được chọn.")
        return
    
    output_file = os.path.join(save_directory, "video_list.txt")
    
    # Các định dạng video phổ biến
    video_extensions = (".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm")
    
    # Lấy danh sách tất cả các tệp video trong thư mục
    video_files = [f for f in os.listdir(video_directory) if f.lower().endswith(video_extensions)]
    
    # Lưu danh sách vào tệp văn bản
    with open(output_file, "w", encoding="utf-8") as file:
        for video in video_files:
            file.write(video + "\n")
    
    print(f"Đã lưu {len(video_files)} tên video vào {output_file}")

# Giao diện chọn thư mục
root = tk.Tk()
root.withdraw()
save_video_filenames()

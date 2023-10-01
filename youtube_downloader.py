import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    # Get the YouTube video link from the text box
    video_link = entry.get()
    
    try:
        # Download the video using pytube
        yt = YouTube(video_link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download()
        
        # Update the GUI with the download status
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        # Update the GUI with the error message
        messagebox.showerror("Error", "Failed to download video: " + str(e))

# Create the GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

# Add a text box to enter the YouTube video link
entry = tk.Entry(root, width=50)
entry.pack()

# Add a button to initiate the download
button = tk.Button(root, text="Download", command=download_video)
button.pack()

# Run the GUI
root.mainloop()

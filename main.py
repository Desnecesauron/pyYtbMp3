#https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
from logging import exception
import yt_dlp as youtube_dl
from tkinter import BOTH, END, Tk, Listbox, Button, StringVar, Label, Text
from threading import Thread
import random

numtextos = 0

class janela(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self, master=None):
        global numtextos
        numtextos+=1
        janela = Tk()
        janela.geometry('650x520')
        janela.resizable(False, False)
        janela.title("Downloader (Youtube, Instagram, Facebook, Twitter, Globo)")
        janela["bg"]="#a3a091"

        global Lb1
        Lb1 = Listbox(janela)
        Lb1.insert(END, "")
        Lb1.pack(side="top", fill=BOTH)
        Lb1.configure(width=50, height=18)

        var = StringVar()
        descriptionURL = Label (janela, textvariable=var)
        var.set("Digite abaixo a URL")
        descriptionURL.pack()

        global text_box
        text_box = Text(
            janela,
            height=1,
            width=72,
            
        )
        text_box.pack(expand=True)
        text_box.config(state='normal')
        
        botao1 = Button(janela, text='Sair', command=self.btn_sair)
        botao1.pack(side="bottom", fill="both")

        botao3 = Button(janela, text='Converter para MP3', command=self.btn_MP3)
        botao3.pack(side="bottom", fill="both")

        botao2 = Button(janela, text='Converter para MP4', command=self.btn_MP4)
        botao2.pack(side="bottom", fill="both")

        janela.mainloop()
                
    def btn_sair(self):
        exit()

    def btn_MP4(self):
        if(len(text_box.get("1.0", 'end-1c'))<10 or not(text_box.get("1.0", 'end-1c').__contains__("."))):
            return
        msgTk("MP4 -- " + text_box.get("1.0", 'end-1c') + " -- Downloading...")
        runMP4().start()

    def btn_MP3(self):
        if(len(text_box.get("1.0", 'end-1c'))<10 or not(text_box.get("1.0", 'end-1c').__contains__("."))):
            return
        msgTk("MP3 -- " + text_box.get("1.0", 'end-1c') + " -- Downloading...")
        runMP3().start()

class runMP3(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self, master=None):
        try:

            video_url = text_box.get("1.0", 'end-1c')
            text_box.delete('1.0',END)

            if(video_url.__contains__("&list=")):
                video_urlSemPlaylist = video_url[0:video_url.find('&list')]
                video_url = video_urlSemPlaylist
                
            try:
                video_info = youtube_dl.YoutubeDL().extract_info(
                    url = video_url,download=False
                )
            except:
                msgTk("An error ocurred, is the link maybe broke?")
                return

            if(video_url.__contains__("facebook") or video_url.__contains__("fb")):
                filename = f"{random.randint(1,9999999999999)}_Facebook.mp3"
                options={
                    'format':'bestaudio/best',
                    'keepvideo':False,
                    'outtmpl':filename,
                }
            else:
                filename = f"{video_info['title']}.mp3"
                options={
                    'format':'bestaudio/best',
                    'keepvideo':False,
                    'outtmpl':filename,
                }

            with youtube_dl.YoutubeDL(options) as ydl:
                try:
                    ydl.download([video_info['webpage_url']])
                except:
                    msgTk("An error ocurred, probably an error in HTTP request")
                    return

            msgTk("Download complete: {}".format(filename))
        except:
            msgTk("An error ocurred, is the link maybe broke?")
            return

class runMP4(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self, master=None):
        try:

            video_url = text_box.get("1.0", 'end-1c')
            text_box.delete('1.0',END)

            if(video_url.__contains__("&list=")):
                video_urlSemPlaylist = video_url[0:video_url.find('&list')]
                video_url = video_urlSemPlaylist
                
            try:
                video_info = youtube_dl.YoutubeDL().extract_info(
                    url = video_url,download=False
                )
            except:
                msgTk("An error ocurred, is the link maybe broke?")
                return
            
            if(video_url.__contains__("facebook") or video_url.__contains__("fb")):
                filename = f"{random.randint(1,9999999999999)}_Facebook.mp4"
                options={
                    'format':'best/best',
                    'keepvideo':True,
                    'outtmpl':filename,
                }    
            else:
                filename = f"{video_info['title']}.mp4"
                options={
                    'format':'best/best',
                    'keepvideo':True,
                    'outtmpl':filename,
                }

            with youtube_dl.YoutubeDL(options) as ydl:
                try:
                    ydl.download([video_info['webpage_url']])
                except:
                    msgTk("An error ocurred, probably an error of connection")
                    return

            msgTk("Download complete: {}".format(filename))
        except:
            msgTk("An error ocurred, is the link maybe broke?")
            return

def msgTk(msg):
    try:
        global numtextos
        numtextos+=1
        if numtextos>16:
            Lb1.delete(0,'end')
            numtextos=0
        Lb1.insert(END, msg)
    except:
        print("an error has gone: ")
        print(exception)
        return

if __name__=='__main__':
    framerr = janela()
    framerr.start()

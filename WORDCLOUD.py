pip install wordcloud
pip install fileupload
pip install ipywidgets
jupyter nbextension install --py --user fileupload
jupyter nbextension enable --py fileupload
pip install speechRecognition
pip install PyAudio



import wordcloud
from matplotlib import pyplot as plt
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk
import fileupload
import tkinter
import tkinter.filedialog 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import speech_recognition as sr



root=Tk()
root.title("WORD CLOUD")
root.configure(bg="rosy brown")
w = Label(root, text="WORD CLOUD",padx=25,pady=11,bg = "rosy brown",fg="lavender",font=("Times",20))
w.pack()



def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)        
    file_contents = r.recognize_google(audio)
    e.insert(INSERT, file_contents)
    def calculate_frequencies(file_contents):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

        non_punctuation_text=""
        for char in file_contents:
            if char not in punctuations:
                non_punctuation_text=non_punctuation_text+char
        words=non_punctuation_text.split()
        clean_words=[]
        frequencies={}
        for word in words:
            if word.isalpha():
                if word not in uninteresting_words:
                    clean_words.append(word)
        for alpha_word in clean_words:
            if alpha_word not in frequencies:
                frequencies[alpha_word]=1
            else:
                frequencies[alpha_word]+=1
        cloud = wordcloud.WordCloud()
        cloud.generate_from_frequencies(frequencies)
        return cloud.to_array()

    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')   
    plt.savefig("result.png", dpi=70)      
    i = PIL.Image.open("result.png")
    photo = ImageTk.PhotoImage(i)
    label = tk.Label(root, bg = "rosy brown",image=photo)
    label.image = photo
    label.pack()  

def view():
    text = e.get("1.0",'end-1c')
    with open("filepy.txt", "w") as outf:
        outf.write(text)
    file_contents=open("filepy.txt") 
    def calculate_frequencies(file_contents):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

        non_punctuation_text=""
        for char in file_contents:
            if char not in punctuations:
                non_punctuation_text=non_punctuation_text+char
        words=non_punctuation_text.split()
        clean_words=[]
        frequencies={}
        for word in words:
            if word.isalpha():
                if word not in uninteresting_words:
                    clean_words.append(word)
        for alpha_word in clean_words:
            if alpha_word not in frequencies:
                frequencies[alpha_word]=1
            else:
                frequencies[alpha_word]+=1
        cloud = wordcloud.WordCloud()
        cloud.generate_from_frequencies(frequencies)
        return cloud.to_array()

    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')   
    plt.savefig("result.png", dpi=70)      
    image = PIL.Image.open("result.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, bg = "rosy brown",image=photo)
    label.image = photo
    label.pack()  
    
def UploadAction(event=None):
    file = filedialog.askopenfilename(filetypes=([('All files', '*.*'),('Text files', '*.txt'),('CSV files', '*.csv')])) 
    file_contents=open(file, encoding="utf8")
    def calculate_frequencies(file_contents):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
        non_punctuation_text=""
        for char in file_contents:
            if char not in punctuations:
                non_punctuation_text=non_punctuation_text+char
        words=non_punctuation_text.split()
        clean_words=[]
        frequencies={}
        for word in words:
            if word.isalpha():
                if word not in uninteresting_words:
                    clean_words.append(word)
        for alpha_word in clean_words:
            if alpha_word not in frequencies:
                frequencies[alpha_word]=1
            else:
                frequencies[alpha_word]+=1
        cloud = wordcloud.WordCloud()
        cloud.generate_from_frequencies(frequencies)
        return cloud.to_array()
    
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')   
    plt.savefig("result.png", dpi=70)      
    image = PIL.Image.open("result.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, bg = "rosy brown",image=photo)
    label.image = photo
    label.pack()
    
p = PhotoImage(file="Capture.PNG") 
b1=Button(root,text="Build Dynamically",bg = "lavender",fg = "black",padx=22,pady=11,command=view)
b2=Button(root,text="Build from a file",padx=25,pady=11,bg = "lavender",fg = "black",command= UploadAction)
b4=Button(root,image = p,text="voice",bg = "lavender",fg = "olive",command= voice)
b3 = Button(root, text = "Exit",padx=25,pady=11,bg = "light coral",fg = "black",command = root.destroy) 
b2.pack( side = LEFT)
b1.pack( side = LEFT)
b4.pack(side=LEFT)
b3.pack( side = LEFT)
e=Text(root, width=51, height=15, borderwidth=5)  
e.pack(padx=10,pady=10)

root.mainloop()

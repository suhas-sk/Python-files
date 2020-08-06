# Instagram Profile downloader
from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import json, requests, urllib.request, tkinter as tk

# Creating necessary tkinter widgets
def create_Widgets():
    #Creating Label widget
    urlLabel = Label(root, text="INSTAGRAM ID: ",background="black", foreground="white")
    urlLabel.grid(row=0, column=0, padx=8,pady=8)

    '''
    The padx puts some space between the adjacent buttons and right or left border of the root window
    The pady puts some space between the adjacent buttons and borders of frame and root window    
    '''

    #Creating entry widget to enter the ID
    root.urlEntry = Entry(root, width=35, textvariable=insta_id)
    root.urlEntry.grid(row=0,column=1,columnspan=2,pady=8)      #columnspan=2 => It will soan 2 columns, column 1 & 2

    #Creating download button
    button = Button(root,text="Download", foreground="white",background="black",command=Download)
    button.grid(row=0, column=3,padx=8,pady=8)


    root.resultLabel = Label(root, textvariable=dwldtxt,background="lightblue")
    root.resultLabel.grid(row=1,column=0,columnspan=4,padx=8,pady=8)   #It will span 4 columns
    root.resultLabel.config(font=(25))

    #Creating a Label for Preview
    root.previewLabel = Label(root,text="DP Preview",background="black",foreground="white")
    root.previewLabel.grid(row=2,column=0,padx=8,pady=8)

    root.dplabel = Label(root,background="lightblue")
    root.dplabel.grid(row=3,column=1,columnspan=2, padx=1, pady=1)

# Defining Download function to download Instagram profile pic
def Download():

    #Storing the path where to download the pic in variable
    download_path = "ig_username "

    #Feteching the user input-instagram id
    ig_username = insta_id.get()

    #Concatnating user input and and instagran URL
    insta_url = "https://www.instagram.com/" + ig_username

    # Sending request to the Insta url and storing the response
    ig_response = requests.get(insta_url)

    # Using html parser
    soup = BeautifulSoup(ig_response.text,'html.parser')

    # finding the <script> whose text match with the 'window._sharedData' using re.compile
    script = soup.find('script', text=re.compile('window._sharedData'))

    # Splitting the text of script 1 time at '=' annd fetching the the item at index 1
    # Removing the ';' from the string
    page_json = script.text.split('=', 1)[1].rstrip(';')

    # Parsing the above json page_json string using json.loads() which is very long
    # dictionary consisting of 19 items
    data = json.loads(page_json)

    # The  profile pic url is present in value of key 'entry_data' which itself is a distionary
    dp_url = data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']

    # Concatenating download path , username and .jpg extension
    dp_name = download_path+ig_username+'.jpg'

    # Download the profile pic from url and save under ddp_name
    urllib.request.urlretrieve(dp_url, dp_name)

    # Open the image using Image module in Pillow
    dp_image = Image.open(dp_name)


    # Resize the image using Image.resize
    dp_image = dp_image.resize((600, 600), Image.ANTIALIAS)


    # Creating an object of ImageTk.PhotoImage() class to display the frame
    image = ImageTk.PhotoImage(dp_image)

    # Configuring the label and displaying the image
    root.dplabel.config(image=image)
    root.dplabel.photo = image

    dwldtxt.set('DP Dowloaded successfully')




# Creating Main Window
root = tk.Tk()

#Setting the title and background color
root.geometry("950x650")
root.title("Instagram DP Downloader")
root.config(background="lightblue")

#Creating tkinter variable
insta_id = StringVar()
dwldtxt = StringVar()

#Calling the create_Widget window
create_Widgets()

#defining infinite loop
root.mainloop()


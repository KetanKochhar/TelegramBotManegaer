import pyfiglet
import os 
import platform
import requests
import time

# Fetchinng the data from files and storing them locallacy in python lists
fetcheddata = []

# banner of telegram
def banner():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")        
    print(pyfiglet.figlet_format("send message to telegram"))

# Getting the token and chat Id fromm user and storing it in txt file locallay
def getData(Token,chatId,messageid):
    file = open("telegramData.txt","w")
    data = f"{Token}\n{chatId}\n{messageid}"
    file.writelines(data)
    file.close()

if "telegramData.txt" in os.listdir():
    pass
else:
    banner()
    Token = input("Enter the token of your Bot : ")
    chatId = input("Enter the Chat Id of your topic : ")
    messageid = input("Enetr the message id of your chat : ")
    getData(Token,chatId,messageid)
    print("Fetching data.....")
 

# Getting the data from text file 
def FetchData():
    FetchingFile = open("telegramData.txt","r")
    data = FetchingFile.readlines()
    # deleting \n
    Token = data[0].strip("\n")
    chatId = data[1].strip("\n")
    messageid=data[2]
    fetcheddata.append(Token)
    fetcheddata.append(chatId)
    fetcheddata.append(messageid)
FetchData()


# Basic Telegarm Api for posting the requsts
telegarmApi = f"https://api.telegram.org/bot{fetcheddata[0]}"
def checkBot():
    update = requests.post(f"{telegarmApi}/getupdates")
    if update.status_code == 200:
        print("Bot is connected sucessfully")
    else:
        print("Bot is not connnected")

def sendText():
    message = input("Enter the text message to be send: ")
    sendingData = {"chat_id":fetcheddata[1],"text":message,'reply_to_message_id':fetcheddata[2]}
    sendTextUrl =f"{telegarmApi}/sendmessage"
    url= requests.post(sendTextUrl,sendingData)
    if url.status_code == 200:
        print("Sucessfully send the message")
    else:
        print("Some Eror while sending the message")

def SendPhoto():
    photourl = input("Drop your photo here : ")
    sendphotouserdata = {"chat_id": fetcheddata[1], "reply_to_message_id": fetcheddata[2]}
    with open(photourl, 'rb') as photo_file:
        sendfiledata = {'photo': (photourl, photo_file)}
        sendingurl = f"{telegarmApi}/sendphoto"
        url = requests.post(sendingurl, data=sendphotouserdata, files=sendfiledata)
        if url.status_code == 200:
            print("Photo sent successfully")
        else:
            print("Error while sending the photo")
            print(url.json())

def SendDocument():
    docurl = input("Drop Your document here : ")
    senddocuserdata={"chat_id":fetcheddata[1],"reply_to_message_id":fetcheddata[2]}
    senddocdata={"document":open(docurl,"rb")}
    sendingurl = f"{telegarmApi}/senddocument"
    url = requests.post(sendingurl,data=senddocuserdata,files=senddocdata)
    if url.status_code == 200:
        print("sucessfuly send the file ")
    else:
        print("error while sending the document")

while True:
    
    FetchData()
    banner()
    print("select the options with the numbers to exit press Ctrl + C")
    print("1. Check Bot")
    print("2. Send Text")
    print("3. Send Image")
    print("4. Send Document")
    print("5. Exit")
    user_input = input("select the option [1-5]: ")
    if user_input == "1":
        checkBot()
        time.sleep(2)
    elif user_input == "2":
        sendText()
        time.sleep(2)
    elif user_input == "3":
        SendPhoto()
        time.sleep(2)
    elif user_input == "4":
        SendDocument()
        time.sleep(2)
    elif user_input == "5":
        print("Exting telegarm Bot...")
        time.sleep(2)
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        break
    else:
        print("Not a valid option")
        time.sleep(2)
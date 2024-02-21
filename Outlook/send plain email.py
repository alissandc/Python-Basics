import win32com.client as client

def create_email():
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.To = "alissa_lopez542@outlook.com"
    message.CC = "alissa_lopez542@outlook.com"
    message.BCC = "alissa_lopez542@outlook.com"
    message.Subject = "Happy Birthday"
    message.Body = "Wish you a happy birthday!"
    message.Display()
    message.Save()
    message.Send()

if __name__ == '__main__':
    create_email()
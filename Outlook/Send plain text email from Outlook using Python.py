import win32com.client as client
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
message.To = "alissa_lopez542@outlook.com"
message.CC = "alissa_lopez542@outlook.com"
message.BCC = "alissa_lopez542@outlook.com"
message.Subject = "Happy Birthday"
message.Body = "Wish you a happy birthday!"
#message.SentOnBehalfofName
message.Save()
message.Send()
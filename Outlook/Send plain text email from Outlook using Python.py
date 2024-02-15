import win32com.client as client
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
message.To = "hoarders2@gmail.com"
message.CC = "hoarders2@gmail.com"
message.BCC = "hoarders2@gmail.com"
message.Subject = "Happy Birthday"
message.Body = "Wish you a happy birthday!"
#message.SentOnBehalfofName
message.Save()
message.Send()
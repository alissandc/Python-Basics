import win32com.client as client
import pathlib
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
#message.Display()
cake_path = pathlib.Path('C:\Users\Alissandra\docus\20200923_113459_prada.jpg')
cert_path = pathlib.Path('C:\Users\Alissandra\docus\missing npc.jpg')
#print(cake_path.absolute)
cake_absolute = str(cake_path.absolute())
cert_absolute = str(cert_path.absolute())
message.Display()
message.To = "hoarders2@gmail.com"
message.Subject = "Happy Birthday"
message.Attachments.Add(cert_absolute)
image = message.Attachments.Add(cake_absolute)
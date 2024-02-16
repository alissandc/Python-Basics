import win32com.client as client
from pathlib import Path
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
#message.Display()
cake_path = Path(r'C:\Users\Alissandra\PC\Downloads\pictures_git', 'fashioncat-lede-1300x1950.jpg')
cert_path = Path(r'C:\Users\Alissandra\PC\Downloads\pictures_git','missing npc.jpg')
cake_absolute = str(cake_path.absolute())
cert_absolute = str(cert_path.absolute())
message.Display()
message.To = "hoarders2@gmail.com"
message.Subject = "Happy Birthday"
message.Attachments.Add(cert_absolute)
image = message.Attachments.Add(cake_absolute)
image.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "cake-img")
html_body = """
    <div>
        <h1 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
            Happy Birthday!!
        </h1>
        <span style="font-family: 'Lucida Sans'; font-size: 28; color: #8d395c;">
            Wishing you all the best on your birthday!!
        </span>
    </div><br>
    <div>
        <img src="cid:cake-img" width=50%>
    </div>

"""
message.HTMLBody = html_body
message.Save()
message.Send()

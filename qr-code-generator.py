import pyqrcode 
  
# String which represent the QR code 
link = "https://github.com/iyuldashev"
  
# Generate QR code 
url = pyqrcode.create(link) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8)
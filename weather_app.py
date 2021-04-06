from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("Air Quality Check")
root.iconbitmap("icon.png")
root.geometry("600x100")

# Create zipcode lookup function
def zipLookup():
#     zip.get()
#     zipLabel = Label(root, text=zip.get())
#     zipLabel.grid(row=1, column=0, columnspan=2)
    
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=B645117F-5DF4-443D-BE41-4F626D43E6DC")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sesitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
            
        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

# APIs return data in different formats

# api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11206&distance=5&API_KEY=B645117F-5DF4-443D-BE41-4F626D43E6DC")
    
    
zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipBtn = Button(root, text="Lookup Zipcode", command=zipLookup)
zipBtn.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()


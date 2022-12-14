import urllib.parse
import requests
import tkinter as tk



def quit(self):
    self.destroy()
    exit()
def output():
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "FkKyOGoGjKTmJfAMaCArRuCL3f1PslfO"
    output_win = tk.Tk()
    output_win.title("MapQuest API")
    output_win.geometry("600x600")

    outframe1 = tk.Frame(master=output_win, width=500, height=500)
    outframe2 = tk.Frame(master=output_win, width=500, height=500)

    orig=in1.get("1.0","end-1c")
    dest=in2.get("1.0","end-1c")

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        output1 = tk.Label(master=outframe1,  text='API Status: ' + str(json_status) + ' = A successful route call.', width=200)
        output1.pack()
        output2 = tk.Label(master=outframe1,  text='Directions from ' + (orig) + ' to ' + (dest), width=200)
        output2.pack()
        output3 = tk.Label(master=outframe1,  text='Trip Duration: ' + (json_data["route"]["formattedTime"]), width=200)
        output3.pack()
        output4 = tk.Label(master=outframe1,  text='Kilometers: ' + str("{:.2f}".format((json_data["route"]["distance"])*1.61)), width=200)
        output4.pack()
        output5 = tk.Label(master=outframe1,  text='Route Type: ' + (json_data['route']['options']['routeType']), width=200)
        output5.pack()
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            output6 = tk.Label(master=outframe1,  text=(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"), width=200).pack()
        outframe1.pack()
        
    elif json_status == 402:
        error1 = tk.Label(master=outframe1,  text='API Status: ' + str(json_status) + '; Invalid user inputs for one or both locations.', width=200)
        error1.pack()
        outframe1.pack()
        
    elif json_status == 611:
        error2 = tk.Label(master=outframe1,  text='API Status: ' + str(json_status) + '; Missing an entry for one or both locations.', width=200)
        error2.pack()
        outframe1.pack()
        
    else:
        error3 = tk.Label(master=outframe1,  text='For status code: ' + str(json_status) + '; Refer to: ', width=200)
        error3.pack() 
        error3_1 = tk.Label(master=outframe1,  text='https://developer.mapquest.com/documentation/directions-api/status-codes', width=200)
        error3_1.pack()
        outframe1.pack()
        
           
    line = tk.Label(master=outframe2, text='======================================').pack()
    remarks = tk.Label(master=outframe2, text='Do you want to enter another route?').pack()
    b1 = tk.Button(master=outframe2, text='Yes', width=10,bg='Green',command= output_win.destroy).pack() # button added
    b2 = tk.Button(master=outframe2, text='No', width=10,command=lambda: quit(window)).pack() # button added
    output6 = tk.Label(master=outframe2,  text=(json_data['info']['copyright']['text']), width=200)
    output6.pack()
    outframe2.pack()
    


#Code for the Tkinter
window = tk.Tk()
window.title("MapQuest API")
window.geometry("400x200")

#Frames of window
frame1 = tk.Frame(master=window, width=500, height=500)
frame2 = tk.Frame(master=window, width=500, height=500)
frame3 = tk.Frame(master=window, width=500, height=500)
frame4 = tk.Frame(master=window, width=500, height=500)

l1 = tk.Label(master=frame1,  text='Starting Location', width=20).pack() # added one Label 
l2 = tk.Label(master=frame3,  text='Destination', width=20 ).pack() # added one Label 

in1 = tk.Text(master=frame2, height=2, width=30)
in2 = tk.Text(master=frame4, height=2, width=30)
in1.pack()
in2.pack()



b1 = tk.Button(master=frame4, text='Enter', width=15,bg='Green',command=lambda: output()).pack() # button added
b2 = tk.Button(master=frame4, text='Close', width=15,command=lambda: quit(window)).pack() # button added


frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

window.mainloop()

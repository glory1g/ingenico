'''
                This Script is used to check connectivity to websites
                
                USAGE : python pingTest.py file.json
'''
import sys 
import json
import requests

WebsiteUrls=sys.argv[1]

with open(WebsiteUrls,'r') as json_file:  #Using Comprehension 
        data=json.load(json_file)
        for element in data['checks']['ping']: #Fetching URLS
                try:
                        
                        website="https://"+str(data['checks']['ping'][element]).split(":")[0] #Clearing Data to perfom the request
                        response=requests.get(website)

                        if (response.status_code == 200):  #if the HTTP Status flag == 200, the webserver responsed to our request
                                
                                print("[+]{}".format(website))
                        
                except requests.exceptions.RequestException as exeption:
                        #a problem happened, like failure to reach the webServer
                        print("[-]{}".format(website))





    



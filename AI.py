#imports
import requests                                             
import json
import numpy as np




def TempDataPrinter(api):
    data = requests.get(api)
    text = json.dumps(data.json(), sort_keys=True, indent = 4)
    print(text)
    
#gets the api using the address saved in text file
def apiGetter():
    with open("apiAIAddress.txt","r") as file:
        address =  file.read()
    return address

#puts data from api into object
def DataCreator(api):
    data = requests.get(api)
    text = json.dumps(data.json(), sort_keys=True, indent = 4)
    return json.loads(text)



def DataToVectors(api):
    listOfVectors = []
    for key in data['hourly']:
        if key != 'time':
            tempList = data['hourly'][key]
            tempVector = np.array(tempList[9:18])
            listOfVectors.append([key,tempVector])
            print([key,tempVector])
        
    


api = apiGetter()
data = DataCreator(api)
TempDataPrinter(api)
DataToVectors(api)

print(len(data['hourly']["apparent_temperature"]))
print(int(data['hourly']["time"][0][11:13]) in range(-1,1))


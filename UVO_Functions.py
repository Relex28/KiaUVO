import requests
import string
import json

headers = {'Content-type': 'application/json;charset=UTF-8',
           'Authorization' : 'Bearer TOKEN-HERE',
           'Cookie' : 'COOKIE-HERE',
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'ccsp-application-id' : 'APP-ID-HERE',
           'ccsp-device-id' : 'DEVICE-ID-HERE',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}


# Send request
UvoProfileRequest = requests.get('https://prd.eu-ccapi.kia.com:8080/api/v1/spa/vehicles/VERHICLE-CODE-HERE/profile', headers=headers)

#Needed for http code error's
UvoProfileRequest.raise_for_status()

# Hier moet je de cookie nog vandaan halen voor de PIN Call
#print contents
NewCookie = UvoProfileRequest.cookies.values()
test = ''.join(NewCookie)
print(test)
#--------------------------------------------------------------

HeadersPinRequest = {'Content-type': 'application/json;charset=UTF-8',
           'Authorization' : 'Bearer BEARER-TOKEN-HERE',
           'Cookie' : 'TS012b00dd=' +test,
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}

print(HeadersPinRequest)
# Send request
PinData = '{"pin":"5027","deviceId":"DEVICE-ID-HERE"}'

UvoPinRequest = requests.put('https://prd.eu-ccapi.kia.com:8080/api/v1/user/pin', data=PinData, headers=HeadersPinRequest)

UvoPinRequest.raise_for_status()
print(UvoPinRequest.content)

ResponsDataPin = UvoPinRequest.json()
ResponsDataPinHeader = ''.join(ResponsDataPin)


#--------------------------------------------------------------

HeadersTempRequest = {'Content-type': 'application/json;charset=UTF-8',
           'Authorization' : 'Bearer '+ResponsDataPinHeader,
           'Cookie' : 'TS012b00dd='+test,
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'ccsp-application-id' : 'APP-ID-HERE',
           'ccsp-device-id' : 'DEVICE-ID-HERE',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}

Tempdata = '{"tempCode" : "06H","hvacType" : 1,"deviceId" : "DEVICE-ID-HERE","options" : {"defrost" : true, "heating1" : 0 }, "unit" : "C", "action" : "start"}'

UvoTempRequest = requests.post('https://prd.eu-ccapi.kia.com:8080/api/v2/spa/vehicles/VERHICLE-CODE-HERE/control/temperature', data=Tempdata, headers=HeadersTempRequest)

UvoTempRequest.raise_for_status()
print(UvoTempRequest.content)


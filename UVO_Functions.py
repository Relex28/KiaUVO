import requests
import string
import json

headers = {'Content-type': 'application/json;charset=UTF-8',
           'Authorization' : 'Bearer Bearer-ID',
           'Cookie' : 'TS012b00dd=TS_COOKIE',
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'ccsp-application-id' : 'APP_ID',
           'ccsp-device-id' : 'DEVICE_ID',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}


# Send request
UvoProfileRequest = requests.get('https://prd.eu-ccapi.kia.com:8080/api/v1/spa/vehicles/VERHICLES_ID/profile', headers=headers)
print(UvoProfileRequest.headers)
#Needed for http code error's
UvoProfileRequest.raise_for_status()


#print contents
NewCookie = UvoProfileRequest.cookies.values()
TsCookie = ''.join(NewCookie)

#--------------------------------------------------------------

HeadersPinRequest = {'Content-type': 'application/json;charset=UTF-8',
           'Authorization' : 'Bearer Bearer-ID',
           'Cookie' : 'TS012b00dd=' +TsCookie,
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}

# Send request
PinData = '{"pin":"PIN-HERE","deviceId":"DEVICE_ID"}'

UvoPinRequest = requests.put('https://prd.eu-ccapi.kia.com:8080/api/v1/user/pin', data=PinData, headers=HeadersPinRequest)

UvoPinRequest.raise_for_status()
ControlTokenVar = UvoPinRequest.json()
ControlToken = ({ControlTokenVar['controlToken']})
ControlToken = ''.join(ControlToken)
#--------------------------------------------------------------

HeadersTempRequest = {'Content-type': 'application/json;charset=UTF-8',
           'Authorization' : 'Bearer '+ControlToken,
           'Cookie' : 'TS012b00dd='+TsCookie,
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'ccsp-application-id' : 'APP_ID',
           'ccsp-device-id' : 'DEVICE_ID',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}

Tempdata = '{"tempCode" : "06H","hvacType" : 1,"deviceId" : "0a7eab9b-17d0-4e0c-80b0-34f41b081a3a","options" : {"defrost" : true, "heating1" : 0 }, "unit" : "C", "action" : "start"}'

UvoTempRequest = requests.post('https://prd.eu-ccapi.kia.com:8080/api/v2/spa/vehicles/VEHICLE_ID/control/temperature', data=Tempdata, headers=HeadersTempRequest)

UvoTempRequest.raise_for_status()
print(UvoTempRequest.content)


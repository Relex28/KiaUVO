import requests
import json
import xml

cookies = {'account': 'COOKIE-HERE'}

headers = {
    'User-Agent': 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)',
    'Accept': '*/*',
    'Accept-Language': 'nl-NL;q=1, en-NL;q=0.9',
    'ccsp-application-id': 'APP-ID-HERE',
    'ccsp-service-id': 'SERVICE-ID-HERE',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'If-None-Match': 'NONMATCH-ID-HERE"',
    'Origin': 'https://prd.eu-ccapi.kia.com:8080',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


RegisterData = '{"pushType" : "APNS","pushRegId" : "PUSHREG-ID-HERE","uuid" : "UUID-HERE"}'

RegisterPost = requests.post('https://prd.eu-ccapi.kia.com:8080/api/v1/spa/notifications/register', headers=headers, cookies=cookies, data=RegisterData)

RegisterPost.raise_for_status()
tester = RegisterPost.json()

DeviceId = ({tester['resMsg']['deviceId']})
MsgId = ({tester['msgId']})


OautCallGet = requests.get('https://prd.eu-ccapi.kia.com:8080/api/v1/user/oauth2/authorize?response_type=code&client_id=SERVICE-ID-HERE&redirect_uri=https://prd.eu-ccapi.kia.com:8080/api/v1/user/oauth2/redirect&state=test&lang=en', cookies=cookies)
OautCallGet.raise_for_status()
# print(OautCallGet.text)

AuthorizeGet = requests.get('https://prd.eu-ccapi.kia.com:8080/web/v1/user/authorize?lang=en&cache=reset', cookies=cookies)

AuthorizeGet.raise_for_status()
# print(AuthorizeGet.text)

NewSessionCookie = AuthorizeGet.cookies.values()
SignInCookie = ''.join(NewSessionCookie)
print(SignInCookie)

HeadersSignInRequest = {'Content-type': 'application/json;charset=UTF-8',
           'Cookie' : 'TS012b00dd='+SignInCookie,
           'Accept-Encoding' : 'br,deflate,gzip',
           'Accept-Language' : 'nl-NL;q=1, en-NL;q=0.9',
           'User-Agent' : 'UVO_REL/1.5.1 (iPhone; iOS 14.0; Scale/3.00)'}

SignInData= '{"email":"EMAIL-HERE","password":"PASSWORD-HERE"}'

SignInPost = requests.post('https://prd.eu-ccapi.kia.com:8080/api/v1/user/signin', headers=HeadersSignInRequest, data=SignInData)

SignInPost.raise_for_status()
print(SignInPost.text)

import json
import sys

import requests

# def refresh():


  # url = "https://api.xero.com/api.xro/2.0/Invoices"
from BigQuery import BQcall

payload = {}
headers = {
  'xero-tenant-id': '169b425b-812a-45cc-84af-6c42a32aba19',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFDQUY4RTY2NzcyRDZEQzAyOEQ2NzI2RkQwMjYxNTgxNTcwRUZDMTkiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJISy1PWm5jdGJjQW8xbkp2MENZVmdWY09fQmsifQ.eyJuYmYiOjE1OTI3MzExNDQsImV4cCI6MTU5MjczMjk0NCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS54ZXJvLmNvbSIsImF1ZCI6Imh0dHBzOi8vaWRlbnRpdHkueGVyby5jb20vcmVzb3VyY2VzIiwiY2xpZW50X2lkIjoiQjgyNjg3MDA2RURGNDdBMTgyNjdGMEY2MTM3QjFCRkMiLCJzdWIiOiI2NGRmYjYzMzQzMmY1MmVjYmUxMzE1ZWRlY2EyMzAwOCIsImF1dGhfdGltZSI6MTU5MjcyMTQ2MywieGVyb191c2VyaWQiOiJjZjlmYmQ3Yy0zYmZlLTQ2NDgtYWVlZi02ZTBiNjA2M2Q5MDEiLCJnbG9iYWxfc2Vzc2lvbl9pZCI6IjRlZGI5ZTczMzZkNTRjNzJiYmQ4NTZjYzY4MzNjNmEwIiwianRpIjoiMWMyNjM5NTBiMjU4OTA4MWNhOGIwNjQ2NWJhMDhhMjciLCJhdXRoZW50aWNhdGlvbl9ldmVudF9pZCI6IjY1ZDcxNjIxLWNiZDUtNGJiNi1hMTM1LWM1ZTNkMjI4Yzg4ZCIsInNjb3BlIjpbImFjY291bnRpbmcudHJhbnNhY3Rpb25zIiwib2ZmbGluZV9hY2Nlc3MiXX0.D0N4iKxwTEtPngATr8Tyd3d7mBzogC3puaya_ortG0OGGCTEoeas7VjMmQ6tLEcUkbMplQVQ0brnebFC_q9lNUKDK-zAz94GivIAKcR-4pBgo9pSVN12EXZOS-uPA8--zpP70hkchlKemWAWrVdN7eFG-oMXu0jaf9hFJEe3HtSUEt1HoHqy9lfT6oH67XmC0SzvSwoGIP5mr5mPtTNLROr1D7US4HcY90R6MhFflpWhhYF8lPyCqGmncmVIf7o8d3uPnqcAOaxhB7BRBvapp9OHKnB-3M9yTNdJJLYGZ8bz1hTFECPLqcMAAhBlSmlD7UDlAm_SgEx889Lh9jvHOw',
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  # 'Cookie': '_gcl_au=1.1.20616791.1592678393; _fbp=fb.1.1592678394096.569490090; _ga=GA1.2.434807873.1592678418; _gid=GA1.2.992569261.1592678418; bm_sz=814D235FFFBEEBFD82DA9FC2F7591311~YAAQHp4QAjqPJadyAQAATZqY1QgA2aeEUmQbxT451NjmhruVra7Qh8v+XK1+WUaRSU/mGdYOOX63p1xiYgPoXmWH7AAC5iSPIepwor8pu4JFJrx41oJ0Vl5MmmY0g34u5K9e4pmJXMcjWVdDQ81PrRLI6B+PZXPGIPLqW06DaGK7XT/y11Rb88ZKaommmQ==; _abck=CA90924056464C02EA207551AF666E3C~-1~YAAQd2t7XIq0BrdyAQAAYved1QSNYuKu0qELvHwvi9w/uU5veYvr71YdLwCw62gWge6128SlV3UQI/F1AxsskkAWQLU/EEkiITm5oaOe2RoCxB/zboPGwO7fm6TiDS+5tJYQDpC+osvm3dHhpfJR/5aBwMMt5UU+MjemuGB78OJt/FrvhPqtogyP0VAbjN6ayti4X3cuqDQ2nn4NVRZlk46NRxtUEMT7JWWKhTwKnJ4njVIC7iAJV2s8NNeQLIO0MmIToilwnl/dpXaPCgDzfCzv+X9F/JN+85oAGroR2yfvNmR1kWU2shYJxVahNM52N9rbgUcl~-1~-1~-1; ak_bmsc=8BF9D91BFFBC9AA874CE1CC119AB97950214841F6E280000A525EF5E17CF3D68~plI/1ZELMJrfWRGVWR22ta268l1et2MJIly9IvAH++1JUSW8l2pvHwKDbs4OzMB2agBdlrcWJ3IHy4XUouZw984U9F9H1F5kD0uDSTQPvIzV7shAqqfFLEXM4MWPMTfp8vgd3vCwK2OSk1sXomCtLctg31uSa5BaKsPS91kpeoA7W+h5BOtfQUKvKJD1PH+dTo24Czo3JUrgvpDIvd+FWD24XC4U71lNb2bB8ErzCBvb8=; bm_sv=1921B079DD062D0ECE1E39D31FD28DC0~Uc/lxG+tlb2m86Iv0yEcoFdbDfWCaY1V12J1n2+18UsJ4yh+SWaSBBOM95Y3MwHkhQdNXDys32oYEwafUb6cJx6Ub9AV3R0ldajsZgxPD176U7x+oXU/Xiu7NJwDy064CxwAFduHmbII6yAVjJ8O+A=='
}
class XeroApi:
  def __init__(self,access_token=None,refresh_token=None):
    if access_token==refresh_token:
      return "Access or Refresh token is invalid"
    self.access_token=access_token
    self.refresh_token=refresh_token


  def call_xero(self,url,method,headers,payload):
    response = requests.request(method, url, headers=headers, data=payload)
    if response.status_code ==200:
      return response
    print(response.status_code)
    print(response.text.encode('utf8'))
    if response.status_code == 401:
      refresh_response=self.call_refresh_token()
      if refresh_response.status_code == 200:
        print('resfreshing...........')
        self.access_token = refresh_response.json()['access_token']
        self.refresh_token = refresh_response.json()['refresh_token']
      else:
        print("REfresh Token not posibel")
        sys.exit(0)
      return self.call_xero(url,method,headers,payload)


  CLIENT_ID = "B82687006EDF47A18267F0F6137B1BFC"
  CLIENT_SECRET = "1yGzsRahlEpzLHDat9mFNKHx9rLZpgz-vz7D3g_dN7zxfoT3"
  def call_refresh_token(self):
    refresh_token_url="https://identity.xero.com/connect/token?="
    payload = {'grant_type': 'refresh_token',
               'refresh_token': f'{self.refresh_token}',
               'client_id': f'{XeroApi.CLIENT_ID}',
               'client_secret': f'{XeroApi.CLIENT_SECRET}'}
    headers = {
      'grant_type': 'refresh_token',
      'Content-Type': 'application/json',}
    print(headers,payload)
    res=self.call_xero(refresh_token_url,"POST",headers,payload)
    # print(res.status_code)
    return res

  def invoice(self,xero_tenant_id="169b425b-812a-45cc-84af-6c42a32aba19"):
    url = "https://api.xero.com/api.xro/2.0/Invoices"
    headers = {
      'xero-tenant-id': f'{xero_tenant_id}',
      'Authorization': f'Bearer {self.access_token}',
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      # 'Cookie': '_gcl_au=1.1.20616791.1592678393; _fbp=fb.1.1592678394096.569490090; _ga=GA1.2.434807873.1592678418; _gid=GA1.2.992569261.1592678418; bm_sz=814D235FFFBEEBFD82DA9FC2F7591311~YAAQHp4QAjqPJadyAQAATZqY1QgA2aeEUmQbxT451NjmhruVra7Qh8v+XK1+WUaRSU/mGdYOOX63p1xiYgPoXmWH7AAC5iSPIepwor8pu4JFJrx41oJ0Vl5MmmY0g34u5K9e4pmJXMcjWVdDQ81PrRLI6B+PZXPGIPLqW06DaGK7XT/y11Rb88ZKaommmQ==; _abck=CA90924056464C02EA207551AF666E3C~-1~YAAQd2t7XIq0BrdyAQAAYved1QSNYuKu0qELvHwvi9w/uU5veYvr71YdLwCw62gWge6128SlV3UQI/F1AxsskkAWQLU/EEkiITm5oaOe2RoCxB/zboPGwO7fm6TiDS+5tJYQDpC+osvm3dHhpfJR/5aBwMMt5UU+MjemuGB78OJt/FrvhPqtogyP0VAbjN6ayti4X3cuqDQ2nn4NVRZlk46NRxtUEMT7JWWKhTwKnJ4njVIC7iAJV2s8NNeQLIO0MmIToilwnl/dpXaPCgDzfCzv+X9F/JN+85oAGroR2yfvNmR1kWU2shYJxVahNM52N9rbgUcl~-1~-1~-1; ak_bmsc=8BF9D91BFFBC9AA874CE1CC119AB97950214841F6E280000A525EF5E17CF3D68~plI/1ZELMJrfWRGVWR22ta268l1et2MJIly9IvAH++1JUSW8l2pvHwKDbs4OzMB2agBdlrcWJ3IHy4XUouZw984U9F9H1F5kD0uDSTQPvIzV7shAqqfFLEXM4MWPMTfp8vgd3vCwK2OSk1sXomCtLctg31uSa5BaKsPS91kpeoA7W+h5BOtfQUKvKJD1PH+dTo24Czo3JUrgvpDIvd+FWD24XC4U71lNb2bB8ErzCBvb8=; bm_sv=1921B079DD062D0ECE1E39D31FD28DC0~Uc/lxG+tlb2m86Iv0yEcoFdbDfWCaY1V12J1n2+18UsJ4yh+SWaSBBOM95Y3MwHkhQdNXDys32oYEwafUb6cJx6Ub9AV3R0ldajsZgxPD176U7x+oXU/Xiu7NJwDy064CxwAFduHmbII6yAVjJ8O+A=='
    }
    res=self.call_xero(url,'GET',headers,{})
    print(res.status_code)
    return res.json().get('Invoices',{})

  def payments(self, xero_tenant_id="169b425b-812a-45cc-84af-6c42a32aba19"):
    url = "https://api.xero.com/api.xro/2.0/Payments"
    headers = {
      'xero-tenant-id': f'{xero_tenant_id}',
      'Authorization': f'Bearer {self.access_token}',
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      # 'Cookie': '_gcl_au=1.1.20616791.1592678393; _fbp=fb.1.1592678394096.569490090; _ga=GA1.2.434807873.1592678418; _gid=GA1.2.992569261.1592678418; bm_sz=814D235FFFBEEBFD82DA9FC2F7591311~YAAQHp4QAjqPJadyAQAATZqY1QgA2aeEUmQbxT451NjmhruVra7Qh8v+XK1+WUaRSU/mGdYOOX63p1xiYgPoXmWH7AAC5iSPIepwor8pu4JFJrx41oJ0Vl5MmmY0g34u5K9e4pmJXMcjWVdDQ81PrRLI6B+PZXPGIPLqW06DaGK7XT/y11Rb88ZKaommmQ==; _abck=CA90924056464C02EA207551AF666E3C~-1~YAAQd2t7XIq0BrdyAQAAYved1QSNYuKu0qELvHwvi9w/uU5veYvr71YdLwCw62gWge6128SlV3UQI/F1AxsskkAWQLU/EEkiITm5oaOe2RoCxB/zboPGwO7fm6TiDS+5tJYQDpC+osvm3dHhpfJR/5aBwMMt5UU+MjemuGB78OJt/FrvhPqtogyP0VAbjN6ayti4X3cuqDQ2nn4NVRZlk46NRxtUEMT7JWWKhTwKnJ4njVIC7iAJV2s8NNeQLIO0MmIToilwnl/dpXaPCgDzfCzv+X9F/JN+85oAGroR2yfvNmR1kWU2shYJxVahNM52N9rbgUcl~-1~-1~-1; ak_bmsc=8BF9D91BFFBC9AA874CE1CC119AB97950214841F6E280000A525EF5E17CF3D68~plI/1ZELMJrfWRGVWR22ta268l1et2MJIly9IvAH++1JUSW8l2pvHwKDbs4OzMB2agBdlrcWJ3IHy4XUouZw984U9F9H1F5kD0uDSTQPvIzV7shAqqfFLEXM4MWPMTfp8vgd3vCwK2OSk1sXomCtLctg31uSa5BaKsPS91kpeoA7W+h5BOtfQUKvKJD1PH+dTo24Czo3JUrgvpDIvd+FWD24XC4U71lNb2bB8ErzCBvb8=; bm_sv=1921B079DD062D0ECE1E39D31FD28DC0~Uc/lxG+tlb2m86Iv0yEcoFdbDfWCaY1V12J1n2+18UsJ4yh+SWaSBBOM95Y3MwHkhQdNXDys32oYEwafUb6cJx6Ub9AV3R0ldajsZgxPD176U7x+oXU/Xiu7NJwDy064CxwAFduHmbII6yAVjJ8O+A=='
    }
    res = self.call_xero(url, 'GET', headers, {})
    print(res.status_code)
    return res.json()['Payments']

  def dump_pay(self):
    print('Payments',self.payments())
    BQcall(self.payments(),"Payments")




if __name__ == "__main__":
  access_token ='eyJhbGciOiJSUzI1NiIsImtpZCI6IjFDQUY4RTY2NzcyRDZEQzAyOEQ2NzI2RkQwMjYxNTgxNTcwRUZDMTkiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJISy1PWm5jdGJjQW8xbkp2MENZVmdWY09fQmsifQ.eyJuYmYiOjE1OTI3NTgwNjYsImV4cCI6MTU5Mjc1OTg2NiwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS54ZXJvLmNvbSIsImF1ZCI6Imh0dHBzOi8vaWRlbnRpdHkueGVyby5jb20vcmVzb3VyY2VzIiwiY2xpZW50X2lkIjoiQjgyNjg3MDA2RURGNDdBMTgyNjdGMEY2MTM3QjFCRkMiLCJzdWIiOiI2NGRmYjYzMzQzMmY1MmVjYmUxMzE1ZWRlY2EyMzAwOCIsImF1dGhfdGltZSI6MTU5MjczNzk5NiwieGVyb191c2VyaWQiOiJjZjlmYmQ3Yy0zYmZlLTQ2NDgtYWVlZi02ZTBiNjA2M2Q5MDEiLCJnbG9iYWxfc2Vzc2lvbl9pZCI6ImY3N2QwMTBkYzEwODQzODRhYjAzNWZlNWNlMTcyNjQ0IiwianRpIjoiOTA2YjQ3OTYzMjI4ODJkMjA3NjY1OTUxMTRkOWQxMDciLCJhdXRoZW50aWNhdGlvbl9ldmVudF9pZCI6ImFiNWNhZDEwLTJlMDktNDU3MC04MzE1LTQyZDYxOTE5NjQxZCIsInNjb3BlIjpbImFjY291bnRpbmcudHJhbnNhY3Rpb25zIiwib2ZmbGluZV9hY2Nlc3MiXX0.PDGRudEWUQRAb3_d-aizR1eJ0Cnxwos8rVuXTIZovFP-ed9eD36hOjqoa5sU60dqNiRKcxtDHukzkW8LKBXJOY84aEaQ-mEegRAbmd1PPn8QyvaDxAcTjMdLqhazcR4WMt8J5jgyZdeusQbJaynFvQDzy65EpW5LF33G40mLnlXyi9ACzbnz4h53EFiti2fgu8GCySJCf_1tPeBRTV2XgxTa5HT0PlJefodLQTlBFLvAyn-9Ft1eBlqJPK3PgJ9OElBqkNZnNbRjmcJMBIfcykO3i_S-kZV_YJxQ6wfJP_8gqC7O0Wp8YdcG0aOSXFd5kQqB3JWGfPmAJPYQMn-a1g'
  refresh_token = 'da880c536b57846ac296f97a9852d70b92d5064c684b990b152896a2fd8ac866'
  xero_ins = XeroApi(access_token,refresh_token)
  #response=xero_ins.invoice()
  response = xero_ins.dump_pay()


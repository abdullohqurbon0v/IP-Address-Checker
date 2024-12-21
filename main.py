import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip):
     try:
          response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
          print(response)

          data = {
               '[IP]': response.get('query'),
               '[Int Prov]': response.get('isp'),
               '[Org]': response.get('org'),
               '[Country]': response.get('country'),
               '[Region Name]': response.get('regionName'),
               '[City]': response.get('city'),
               '[Zip]': response.get('zip'),
               '[Lat]': response.get('lat'),
               '[Lon]': response.get('lon')
          }

          for k,y in data.items():
               print(f"{k}, {y}")

          area = folium.Map(location=[response.get('lat'), response.get('lon')])
          area.save(f"{response.get('query')}_{response.get('city')}.html")

     except requests.exceptions.ConnectionError:
          print("Pleace check your connection")

def main():
     preview_text = Figlet(font='slant')
     print(preview_text.renderText('IP INFO'))
     ip = input("Enter IP address: ")
     get_info_by_ip(ip=ip)

if __name__ == '__main__':
     main()
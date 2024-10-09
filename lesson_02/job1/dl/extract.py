import requests
import os
import sys
if __name__ == '__main__':
    current_dir=os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(os.path.join(current_dir,'..','..')))
    from env.env_variables import get_env_variable
else:
    from env.env_variables import get_env_variable
def request(period,page):
    custom_ca_cert_path = r'C:\Users\iuar0081\Desktop\Power BI APP\JiraCoonection\rbua 1.pem'
    AUTH_TOKEN=get_env_variable('AUTH_TOKEN')
    response = requests.get(
            url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
            params={'date': period, 'page': page},
            headers={'Authorization': AUTH_TOKEN},
            verify=custom_ca_cert_path
        )
    return response
def get_extract(period,page):
    return [period,page,request(period,page).json()]
def main ():
    print("Response status code:", request('2022-08-09','2').status_code)
    print("Response JSON", get_extract('2022-08-09','2'))

if __name__ == '__main__':
    main()
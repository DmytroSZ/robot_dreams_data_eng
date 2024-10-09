import os 
from dotenv import load_dotenv

load_dotenv()
variables=["BASE_DIR","AUTH_TOKEN"]
for v in variables:
     globals()[v]=os.environ.get(v)
     if not globals()[v]:
        print(v +" environment variable must be set in .env file")
        exit(1)
def get_env_variable(name):
    return globals()[name]

def main():
    for v in variables:
        print(v + ": " + globals()[v])
if __name__ == '__main__':
     main()
     


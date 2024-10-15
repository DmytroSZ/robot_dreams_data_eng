import json
import os
import sys

if __name__ == '__main__':
    current_dir=os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(os.path.join(current_dir,'..','..')))
    from env.env_variables import get_env_variable
else:
    from env.env_variables import get_env_variable
    
BASE_DIR=get_env_variable('BASE_DIR')
def get_extract(period,page):

    FILE_DIR=os.path.join(BASE_DIR, "raw", "sales",period,period+"_"+page+".json") 
    if not os.path.exists(FILE_DIR):
        print(FILE_DIR +" - file not exist")
        exit(1)
    with open(FILE_DIR, 'rb') as f:
        data = json.load(f)
    return [period,page,data]


def main ():
    print(get_extract('2022-08-09','2'))

if __name__ == '__main__':
    main()
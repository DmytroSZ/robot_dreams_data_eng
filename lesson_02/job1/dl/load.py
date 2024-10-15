import os
import sys
import json
if __name__ == '__main__':
    current_dir=os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(os.path.join(current_dir,'..','..')))
    from env.env_variables import get_env_variable
else:
    from env.env_variables import get_env_variable

BASE_DIR=get_env_variable('BASE_DIR')
RAW_DIR=os.path.join(BASE_DIR, "raw", "sales")
def load_raw(transformed_data): 
    directory= RAW_DIR+"\\"+transformed_data[0]
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory,transformed_data[0]+"_"+transformed_data[1]+".json"), 'w') as f:
        json.dump(transformed_data[2], f)
def main ():
    print (RAW_DIR)

if __name__ == '__main__':
    main()
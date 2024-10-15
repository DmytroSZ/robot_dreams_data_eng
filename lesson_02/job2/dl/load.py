import os
import sys
from fastavro import writer
from jsonschema import validate
import json

if __name__ == '__main__':
    current_dir=os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(os.path.join(current_dir,'..','..')))
    from env.env_variables import get_env_variable
else:
    from env.env_variables import get_env_variable

BASE_DIR=get_env_variable('BASE_DIR')
STG_DIR=os.path.join(BASE_DIR, "stg", "sales")

schema={
    "type":"record",
    "name":"Transaction",
    "fields": [
        {"name":"client","type":"string"},
        {"name":"purchase_date","type":"string"},
        {"name":"product","type":"string"},
        {"name":"price","type":"float"}
    ]
}

def load_stg(transformed_data): 
    directory= STG_DIR+"\\"+transformed_data[0]
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory,transformed_data[0]+"_"+transformed_data[1]+".avro"), 'wb') as f_out:
        writer(f_out, schema, transformed_data[2])
        
def main ():
    print (STG_DIR)

if __name__ == '__main__':
    main()
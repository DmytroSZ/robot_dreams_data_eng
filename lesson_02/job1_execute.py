from job1.dl.extract import get_extract
from job1.bl.transform import get_transform_result
from job1.dl.load import load_raw

def main():
    period='2022-08-09'
    page='4'
    extract=get_extract(period,page)
    transform=get_transform_result(extract)
    load_raw(transform)

if __name__ == '__main__':
    main()
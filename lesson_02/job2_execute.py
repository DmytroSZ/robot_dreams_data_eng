from job2.dl.extract import get_extract
from job2.bl.transform import get_transform_result
from job2.dl.load import load_stg

def main():
    period='2022-08-09'
    page='4'
    extract=get_extract(period,page)
    transform=get_transform_result(extract)
    load_stg(transform)


if __name__ == '__main__':
    main()
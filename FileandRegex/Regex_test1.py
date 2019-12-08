import csv
import re


def readfile(file_name):
    try:
        compiled_ip_pattern = re.compile("^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$")
        compiled_date_pattern = re.compile('^\d{1,2}.\d{1,2}.\d{4}$')
        csvfile = open(file_name, "r+")
        csv_read = csv.DictReader(csvfile)
        row1 = []
        for row in csv_read:
            print('Original Dict:', row)
            dict1 = {}
            for (k, v) in row.items():
                if k == 'MANTNR':
                    v1 = re.sub('[^a-zA-Z\d%()]*', '', v)
                    dict1.update({k: v1})
                elif k == 'PSTTR':
                    count_PSTTR = v.count('.')
                    row.update({"PSTTR": str(count_PSTTR)})
                    dict1.update({k: v})
                    dict1.update({"Count_PSTTR": str(count_PSTTR)})
                elif k == 'PEDTR':
                    month_search = compiled_date_pattern.search(v)
                    dict1.update({k: v})
                    month = month_search.group().split('.')[1]
                    dict1.update({'Month': month})
                elif k == 'PERTR':
                    year_search = compiled_date_pattern.search(v)
                    dict1.update({k: v})
                    year = year_search.group().split('.')[2]
                    dict1.update({'year': year})
                elif k == 'IP':
                    dict1.update({k: v})
                    ipValid = compiled_ip_pattern.match(v)
                    if (ipValid):
                        dict1.update({'ip valid': 'Yes'})
                    else:
                        dict1.update({'ip valid': 'No'})
                else:
                    dict1.update({k: v})
            print("Modified Dict:", dict1)
            row1.append(dict1)
        return row1
    except IOError:
        print('There is Error while reading File')
    finally:
        csvfile.close()


def writefile(file_name,row1):
    try:
        columns = row1[0].keys()
        csv_columns = columns
        csv_new_file = open(file_name, 'w')
        writer = csv.DictWriter(csv_new_file, fieldnames=csv_columns)
        writer.writeheader()
        for new_data in row1:
            writer.writerow(new_data)
    except IOError:
        print('There is Error while writing to File')
    finally:
        csv_new_file.close()


newlist = readfile('TestFile1.csv')
writefile('Testfile2.csv',newlist)

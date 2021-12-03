from __future__ import print_function
import os
import json
import sys


def read_prov(fn):
    res = {}
    with open(fn, 'r') as fin:
        for line in fin.readlines():
            line = line.decode('gbk', errors='ignore')
            arr = line.split(u'\t')
            res[arr[2]] = arr[1]
    return res


def skip(arr):
    if arr[6].find(u'公司企业') >= 0 or arr[6].find(u'小区') >= 0 or arr[6].find(u'住宅区') >= 0:
        return False
    return True


if __name__ == '__main__':
    prov_config = read_prov(sys.argv[1])
    data_file = sys.argv[2]
    with open(data_file, 'r') as fin:
        line = fin.readline()
        while line:
            line = line.decode('gbk', errors='ignore')
            arr = line.split(u'\t')
            if skip(arr):
                line = fin.readline()
                continue
            admin_info = json.loads(arr[7])
            admin_code = admin_info['city_id']
            prov_name = prov_config[admin_code[0:2]]
            address = u'{}{}{}{}'.format(prov_name, arr[4], arr[5], arr[1])
            xy = arr[3]
            print(u'{}\t{}'.format(address, xy).encode('gbk'))


import os
import json
import pathlib
import datetime

import boto3

all_users = pathlib.Path(pathlib.Path(
    __file__).parent, 'users.json')
all_assets = pathlib.Path(pathlib.Path(
    __file__).parent, 'assets.json')
all_drawings = pathlib.Path(pathlib.Path(
    __file__).parent, 'drawings.json')

out_folder = pathlib.Path(pathlib.Path(
    __file__).parent, 'images')


def load(path):
    with open(path, "r") as f:
        return json.load(f)


users_arr = load(all_users)
users = set()
for user in users_arr:
    if user['email'].endswith('beamup.ai') is False:
        users.add(user['_id']['$oid'])

drawings_arr = load(all_drawings)
drawings = dict()
one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)

for drawing in drawings_arr:
    if drawing['user']['$oid'] in users:
        nums = [int(n) for n in drawing['createdAt']
                ['$date'].split('T')[0].split('-')]
        drawing_date = datetime.datetime(nums[0], nums[1], nums[2])
        if drawing_date > one_year_ago:
            extension = drawing['originalName'].split('.')[-1]
            if extension != 'site':
                drawings[drawing['_id']['$oid']] = drawing
                drawings[drawing['_id']['$oid']]['type'] = extension

assets_arr = load(all_assets)

for asset in assets_arr:
    if asset['drawing']['$oid'] in drawings:
        if asset['type'] in ['png', 'jpg', 'jpeg']:
            drawings[asset['drawing']['$oid']]['asset'] = asset
        drawings[asset['drawing']['$oid']]['test'] = 'this is a test'

times = []
bucket_paths = []
s3 = boto3.client('s3')


should_save = False
for drawing in drawings:
    d = drawings[drawing]
    if d['type'] == 'png' or d['type'] == 'jpg' or d['type'] == 'jpeg':
        if d['asset']:
            bucket_paths.append(d['asset']['bucketPath'])
            try:
                if d['asset']['fileName'] == 'OG_Neu_2021_05_05.png':
                    should_save = True
                if should_save:
                    s3.download_file('prod.user.data',
                                     d['asset']['bucketPath'], str(out_folder) + '/' + d['asset']['fileName'])
                    print("downloaded file successfully")
            except:
                print("An exception occurred")

print("images in last year", len(bucket_paths))

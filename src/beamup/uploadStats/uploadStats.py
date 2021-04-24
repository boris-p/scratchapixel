import os
import json
import pathlib
import datetime

all_users = pathlib.Path(pathlib.Path(__file__).parent, 'users.json')
all_assets = pathlib.Path(pathlib.Path(__file__).parent, 'assets.json')
all_drawings = pathlib.Path(pathlib.Path(__file__).parent, 'drawings.json')

writePath = pathlib.Path(pathlib.Path(__file__).parent, 'res.txt')


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
three_months_ago = datetime.datetime.now() - datetime.timedelta(days=91)
drawings_types = dict()

for drawing in drawings_arr:
    if drawing['user']['$oid'] in users:
        nums = [int(n) for n in drawing['createdAt']
                ['$date'].split('T')[0].split('-')]
        drawing_date = datetime.datetime(nums[0], nums[1], nums[2])
        if drawing_date > three_months_ago:
            extension = drawing['originalName'].split('.')[-1]
            if extension != 'site':
                drawings[drawing['_id']['$oid']] = drawing
                drawings[drawing['_id']['$oid']]['type'] = extension
                drawings[drawing['_id']['$oid']]['assets'] = []
                if drawings_types.get(extension):
                    drawings_types[extension] += 1
                else:
                    drawings_types[extension] = 1

assets_arr = load(all_assets)

for asset in assets_arr:
    if asset['drawing']['$oid'] in drawings:
        drawings[asset['drawing']['$oid']]['assets'].append(asset)


def asset_by_type(drawing, type):
    assets = drawing['assets']
    for asset in assets:
        if asset['type'] == type:
            return asset
    return None


def create_date(asset, field):
    nums1 = [int(n) for n in asset[field]['$date'].split('T')[0].split('-')]
    nums2 = [int(n) for n in asset[field]['$date'].replace('Z', '').split('T')
             [1].split('.')[0].split(':')]
    year = nums1[0]
    month = nums1[1]
    day = nums1[2]

    hour = nums2[0]
    minute = nums2[1]
    second = nums2[2]

    d = datetime.datetime(year, month, day, hour, minute, second)
    return d


times = []
for drawing in drawings:
    d = drawings[drawing]
    if d['type'] == 'pdf' or d['type'] == 'dwg':
        # todo - measure pdf -> dwg
        dwg_asset = asset_by_type(d, 'dwg')
        dwg_json_asset = asset_by_type(d, 'dwg.json')
        underlay_asset = asset_by_type(d, 'underlay')
        wiring_asset = asset_by_type(d, 'wiring')

        if not dwg_asset or not dwg_json_asset or not underlay_asset or not wiring_asset:
            print(f"something went wrong in drawing {drawing}")
            continue

        dwg_created = create_date(dwg_asset, 'createdAt')
        dwg_json_created = create_date(dwg_json_asset, 'createdAt')
        generate_started = create_date(underlay_asset, 'createdAt')
        generate_finished = create_date(underlay_asset, 'updatedAt')
        wiring_created = create_date(wiring_asset, 'updatedAt')
        drawing_updated = create_date(d, 'updatedAt')

        dwg_to_json_time = (dwg_json_created - dwg_created).total_seconds()
        time_to_generate = (generate_started -
                            dwg_json_created).total_seconds()
        processing_time = (generate_finished -
                           generate_started).total_seconds()

        post_processing_time = (
            drawing_updated - generate_finished).total_seconds()

        drawing_minus_wiring = (
            drawing_updated - wiring_created).total_seconds()

        design_time = (
            drawing_updated - wiring_created).total_seconds()

        print("post_processing_time", post_processing_time)
        if post_processing_time > 1000880:
            print(d)
        # t = {
        #     'dwg_to_json_time': dwg_to_json_time,
        #     'time_to_generate': time_to_generate,
        #     'processing_time': processing_time,
        #     # 'post_processing_time': post_processing_time,
        # }
        times.append([dwg_to_json_time, time_to_generate,
                      processing_time, post_processing_time])
        # dwg_created = dwg_asset['createdAt']['$date']
        # dwg_json_created = dwg_json_asset['createdAt']['$date']
        # generate_started = underlay_asset['createdAt']['$date']
        # generate_finished = underlay_asset['updatedAt']['$date']
        # design_created = wiring_asset['createdAt']['$date']


print("users", len(users))
print("drawings", len(drawings))
print("drawings_types", drawings_types)


with open(writePath, "w") as f:
    # f.write(f'total number of users is {len(users)}\n')
    # f.write(f'total number of drawings is {len(drawings)}\n')
    # f.write(f'drawings_types {json.dumps(drawings_types)}\n')
    for t in times:
        f.write(','.join([str(i) for i in t]) + '\n')

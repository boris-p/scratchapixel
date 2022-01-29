__author__ = "Guy-BeamUP"
__version__ = "2021.06.15"

import Rhino as rh
import json
import operator
import copy


############################DOOR WARNING GENERATORS ###################################

def CheckDoorHasNumberOfAxis(_door_id, _values):
    door_data = GetNodeData(_door_id)
    if door_data["axis"] == None:
        msg = "Door has no axis"
        return CreateWarning("DOOR", _door_id, msg)
    if not len(door_data["axis"]) == _values["axisAmount"]:
        msg = "Door has " + str(len(door_data["axis"])) + " axes"
        return CreateWarning("DOOR", _door_id, msg, _level=1)
    return None


def CheckDoorLeadsOutside(_door_id, _values):
    rooms = GetRoomsFromDoor(_door_id)
    door_data = GetNodeData(_door_id)
    if -1 in rooms:
        msg = CATEGORY_STRINGS[door_data["category"]] + " leading outside"
        warn = CreateWarning("DOOR", _door_id, msg)
        return warn
    return None


def CheckDoorHasDifferentLevels(_door_id, _values):
    rooms = GetRoomsFromDoor(_door_id)
    door_data = GetNodeData(_door_id)
    if GetRoomSecurity(rooms[0]) != GetRoomSecurity(rooms[1]):
        msg = CATEGORY_STRINGS[door_data["category"]] + \
            " between different security levels"
        return CreateWarning("DOOR", _door_id, msg, _level=3)
    return None


def CheckDoorHasEqualLevels(_door_id, _values):
    rooms = GetRoomsFromDoor(_door_id)
    door_data = GetNodeData(_door_id)
    if GetRoomSecurity(rooms[0]) == GetRoomSecurity(rooms[1]):
        msg = CATEGORY_STRINGS[door_data["category"]] + \
            " between same security levels"
        return CreateWarning("DOOR", _door_id, msg, _level=1)
    return None


def CheckDoorIsInteriorDoor(_door_id, _values):
    rooms = GetRoomsFromDoor(_door_id)
    door_data = GetNodeData(_door_id)
    if not -1 in rooms:
        msg = CATEGORY_STRINGS[door_data["category"]] + " is interior door"
        return CreateWarning("DOOR", _door_id, msg, _level=1)
    return None


def CheckDoorSubtypeIsNot(_door_id, _values):
    door_data = GetNodeData(_door_id)
    if not door_data["subtype"] == _values["subtype"]:
        msg = CATEGORY_STRINGS[door_data["category"]] + \
            " is wrong door subtype"
        return CreateWarning("DOOR", _door_id, msg, _level=3)
    return None


def CheckDoorSubtype(_door_id, _values):
    door_data = GetNodeData(_door_id)
    if door_data["subtype"] == _values["illegalSubtype"]:
        msg = CATEGORY_STRINGS[door_data["category"]] + \
            " is wrong door subtype"
        return CreateWarning("DOOR", _door_id, msg, _level=3)
    else:
        return None


def CheckDoorLeadsToLevels(_door_id, _values):
    rooms = GetRoomsFromDoor(_door_id)
    door_data = GetNodeData(_door_id)
    levels = [GetRoomSecurity(room) for room in rooms]
    for level in levels:
        if level in _values["illegalLevels"]:
            msg = CATEGORY_STRINGS[door_data["category"]
                                   ] + " leads to security level "+str(level)
            return CreateWarning("DOOR", _door_id, msg, _level=3)
    return None


def CheckDoorDoesntLeadToLevel(_door_id, _values):
    rooms = GetRoomsFromDoor(_door_id)
    door_data = GetNodeData(_door_id)
    levels = [GetRoomSecurity(room) for room in rooms]

    if not _values["obligatoryLevel"] in levels:
        msg = CATEGORY_STRINGS[door_data["category"]] + \
            " does not lead to security level "+str(_values["obligatoryLevel"])
        return CreateWarning("DOOR", _door_id, msg)
    return None


def CheckDoorClosestDoorSubtypeIsNot(_door_id, _values):

    rooms = GetRoomsFromDoor(_door_id)
    door_list = GetDoorsFromDoor(_door_id)
    closest_index = GetClosestDoor(_door_id, door_list)
    if closest_index < 0:
        return None
    closest_door = GetNodeData(closest_index)
    if closest_door["subtype"] != _values["closestSubtype"]:
        msg = " Closest door subtype is not "+str(_values["closestSubtype"])
        return CreateWarning("DOOR", _door_id, msg)
    return None


####################### DOOR CATEGORY FUNCTIONS ##########################
def N(_door_id):
    warnings = [CheckDoorHasDifferentLevels,  CheckDoorLeadsOutside]
    values = {}
    return EvaluateWarnings(warnings, _door_id, values)


def E(_door_id):
    warnings = [CheckDoorSubtypeIsNot, CheckDoorIsInteriorDoor,
                CheckDoorLeadsToLevels, CheckDoorHasNumberOfAxis]
    values = {"subtype": "swing", "illegalLevels": [4, 5], "axisAmount": 1}
    return EvaluateWarnings(warnings, _door_id, values)


def T(_door_id):
    warnings = [CheckDoorSubtypeIsNot,
                CheckDoorLeadsOutside, CheckDoorLeadsToLevels]
    values = {"subtype": "turnstile", "illegalLevels": [3, 4, 5]}
    return EvaluateWarnings(warnings, _door_id, values)


def TB(_door_id):
    warnings = [CheckDoorSubtype, CheckDoorLeadsOutside,
                CheckDoorClosestDoorSubtypeIsNot,  CheckDoorLeadsToLevels]
    values = {"illegalSubtype": "turnstile",
              "closestSubtype": "turnstile", "illegalLevels": [3, 4, 5]}
    return EvaluateWarnings(warnings, _door_id, values)


def P(_door_id):
    warnings = [CheckDoorLeadsOutside,
                CheckDoorHasEqualLevels,  CheckDoorLeadsToLevels]
    values = {"illegalLevels": [1, 5]}
    return EvaluateWarnings(warnings, _door_id, values)


def LA(_door_id):
    warnings = [CheckDoorIsInteriorDoor, CheckDoorHasEqualLevels,
                CheckDoorLeadsToLevels, CheckDoorHasNumberOfAxis]
    values = {"illegalLevels": [4, 5], "axisAmount": 2}
    return EvaluateWarnings(warnings, _door_id, values)


def PE(_door_id):
    warnings = [CheckDoorIsInteriorDoor,
                CheckDoorSubtypeIsNot, CheckDoorLeadsToLevels]
    values = {"illegalLevels": [2, 3, 4, 5], "subtype": "sliding"}
    return EvaluateWarnings(warnings, _door_id, values)


def AHE(_door_id):
    warnings = [CheckDoorIsInteriorDoor,
                CheckDoorSubtypeIsNot, CheckDoorLeadsToLevels]
    values = {"illegalLevels": [2, 3, 4, 5], "subtype": "sliding"}
    return EvaluateWarnings(warnings, _door_id, values)


def C(_door_id):
    warnings = [CheckDoorHasEqualLevels, CheckDoorDoesntLeadToLevel,
                CheckDoorLeadsOutside, CheckDoorLeadsToLevels]
    values = {"obligatoryLevel": 5, "illegalLevels": [1, 2]}
    return EvaluateWarnings(warnings, _door_id, values)


"""
def D(_door_id):
    warnings = [  CheckDoorLeadsOutside , CheckDoorLeadsToLevel,CheckDoorHasEqualLevels, CheckDoorIsInteriorDoor, CheckDoorLeadsToLevels  ]
    values = {"obligatoryLevel": 4, "illegalLevels" : [1,2]}
    return EvaluateWarnings(warnings, _door_id, values)

def R(_door_id): 
    return [CreateWarning("DOOR",_door_id,"door type R not implemented yet")]

"""


def B(_door_id):
    return []


def RU(_door_id):
    warnings = [CheckDoorIsInteriorDoor,
                CheckDoorSubtypeIsNot, CheckDoorLeadsToLevels]
    values = {"subtype": "loading", "illegalLevels": [4, 5]}
    return EvaluateWarnings(warnings, _door_id, values)


######################## High level functions by zone sec level ###############################

def EvalZone0(_zone):
    warnings = []
    values = {}
    return EvalZoneWarnings(warnings, values, _zone)


def EvalZone1(_zone):
    warnings = [CheckZoneHasAtLeastOneAHE,
                CheckZoneHasOnlyOneAHE, CheckZoneHasOpenings]
    values = {}
    return EvalZoneWarnings(warnings, values, _zone)


def EvalZone2(_zone):
    warnings = [CheckZoneNeedsTB, CheckZoneHasOnlyOneTB,
                CheckZoneHasOpenings, CheckZoneHasNonExitEntrance]
    values = {}
    return EvalZoneWarnings(warnings, values, _zone)


def EvalZone3(_zone):
    warnings = [CheckZoneHasTooManyLA, CheckZoneIllegalConnectedSecurityLevels,
                CheckZoneHasOpenings, CheckZoneHasNonExitEntrance]
    values = {"illegalConnectedLevels": [1]}
    return EvalZoneWarnings(warnings, values, _zone)


def EvalZone4(_zone):
    warnings = [CheckZoneIllegalConnectedSecurityLevels, CheckZoneHasOpenings]
    values = {"illegalConnectedLevels": [1, 2]}
    return EvalZoneWarnings(warnings, values, _zone)


def EvalZone5(_zone):
    warnings = [CheckZoneIllegalConnectedSecurityLevels, CheckZoneHasWindows,
                CheckZoneHasOpenings, CheckZoneHasMultipleEntrances]
    values = {"illegalConnectedLevels": [1, 2]}
    return EvalZoneWarnings(warnings, values, _zone)


def EvalZoneWarnings(_zone_warnings, _values, _zone):
    res = []
    for Warning in _zone_warnings:
        eval = Warning(_values, _zone)
        if eval:
            res.extend(eval)
    return res

######################### ZONE CHECKS ##############################


def CheckZoneHasWindows(_values, _zone_id):
    zone_data = GetNodeData(_zone_id)
    warnings = []
    for room_id in zone_data["rooms"]:
        neighbors = [y for x, y, z in G.edges(room_id, data=True)]
        windows = [x for x in neighbors if G.nodes[x]['type'] == 'WINDOW']
        if len(windows) > 0:
            msg = "Zone " + \
                str(zone_data["securityLevel"]) + " room cannot have windows"
            # roomId field in zone warnings contain information for localizing the source of the warning
            fix = "\nchange security level to 4 or lower"
            warnings.append(CreateWarning(
                "ROOM", room_id, msg + fix,  _level=3))
    return warnings


def CheckZoneHasOpenings(_values, _zone_id):
    openings = GetZoneOpenings(_zone_id)
    zone_data = GetNodeData(_zone_id)

    if len(openings) == 0:
        return []
    opening_to_rooms = set()
    for o_id in openings:
        connected_ids = [y for x, y, z in G.edges(
            o_id, data=True) if z['type'] == 'CONNECTED']
        for id in connected_ids:
            if id not in zone_data["rooms"]:
                opening_to_rooms.add(id)

    warnings = []
    for room in opening_to_rooms:
        if GetRoomSecurity(room) < zone_data["securityLevel"]:
            msg = "Room has opening leading to a higher security level"
            fix = "\nchange security level to " + \
                str(zone_data["securityLevel"])
            warnings.append(CreateWarning("ROOM", room, msg+fix, _level=3))
    return warnings


def CheckZoneHasMultipleEntrances(_values, _zone_id):
    entrances = GetZoneDoors(_zone_id) + GetZoneExits(_zone_id)
    zone_data = GetNodeData(_zone_id)
    if len(entrances) < 2:
        return []

    rooms_with_entrance = set()
    for e_id in entrances:
        connected_ids = [y for x, y, z in G.edges(
            e_id, data=True) if z['type'] == 'CONNECTED']
        for id in connected_ids:
            if id in zone_data["rooms"]:
                rooms_with_entrance.add(id)
    warnings = []
    msg = "Zone " + str(zone_data["securityLevel"]) + \
        " cannot have more than one entrance"
    fix = "\nchange security level to 4 or lower"

    for r_id in rooms_with_entrance:
        # roomId feild in zone warnings contain information for loaclaizing the source of the warning

        warnings.append(CreateWarning("ROOM", r_id, msg+fix, _level=3))
    return warnings


def CheckZoneHasNonExitEntrance(_values, _zone_id):
    entrances = GetZoneDoors(_zone_id) + GetZoneExits(_zone_id)
    zone_data = GetNodeData(_zone_id)
    if len(entrances) == 0:
        return []
    exits = GetEntrancesByCategory(_zone_id, "E")
    warnings = []
    if len(entrances) == len(exits):
        msg = "Zone has to have at least one entrance which is not an emergency exit"
        for d_id in entrances:
            warnings.append(CreateWarning("DOOR", d_id, msg, _level=1))
    return warnings


def CheckZoneIllegalConnectedSecurityLevels(_values, _zone_id):

    all_exits = GetZoneDoors(_zone_id) + GetZoneExits(_zone_id)
    zone_data = GetNodeData(_zone_id)
    if zone_data["securityLevel"] == 0:
        return []
    rooms_with_problems = []
    other_sec_levels = []

    for e_id in all_exits:
        sec_level = GetconnectedSecurityLevel(e_id, _zone_id)
        if sec_level in _values["illegalConnectedLevels"]:
            connected_ids = [y for x, y, z in G.edges(
                e_id, data=True) if z['type'] == 'CONNECTED']
            room_id = [
                id for id in connected_ids if id in zone_data["rooms"]][0]
            if room_id not in rooms_with_problems:
                other_sec_levels.append(sec_level)
                rooms_with_problems.append(room_id)

    warnings = []
    for i in range(len(rooms_with_problems)):
        msg = "Zone " + str(zone_data["securityLevel"]) + \
            " should not be accessed from zone " + str(other_sec_levels[i])
        warnings.append(CreateWarning(
            "ROOM", rooms_with_problems[i], msg, _level=3))
    return warnings


def CheckZoneHasAtLeastOneAHE(_values, _zone_id):

    PEs = GetEntrancesByCategory(_zone_id, "PE")
    AHEs = GetEntrancesByCategory(_zone_id, "AHE")
    if len(AHEs) < 1 and len(PEs) > 0:
        msg = "Zone has no AHE. consider changing this door to AHE"
        # searching from the first and last turnstile will work well for the PoC
        # it does not garentee perfect results on a different plan
        return [CreateWarning("DOOR", PEs[-1], msg, _level=1), CreateWarning("DOOR", PEs[0], msg, _level=1)]
    return []


def CheckZoneHasOnlyOneAHE(_values, _zone_id):

    AHEs = GetEntrancesByCategory(_zone_id, "AHE")
    if len(AHEs) > 1:
        AHE_warnings = []
        msg = "Zone has too many AHE's"
        for AHE_id in AHEs:
            AHE_warnings.append(CreateWarning("DOOR", AHE_id, msg, _level=1))
        return AHE_warnings
    return []


def CheckZoneHasOnlyOneTB(_values, _zone_id):

    foundTB = GetEntrancesByCategory(_zone_id, "TB")
    if len(foundTB) < 2:
        return []

    warnings = []
    for TB_id in foundTB:
        msg = "Zone has too many TB's"
        warnings.append(CreateWarning("DOOR", TB_id, msg, _level=1))
    return warnings


def CheckZoneNeedsTB(_values, _zone_id):

    foundT = GetEntrancesByCategory(_zone_id, "T")
    if len(foundT) == 0:
        return []

    warnings = []
    foundTB = GetEntrancesByCategory(_zone_id, "TB")

    if len(foundTB) == 0:

        msg = "One of the exits next to a turnstile should be a Turnstile bypass"
        door_ids = GetZoneExits(_zone_id) + GetZoneDoors(_zone_id)
        # searching from the first and last turnstile will work well for the PoC
        # it does not garentee perfect results on a different plan
        warnings.append(CreateWarning("DOOR", GetClosestNonTDoor(
            foundT[0], door_ids), msg, _level=1))
        warnings.append(CreateWarning("DOOR", GetClosestNonTDoor(
            foundT[-1], door_ids), msg, _level=1))
    return warnings


def CheckZoneHasTooManyLA(_values, _zone_id):

    foundLA = GetEntrancesByCategory(_zone_id, "LA", False)
    if len(foundLA) < 2:
        return []

    warnings = []
    for id in foundLA:
        msg = "Zone has " + str(len(foundLA)) + " Limited Access Doors"
        warnings.append(CreateWarning("DOOR", id, msg, _level=1))
    return warnings

############################### DOOR  HELPER FUNCTIONS ###############################


def GetRoomsFromDoor(_door_id):

    connected_ids = [y for x, y, z in G.edges(
        _door_id, data=True) if z['type'] == 'CONNECTED']
    room_list = [id for id in connected_ids if G.nodes[id]['type'] == 'ROOM']
    if len(room_list) == 1:
        room_list.append(-1)
    return room_list


def GetDoorsFromDoor(_door_id):
    rooms = GetRoomsFromDoor(_door_id)
    door_list = []
    for room in rooms:
        if room == -1:
            continue
        connected_ids = [y for x, y, z in G.edges(
            room, data=True) if z['type'] == 'CONNECTED']
        door_list.extend([id for id in connected_ids if G.nodes[id]
                          ['type'] == 'DOOR' and id != _door_id])
    return door_list


def GetClosestDoor(_door_id, _door_list):
    p_for_cloud = []
    for door in _door_list:
        mid = GetNodeData(door)["midPoint"]
        p_for_cloud.append(rh.Geometry.Point3d(mid["x"], mid["y"], mid["z"]))

    cloud = rh.Geometry.PointCloud(p_for_cloud)
    this_mid = GetNodeData(_door_id)["midPoint"]
    this_point = rh.Geometry.Point3d(
        this_mid["x"], this_mid["y"], this_mid["z"])
    closest_index = cloud.ClosestPoint(this_point)
    if closest_index < 0:
        return _door_id
    return _door_list[closest_index]


def GetDoorSecuritylevels(_door_id):
    rooms = GetRoomsFromDoor(_door_id)
    return [GetRoomSecurity(rooms[0]), GetRoomSecurity(rooms[1])]


def EvaluateWarnings(_warnings, _door_id, _values):
    # evaluate all possible warnings for each door catgeory
    res = []
    for Warning in _warnings:
        eval = Warning(_door_id, _values)
        if eval:
            res.append(eval)
    return res


######################### ZONE HELPER FUNCTIONS #######################

def PrintZone(_zone_id):
    data = GetNodeData(_zone_id)
    print "index: ", data["index"], " rooms: ", len(data["rooms"]), " doors: ",  len(GetZoneDoors(zone_id)), \
        " level: ", data["securityLevel"]
    print "exits: ", GetZoneExits(_zone_id)
    print "zone doors", GetZoneDoors(_zone_id)


def GetEntrancesByCategory(_zone_id, _category, _include_doors=True):
    door_ids = GetZoneExits(_zone_id)
    if _include_doors:
        door_ids = door_ids + GetZoneDoors(_zone_id)
    return [id for id in door_ids if GetNodeData(id)["category"] == _category]


def GetZoneFromRoom(_room_id):
    if _room_id == -1:
        return
    id = [y for x, y, z in G.edges(
        _room_id, data=True) if z['type'] == 'INCLUDED']
    if id:
        return id[0]
    return


def GetClosestNonTDoor(_door_id, _door_list):
    p_for_cloud = []
    cand_doors = []
    for door in _door_list:
        if GetNodeData(door)["category"] == "T":
            continue
        if door == _door_id:
            continue

        mid = GetNodeData(door)["midPoint"]
        p_for_cloud.append(rh.Geometry.Point3d(mid["x"], mid["y"], mid["z"]))
        cand_doors.append(door)
    if len(cand_doors) == 0:
        return _door_id
    cloud = rh.Geometry.PointCloud(p_for_cloud)
    this_mid = GetNodeData(_door_id)["midPoint"]
    this_point = rh.Geometry.Point3d(
        this_mid["x"], this_mid["y"], this_mid["z"])
    closest_index = cloud.ClosestPoint(this_point)
    return cand_doors[closest_index]


def GetZoneOpenings(_zone_id):
    zone_room_ids = GetNodeData(_zone_id)["rooms"]
    zone_openings = set()

    for room_id in zone_room_ids:
        connected_ids = [y for x, y, z in G.edges(
            room_id, data=True) if z['type'] == 'CONNECTED']
        opening_ids = [id for id in connected_ids if G.nodes[id]
                       ['type'] == 'OPENING']
        for opening_id in opening_ids:
            connects = [y for x, y, z in G.edges(
                opening_id, data=True) if z['type'] == 'CONNECTED']
            for connected_room in connects:
                if connected_room not in zone_room_ids:
                    zone_openings.add(opening_id)
    return list(zone_openings)


def GetZoneDoors(_zone_id):

    zone_room_ids = GetNodeData(_zone_id)["rooms"]
    zone_doors = set([])
    for room_id in zone_room_ids:
        connected_ids = [y for x, y, z in G.edges(
            room_id, data=True) if z['type'] == 'CONNECTED']
        door_ids = [id for id in connected_ids if G.nodes[id]
                    ['type'] == 'DOOR']
        for door_id in door_ids:
            connects = [y for x, y, z in G.edges(
                door_id, data=True) if z['type'] == 'CONNECTED']
            for connected_room in connects:
                if connected_room not in zone_room_ids:
                    zone_doors.add(door_id)
    return list(zone_doors)


def GetZoneExits(_zone_id):
    zone_room_ids = GetNodeData(_zone_id)["rooms"]
    exit_guids = set([])
    for room_id in zone_room_ids:
        connected_ids = [y for x, y, z in G.edges(
            room_id, data=True) if z['type'] == 'CONNECTED']
        door_ids = [id for id in connected_ids if G.nodes[id]
                    ['type'] == 'DOOR']
        for d_id in door_ids:
            if -1 in GetNodeData(d_id)["connectsGuid"]:
                exit_guids.add(d_id)
    return list(exit_guids)


def GetconnectedSecurityLevel(_exit_id, _zone_id):
    rooms = GetRoomsFromDoor(_exit_id)
    for room in rooms:
        if room == -1:
            return 1
        if room in GetNodeData(_zone_id)["rooms"]:
            continue
        else:
            return GetNodeData(room)["securityLevel"]


def GetRoomSecurity(_room_id):
    if _room_id == -1:
        return 1
    return GetNodeData(_room_id)["securityLevel"]


def GetZoneCenter(_zone_data):
    x, y, z, count = 0, 0, 0, 0
    for room_id in _zone_data["rooms"]:
        for point_dict in GetNodeData(room_id)["geom"]:
            x += point_dict["x"]
            y += point_dict["y"]
            z += point_dict["z"]
            count += 1
    return rh.Geometry.Point3d(x/count, y/count, z/count)


def GetRoomCenter(_room_data):
    x, y, z, count = 0, 0, 0, 0
    for point_dict in _room_data["geom"]:
        x += point_dict["x"]
        y += point_dict["y"]
        z += point_dict["z"]
        count += 1
    return rh.Geometry.Point3d(x/count, y/count, z/count)


######################### GENERAL HELPER FUNCTIONS #######################

def GetNodeData(_node_id):
    return G.node[_node_id]


def CreateWarning(_type, _guid, _msg, _info=None, _level=2):
    return {
        "warningMsg": _msg,
        "objectGuid": _guid,
        "objectType": _type,
        "info": _info,
        "warningLevel": _level
    }


def ReadPointDict(_dict):
    return rh.Geometry.Point3d(_dict["x"], _dict["y"], _dict["z"])


###################### MAIN LEVEL FUNCTIONS ####################################

def TestDoorByCategory(_door_id):
    # select the appropriate function by the door catgeory
    door_data = GetNodeData(_door_id)
    if not door_data["category"] in CATEGORY_FUNCTIONS:
        warning = CreateWarning(
            "DOOR", _door_id, ("no such category" + door_data["category"]))
        return [warning]
    cat_function = CATEGORY_FUNCTIONS[door_data["category"]]

    return cat_function(_door_id)


def GetAllWarnings():

    new_warnings = []
    zone_ids = [x for x, y in G.nodes(data=True) if y['type'] == "ZONE"]
    door_ids = [x for x, y in G.nodes(data=True) if y['type'] == 'DOOR']

    for door_id in door_ids:
        new_warnings.extend(TestDoorByCategory(door_id))
    for z_id in zone_ids:
        zone_sec_level = GetNodeData(z_id)["securityLevel"]
        EvalFunction = ZONE_FUNCTIONS[zone_sec_level]
        zone_warnings = EvalFunction(z_id)
        new_warnings.extend(zone_warnings)
    return new_warnings

# region=test
###################### INIT DATA #############################################
DOOR_CATEGORIES = ["B", "N", "PE", "AHE", "T", "TB", "LA", "P", "E", "RU", "C"]

# function lookup dict
CATEGORY_FUNCTIONS = {"B": B,  "N": N, "PE": PE, "AHE": AHE, "T": T, "TB": TB,
                      "LA": LA, "P": P, "E": E, "RU": RU, "C": C}

# door name dict
CATEGORY_STRINGS = {"B": "Blanck", "N": "Non-Protected door ", "PE": "Primary Entrance",
                    "AHE": "After Hours Entrance ", "T": "Turnstile ", "TB": "Turnstile Bypass ",
                    "LA": "Limited Access door ", "P": " Pedestrian door ", "E": "Emergency Exit ",
                    "RU": "Roll Up door", "C": "Critical data door"}

ZONE_FUNCTIONS = [EvalZone0, EvalZone1,
                  EvalZone2, EvalZone3, EvalZone4, EvalZone5]

# endregion
###################### MAIN #############################################

door_ids = [x for x, y in G.nodes(data=True) if y['type'] == 'DOOR']
cats_no_B = DOOR_CATEGORIES[1:]
door_points = []
all_options = []
opt_strings = []

# first loop - get door suggestions
for door_id in door_ids:

    door_data = GetNodeData(door_id)
    mid = door_data["midPoint"]
    door_points.append(rh.Geometry.Point3d(mid["x"], mid["y"], 0))

    sec_levels = GetDoorSecuritylevels(door_id)
    if 0 in sec_levels:
        door_data.update({"category": "B"})
        opt_strings.append("")
        continue

    warning_counts, level_counts = [], []
    # traverse the possible categories, checking only the door generatged errors
    for new_cat in cats_no_B:
        door_data.update({"category": new_cat})
        warnings = TestDoorByCategory(door_id)
        warning_counts.append(len(warnings))
        level_count = 0
        for w in warnings:
            level_count += w["warningLevel"]
        level_counts.append(level_count)

    # the recommended category is the one with the minimal amount of accumilated warning levels
    new_cat = cats_no_B[level_counts.index(min(level_counts))]
    # other option are categories didnt accumilate a lot of warning levels, I put the threshold at 3
    options = [cats_no_B[i]
               for i in range(len(cats_no_B)) if level_counts[i] < threshold]

    opt_strings.append(str(options))  # for GH view purposes
    door_data.update({"category": new_cat})


# this is a GH function which simulates user over of door catregory
midPointCloud = rh.Geometry.PointCloud(door_points)

for o_index in range(len(__overide_points)):
    o_point = __overide_points[o_index]
    o_cat = __overide_layers[o_index]
    closest_index = midPointCloud.ClosestPoint(o_point)
    data = GetNodeData(door_ids[closest_index])
    data.update({"category": o_cat})

categories = [GetNodeData(door)["category"]
              for door in door_ids]  # for GH view purposes

# now all possible warnings (including zone warnings) are tested and displayed on the final state
warnings = GetAllWarnings()

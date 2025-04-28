# Classroom scheduling problem
# Greedy approach
classes = {}
classes["art"] = {}
classes["art"]["start"] = 9
classes["art"]["end"] = 10
classes["eng"] = {}
classes["eng"]["start"] = 9.5
classes["eng"]["end"] = 10.5
classes["math"] = {}
classes["math"]["start"] = 10
classes["math"]["end"] = 11
classes["cs"] = {}
classes["cs"]["start"] = 10.5
classes["cs"]["end"] = 11.5
classes["music"] = {}
classes["music"]["start"] = 11
classes["music"]["end"] = 12

# assume the classes are provided to you in a sorted order already
classNames = ["art", "eng", "math", "cs", "music"]

def schedule_max_amount_of_classes(classes, classNames):

    # set the initial values of soonest_end_time and schedule

    end_time = 0
    schedule = []

    for c in classNames:
        if classes[c]["end"] >= end_time:
            if schedule != [] and classes[c]["start"] < end_time:
                continue
            else:
                end_time = classes[c]["end"]
                schedule.append(c)

    return schedule

# print(schedule_max_amount_of_classes(classes, classNames))


# Set covering problem
# Greedy approach
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

def greedy_set_cover(states_needed, stations):
    # go through the stations and find the best station. The best station is the one that covers the most states that aren't covered yet
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_covered_in_station in stations.items():
            covered = states_needed & states_covered_in_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        
        states_needed -= states_covered
        final_stations.add(best_station)


# greedy_set_cover(states_needed, stations)
# print(final_stations)


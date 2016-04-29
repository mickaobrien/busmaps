import json
import requests

def get_route_details(route_number):
    url = 'http://rtpi.ie/ConnectService.svc/GetPublicServicesForCriteriaSerialized'
    data = '{"searchString": %d, "districtId": -1}' % route_number
    r = requests.post(url, data=data, headers={'content-type': 'application/json; charset=UTF-8'})
    if not r.ok:
        print 'Couldn\'t get data for route {}'.format(route_number)
    json_string = r.content.replace('\\', '').split('=')[1][:-2]
    return json.loads(json_string)


def get_stop_details(stop_number):
    url = 'http://rtpi.ie/ConnectService.svc/GetStopsFromStopRef'
    data = '{"stopref": %d}' % stop_number
    r = requests.post(url, data=data, headers={'content-type': 'application/json; charset=UTF-8'})
    if not r.ok:
        print 'Couldn\'t get data for stop {}'.format(route_number)
    json_string = r.content.replace('\\', '').split('=')[1][:-2]
    return json.loads(json_string)

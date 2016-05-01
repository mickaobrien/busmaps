import json
import requests


def get_route_details():
    url = 'http://rtpi.ie/ConnectService.svc/GetServiceDataSerialized'
    data = '{"publicServiceCode":"202","operatorID":2,"depotID":1,"serviceVariantIDs":"866,867,873,874,875","routeLineNodes":"none"}'
    route = get_data(url, data)
    return route['AllStops']


def get_route_options(route_number):
    url = 'http://rtpi.ie/ConnectService.svc/GetPublicServicesForCriteriaSerialized'
    data = '{"searchString": %d, "districtId": -1}' % route_number
    return get_data(url, data)


def get_stop_details(stop_number):
    url = 'http://rtpi.ie/ConnectService.svc/GetStopsFromStopRef'
    data = '{"stopref": %d}' % stop_number
    return get_data(url, data)


def get_data(url, data):
    r = requests.post(url, data=data, headers={'content-type': 'application/json; charset=UTF-8'})
    if not r.ok:
        print 'Couldn\'t get data:\n url: {}\n data: {}'.format(url, data)
    json_string = r.content.replace('\\', '').split('=')[1][:-2]
    return json.loads(json_string)

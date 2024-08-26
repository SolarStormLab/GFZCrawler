import json
from .worker import get_data, source_links, pattern, OUTPUT, TEMP

kp_data = {
	'nowcast': get_data(source_links['nowcast']['kp'], pattern['kp']),
	'complete': get_data(source_links['complete']['kp'], pattern['kp']),
}

def kp_format(data):
    return {
			'year': int(data['year']),
			'month': int(data['month']),
			'day': int(data['day']),
			'days': int(data['days']),
			'days_m': float(data['days_m']),
			'bsr': int(data['bsr']),
			'db': int(data['db']),
			'kp1': float(data['kp1']),
			'kp2': float(data['kp2']),
			'kp3': float(data['kp3']),
			'kp4': float(data['kp4']),
			'kp5': float(data['kp5']),
			'kp6': float(data['kp6']),
			'kp7': float(data['kp7']),
			'kp8': float(data['kp8']),
			'ap1': int(data['ap1']),
			'ap2': int(data['ap2']),
			'ap3': int(data['ap3']),
			'ap4': int(data['ap4']),
			'ap5': int(data['ap5']),
			'ap6': int(data['ap6']),
			'ap7': int(data['ap7']),
			'ap8': int(data['ap8']),
			'ap': int(data['ap']),
			'sn': int(data['sn']),
			'f107obs': float(data['f107obs']),
			'f107adj': float(data['f107adj']),
			'd': int(data['d']),
		}

def parse_data():
    
    nowcast = []
    complete = []
    
    for n in kp_data['nowcast']:
        nowcast.append(kp_format(n))
    
    for c in kp_data['complete']:
        complete.append(kp_format(c))
        
    with open(TEMP / 'kp_nowcast_new.json', 'w') as file:
        json.dump(nowcast, file, indent=4)
        
    with open(TEMP / 'kp_complete_new.json', 'w') as file:
        json.dump(complete, file, indent=4)
        
parse_data()

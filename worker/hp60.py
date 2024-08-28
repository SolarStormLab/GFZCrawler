import os, sys, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from worker import get_data, source_links, pattern, TEMP

hp60_data = {
	'nowcast': get_data(source_links['nowcast']['hp_ap_60'], pattern['hp60']),
	'complete': get_data(source_links['complete']['hp_ap_60'], pattern['hp60']),
}

def hp60_format(data):
    return {
			'year': int(data['year']),
			'month': int(data['month']),
			'day': int(data['day']),
			'hh_h': float(data['hh_h']),
			'hh_m': float(data['hh_m']),
			'days': int(data['days']),
			'days_m': float(data['days_m']),
			'hp60': float(data['hp60']),
			'ap60': int(data['ap60']),
			'd': int(data['d']),
		}

def parse_data():
    
    nowcast = []
    complete = []
    
    for n in hp60_data['nowcast']:
        nowcast.append(hp60_format(n))
    
    for c in hp60_data['complete']:
        complete.append(hp60_format(c))
        
    with open(TEMP / 'hp60_nowcast_new.json', 'w') as file:
        json.dump(nowcast, file, indent=4)
        
    with open(TEMP / 'hp60_complete_new.json', 'w') as file:
        json.dump(complete, file, indent=4)
        
parse_data()
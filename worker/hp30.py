import os, sys, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from worker import get_data, source_links, pattern, TEMP

hp30_data = {
	'nowcast': get_data(source_links['nowcast']['hp_ap_30'], pattern['hp30']),
	'complete': get_data(source_links['complete']['hp_ap_30'], pattern['hp30']),
}

def hp30_format(data):
    return {
		'year': int(data['year']),
		'month': int(data['month']),
		'day': int(data['day']),
  		'hh_h': float(data['hh_h']),
		'hh_m': float(data['hh_m']),
		'days': float(data['days']),
		'days_m': float(data['days_m']),
		'hp30': float(data['hp30']),
		'ap30': int(data['ap30']),
		'd': int(data['d']),
	}

def parse_data():
    
    nowcast = []
    complete = []
    
    for n in hp30_data['nowcast']:
        nowcast.append(hp30_format(n))
    
    for c in hp30_data['complete']:
        complete.append(hp30_format(c))
        
    with open(TEMP / 'hp30_nowcast_new.json', 'w') as file:
        json.dump(nowcast, file, indent=4)
        
    with open(TEMP / 'hp30_complete_new.json', 'w') as file:
        json.dump(compress(complete), file, indent=4)
        
parse_data()

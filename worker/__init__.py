from pathlib import Path
import requests, re, sys, os, urllib3

ROOT = Path(__file__).parent.parent
OUTPUT = ROOT / 'output'
TEMP = ROOT / 'temp'
WORKER = ROOT / 'worker'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sys.path.append(os.path.dirname(WORKER))

source_links = {
    'nowcast': {
		'hp_ap_30': 'https://kp.gfz-potsdam.de/app/files/Hp30_ap30_nowcast.txt',
		'hp_ap_60': 'https://kp.gfz-potsdam.de/app/files/Hp60_ap60_nowcast.txt',
		'kp': 'https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_nowcast.txt'
	},
    'complete': {
		'hp_ap_30': 'https://kp.gfz-potsdam.de/app/files/Hp30_ap30_complete_series.txt',
		'hp_ap_60': 'https://kp.gfz-potsdam.de/app/files/Hp60_ap60_complete_series.txt',
		'kp': 'https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt'
	}
}

pattern = {
	'hp30': r"^(?P<year>\d{4})\s+(?P<month>\d{2})\s+(?P<day>\d{2})\s+(?P<hh_h>\d{,2}\.\d{1})\s+(?P<hh_m>\d{,2}\.\d{,2})\s+(?P<days>\d{,5}\.\d{,5})\s+(?P<days_m>\d{,5}\.\d{,5})\s+(?P<hp30>-?\d{,2}\.\d{,3})\s+(?P<ap30>-?\d{,4})\s+(?P<d>-?\d{1})$",
	'hp60': r"^(?P<year>\d{4})\s+(?P<month>\d{2})\s+(?P<day>\d{2})\s+(?P<hh_h>\d{,2}\.\d{1})\s+(?P<hh_m>\d{,2}\.\d{,2})\s+(?P<days>\d{,5}\.\d{,5})\s+(?P<days_m>\d{,5}\.\d{,5})\s+(?P<hp60>-?\d{,2}\.\d{,3})\s+(?P<ap60>-?\d{,4})\s+(?P<d>-?\d{1})$",
	'kp': r"^(?P<year>\d{4})\s+(?P<month>\d{2})\s+(?P<day>\d{2})\s+(?P<days>\d{5})\s+(?P<days_m>\d{5}\.\d{1})\s+(?P<bsr>-?\d{4})\s+(?P<db>-?\d{,2})\s+(?P<kp1>-?\d{,2}.\d{,3})\s+(?P<kp2>-?\d{,2}.\d{,3})\s+(?P<kp3>-?\d{,2}.\d{,3})\s+(?P<kp4>-?\d{,2}.\d{,3})\s+(?P<kp5>-?\d{,2}.\d{,3})\s+(?P<kp6>-?\d{,2}.\d{,3})\s+(?P<kp7>-?\d{,2}.\d{,3})\s+(?P<kp8>-?\d{,2}.\d{,3})\s+(?P<ap1>-?\d{,4})\s+(?P<ap2>-?\d{,4})\s+(?P<ap3>-?\d{,4})\s+(?P<ap4>-?\d{,4})\s+(?P<ap5>-?\d{,4})\s+(?P<ap6>-?\d{,4})\s+(?P<ap7>-?\d{,4})\s+(?P<ap8>-?\d{,4})\s+(?P<ap>-?\d{,4})\s+(?P<sn>-?\d{,3})\s+(?P<f107obs>-?\d{,6}\.\d{1})\s+(?P<f107adj>-?\d{,6}\.\d{1})\s+(?P<d>-?\d{1})$"
}

def get_data(link: str, pattern: str):
    response = requests.get(link, verify=False)
    lines = response.text.split('\n')
    
    source_data = []
    for l in lines:
        match = re.search(pattern, l)
        
        if match is not None:
            source_data.append(match.groupdict())
    
    return source_data

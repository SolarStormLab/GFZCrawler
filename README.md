# GFZCrawler

![GitHub manifest version](https://img.shields.io/github/manifest-json/v/SolarStormLab/GFZCrawler?style=flat-square&label=Version)![GitHub License](https://img.shields.io/github/license/SolarStormLab/GFZCrawler?style=flat-square&label=License)




Just mirroring some data from GFZ Potsdam as JSON files.

## Idea

I should thank [@RenanRB](https://github.com/RenanRB/KPIndex) for this idea to create a mirror through github

## Data

All output data can be find in **output** folder

- **Kp, ap, Ap, SN und F10.7 der letzten 30 Tage** -> [kp_nowcast.json](https://github.com/SolarStormLab/GFZCrawler/raw/refs/heads/main/output/kp_nowcast.json)
- **Kp, ap, Ap, SN und F10.7 seit 1932** -> [kp_complete.json](https://github.com/SolarStormLab/GFZCrawler/raw/refs/heads/main/output/kp_complete.json)
- **Hp30 und ap30 der letzten 30 Tage** -> [hp30_nowcast.json](https://github.com/SolarStormLab/GFZCrawler/raw/refs/heads/main/output/hp30_nowcast.json)
- **Hp30 und ap30 seit 1985** -> not possible with GitHub limitations. If you want to use it - fork this repo and uncomment https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp30.py#L35 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp30.py#L36 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp30.py#L41 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp30.py#L42 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/.github/workflows/hp30.yml#L46
- **Hp60 und ap60 der letzten 30 Tage** -> [hp60_nowcast.json](https://github.com/Gokujo/GFZCrawler/raw/main/output/hp60_nowcast.json)
- **Hp60 und ap60 seit 1985** -> not possible with GitHub limitations. If you want to use it - fork this repo and uncomment https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp60.py#L35 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp60.py#L36 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp60.py#L41 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/worker/hp60.py#L42 https://github.com/SolarStormLab/GFZCrawler/blob/a5401a10ccac1d1c7b9be76329f431c8f7ecd5eb/.github/workflows/hp60_kpindex.yml#L48


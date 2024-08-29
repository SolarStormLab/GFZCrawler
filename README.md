# GFZCrawler

Just mirroring some data from GFZ Potsdam as JSON files.

## Idea

I should thank [@RenanRB](https://github.com/RenanRB/KPIndex) for this idea to create a mirror through github

## Data

All output data can be find in **output** folder

- **Kp, ap, Ap, SN und F10.7 der letzten 30 Tage** -> [kp_nowcast.json](https://github.com/Gokujo/GFZCrawler/raw/main/output/kp_nowcast.json)
- **Kp, ap, Ap, SN und F10.7 seit 1932** -> [kp_complete.json](https://github.com/Gokujo/GFZCrawler/raw/main/output/kp_complete.json)
- **Hp30 und ap30 der letzten 30 Tage** -> [hp30_nowcast.json](https://github.com/Gokujo/GFZCrawler/raw/main/output/hp30_nowcast.json)
- **Hp30 und ap30 seit 1985** -> not possible with GitHub limitations. If you want to use it - fork this repo and uncomment https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp30.py#L35 https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp30.py#L36 https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp30.py#L41 https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp30.py#L42 https://github.com/Gokujo/GFZCrawler/blob/bbeceb40fe8bc9f436f2a7d89db14674a92b5c33/.github/workflows/hp3060.yml#L45
- **Hp60 und ap60 der letzten 30 Tage** -> [hp60_nowcast.json](https://github.com/Gokujo/GFZCrawler/raw/main/output/hp60_nowcast.json)
- **Hp60 und ap60 seit 1985** -> not possible with GitHub limitations. If you want to use it - fork this repo and uncomment https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp60.py#L35 https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp60.py#L36 https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp60.py#L41 https://github.com/Gokujo/GFZCrawler/blob/7f0039af753dd4ac9dac4f09e97d3ee7e76c33cd/worker/hp60.py#L42 https://github.com/Gokujo/GFZCrawler/blob/bbeceb40fe8bc9f436f2a7d89db14674a92b5c33/.github/workflows/hp3060.yml#L47


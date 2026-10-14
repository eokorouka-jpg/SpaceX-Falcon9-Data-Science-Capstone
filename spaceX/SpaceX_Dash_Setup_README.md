# SpaceX Interactive Dashboard — IBM Capstone

Completed **Tasks 1–4** from the IBM Plotly Dash lab:

1. Launch-site dropdown (`site-dropdown`) with **All Sites** and site-specific choices.
2. Success pie chart (`success-pie-chart`) that updates when a site is selected. All Sites shows successful landing counts by launch site; individual sites show success versus failure counts.
3. Payload range slider (`payload-slider`) from **0 to 10,000 kg**.
4. Landing-outcome scatter chart (`success-payload-scatter-chart`) filtered by site and payload range, coloured by booster version.

## Run locally (Windows, Command Prompt / Anaconda Prompt)

1. Put `spacex-dash-app.py` and `spacex_launch_dash.csv` **in the same folder**.
2. Download the original IBM dataset from:
   https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv
3. In a terminal opened in that folder, install packages:
   ```bash
   python -m pip install pandas dash plotly
   ```
4. Start the dashboard:
   ```bash
   python spacex-dash-app.py
   ```
5. Open **http://127.0.0.1:8050/** in your browser. Keep the terminal running.

## Capture evidence for IBM

Take screenshots of (a) all sites selected, (b) a specific site selected, and (c) a filtered payload range. Upload the Python script and screenshots to GitHub. The IBM lab notes that these will be used in the presentation.

## Findings to investigate

- Site with the **most successful landings** (all-sites pie chart)
- Site with the **highest success rate** (successes divided by all launches at that site)
- Payload ranges with highest and lowest landing success rates
- Booster version with highest landing success rate

Do not claim numeric results until you have loaded the original CSV and checked the dashboard or computed the grouped success rates.

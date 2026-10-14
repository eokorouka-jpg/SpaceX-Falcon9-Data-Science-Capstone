"""IBM SpaceX Data Science Capstone — completed Plotly Dash lab (Tasks 1–4).

Place spacex_launch_dash.csv alongside this file and run:
    python -m pip install pandas dash plotly
    python spacex-dash-app.py
Then visit http://127.0.0.1:8050
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

DATA_FILE = Path(__file__).with_name('spacex_launch_dash.csv')
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f'Missing {DATA_FILE.name}. Download the IBM dataset and save it next to this script:\n'
        'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
        'IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
    )

spacex_df = pd.read_csv(DATA_FILE)
required = ['Launch Site', 'class', 'Payload Mass (kg)', 'Booster Version Category']
missing = [c for c in required if c not in spacex_df.columns]
if missing:
    raise ValueError(f'Missing required columns in dataset: {missing}')
spacex_df['class'] = pd.to_numeric(spacex_df['class'], errors='coerce')
spacex_df['Payload Mass (kg)'] = pd.to_numeric(spacex_df['Payload Mass (kg)'], errors='coerce')
spacex_df = spacex_df.dropna(subset=required).copy()
spacex_df['class'] = spacex_df['class'].astype(int)

sites = sorted(spacex_df['Launch Site'].unique())
min_payload, max_payload = 0, 10000
app = Dash(__name__)
app.title = 'SpaceX Launch Records Dashboard'

app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#24324a'}),
    html.P('Explore first-stage landing outcomes by launch site, payload mass, and booster version.',
           style={'textAlign': 'center'}),
    html.Label('Select a launch site:'),
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': s, 'value': s} for s in sites],
        value='ALL', placeholder='Select a Launch Site here', searchable=True,
        clearable=False,
    ),
    dcc.Graph(id='success-pie-chart'),
    html.Label('Select payload mass range (kg):'),
    dcc.RangeSlider(
        id='payload-slider', min=min_payload, max=max_payload, step=1000,
        marks={i: f'{i:,}' for i in range(0, 10001, 2000)},
        value=[min_payload, max_payload],
        tooltip={'placement': 'bottom', 'always_visible': False},
    ),
    dcc.Graph(id='success-payload-scatter-chart'),
    html.P('Outcome: 1 = successful first-stage landing; 0 = unsuccessful landing.',
           style={'fontSize': '0.9rem', 'color': '#555'}),
], style={'maxWidth': '1100px', 'margin': 'auto', 'padding': '24px', 'fontFamily': 'Arial, sans-serif'})


# TASK 2 — Pie chart reacts to launch-site dropdown.
@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        successful = spacex_df.loc[spacex_df['class'] == 1]
        counts = successful.groupby('Launch Site').size().reset_index(name='Successful landings')
        fig = px.pie(counts, values='Successful landings', names='Launch Site',
                     title='Successful First-Stage Landings by Launch Site')
    else:
        filtered = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        counts = filtered['class'].value_counts().reindex([0, 1], fill_value=0)
        pie_df = pd.DataFrame({
            'Outcome': ['Unsuccessful landing', 'Successful landing'],
            'Count': counts.to_numpy(),
        })
        fig = px.pie(pie_df, values='Count', names='Outcome',
                     title=f'First-Stage Landing Outcomes at {entered_site}',
                     color='Outcome',
                     color_discrete_map={
                         'Successful landing': '#2ca02c',
                         'Unsuccessful landing': '#d62728',
                     })
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=20))
    return fig


# TASK 4 — Scatter chart reacts to site dropdown AND payload slider.
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('payload-slider', 'value'),
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered = spacex_df.loc[spacex_df['Payload Mass (kg)'].between(low, high)].copy()
    if entered_site != 'ALL':
        filtered = filtered.loc[filtered['Launch Site'] == entered_site]
    title = ('Landing Outcome vs. Payload Mass — All Sites' if entered_site == 'ALL'
             else f'Landing Outcome vs. Payload Mass — {entered_site}')
    fig = px.scatter(
        filtered, x='Payload Mass (kg)', y='class',
        color='Booster Version Category',
        hover_data=['Launch Site'], title=title,
        labels={'class': 'Landing Outcome (0 = failure, 1 = success)'},
    )
    fig.update_yaxes(tickvals=[0, 1], range=[-0.15, 1.15])
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=20))
    return fig


if __name__ == '__main__':
    app.run(debug=True, port=8050)

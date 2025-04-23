# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a Dash application
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Dropdown for launch site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            *[{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()]
        ],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),

    html.Br(),

    # TASK 2: Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),

    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: RangeSlider for payload
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: f'{i}' for i in range(0, 10001, 1000)},
        value=[min_payload, max_payload]
    ),

    html.Br(),

    # TASK 4: Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# TASK 2: Callback to update pie chart based on site selection
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie(site):
    if site == 'ALL':
        filtered_df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(filtered_df, names='Launch Site', title='Total Successful Launches by Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == site]
        fig = px.pie(filtered_df, names='class', title=f'Success vs. Failure for site {site}')
    return fig

# TASK 4: Callback to update scatter plot based on site and payload
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter(site, payload_range):
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == site]
        title = f'Correlation between Payload and Success for {site}'
    else:
        title = 'Correlation between Payload and Success for All Sites'

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=title,
        size='Payload Mass (kg)',
        hover_data=['Payload Mass (kg)']
    )
    return fig

# Run the app
# Run the app
if __name__ == '__main__':
    app.run()


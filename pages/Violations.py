from matplotlib.pyplot import get
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Output, Input, callback, dash_table , State
from .data_base_connections import get_mysql_data
import dash
from .options import *

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = Dash(__name__, external_stylesheets=external_stylesheets)

dash.register_page(__name__)

for i in ['Violation_Issue_Time', 'VIOLATION_ISSUE_DT', 'VIOLATION_OCCUR_DT', 'VIOLATOR_TYPE_CD', 'COAL_METAL_IND', 'MINE_TYPE', 'SECTION_OF_ACT', 'PART_SECTION', 'CIT_ORD_SAFE', 'LIKELIHOOD', 'INJ_ILLNESS', 'NEGLIGENCE', 'state']:
    if i =='state':
        dropdown_options1[i]=column_options(i,'Mines')
    else:
        dropdown_options1[i]=column_options(i,'Violations')

# def interaction_plots_layout():
layout = html.Div([
        html.Div([html.H3('MSHA Violations Dropdown')], id = 'title2'),
        
        html.Div([
            html.Div([
                html.Div([
                html.Div([html.H5('CALENDAR YEAR')], id = 'title2'),
                dcc.Dropdown(id='CAL_YR',placeholder='Violation Year', multi=True,value='select_all',
                            options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['year']),                   
                 
                        ]),   
                ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('VIOLATION ISSUE TIME')], id = 'title2'),
                    dcc.Dropdown(id='Violation_Issue_Time',placeholder='Violation Issue Time', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['Violation_Issue_Time'])         
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('VIOLATION ISSUE DATE')], id = 'title2'),
                    dcc.Dropdown(id='VIOLATION_ISSUE_DT',placeholder='Violation Issue Date', multi=True,value='select_all',
                                options= [{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['VIOLATION_ISSUE_DT'])      
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('VIOLATION OCCUR DATE')], id = 'title2'),
                    dcc.Dropdown(id='VIOLATION_OCCUR_DT',placeholder='Violation Occur Date', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['VIOLATION_OCCUR_DT'])       
                            ]),   
                    ],className='create_container1 three columns'),
            ], className='row flex-display'),
        html.Br(),
        html.Div([
            html.Div([
                html.Div([
                html.Div([html.H5('VIOLATOR TYPE')], id = 'title2'),
                dcc.Dropdown(id='VIOLATOR_TYPE_CD',placeholder='Violators Type', multi=True,value='select_all',
                            options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['VIOLATOR_TYPE_CD'])       
                        ]),   
                ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('MINING METHOD')], id = 'title2'),
                    dcc.Dropdown(id='Mining_method',placeholder='Mining Method', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['COAL_METAL_IND'])         
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('MINING TYPE')], id = 'title2'),
                    dcc.Dropdown(id='Mining_type',placeholder='Mining Type', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['MINE_TYPE'])         
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('SECTION OF ACT')], id = 'title2'),
                    dcc.Dropdown(id='SECTION_OF_ACT',placeholder='Section of Act', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['SECTION_OF_ACT'])       
                            ]),   
                    ],className='create_container1 three columns'),
            ], className='row flex-display'),
        html.Br(),
        html.Div([
            html.Div([
                html.Div([
                html.Div([html.H5('PART SECTION')], id = 'title2'),
                dcc.Dropdown(id='PART_SECTION',placeholder='Part of Section', multi=True,value='select_all',
                            options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['PART_SECTION'])         
                        ]),   
                ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('TYPE OF CITATION')], id = 'title2'),
                    dcc.Dropdown(id='Type_of_citation',placeholder='Type of citation', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['CIT_ORD_SAFE'])         
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('SERIOUSNESS')], id = 'title2'),
                    dcc.Dropdown(id='Seriousness',placeholder='Seriousness', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['LIKELIHOOD'])         
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('GRAVITY OF INJURY')], id = 'title2'),
                dcc.Dropdown(id='Gravity_of_injury',placeholder='Gravity of injury', multi=True,value='select_all',
                            options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['INJ_ILLNESS'])         
                        ]),   
                ],className='create_container1 three columns'),
            
            ], className='row flex-display'),
        html.Br(),
        html.Div([
            html.Div([
                html.Div([
                html.Div([html.H5('NEGLIGENCE')], id = 'title2'),
                    dcc.Dropdown(id='NEGLIGENCE',placeholder='NEGLIGENCE', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['NEGLIGENCE'])         
                            ]),   
                    ],className='create_container1 three columns'),
            html.Div([
                html.Div([
                html.Div([html.H5('STATE')], id = 'title2'),
                    dcc.Dropdown(id='state',placeholder='State', multi=True,value='select_all',
                                options=[{'label': 'Select All', 'value': 'select_all'}]+dropdown_options1['state'])         
                            ]),   
                    ],className='create_container1 three columns'),
            ], className='row flex-display'),
        html.Br(),
        html.Div([
            html.Button('SUBMIT', id='submit-val', n_clicks=0),
        ]),
        html.Br(),
        
        html.Div([
            html.Div([
                html.Div( id='table_placeholder34', children=[]),
            ],className='create_container2 six columns'),
            html.Div([
                html.Div([
                    html.Div([
                        html.H5('Select column name'),
                        dcc.Dropdown(id='column_name1',placeholder='',value='NEGLIGENCE',
                                    options=list(dropdown_options1.keys()))         
                        ],className='create_container1 six columns'),
                    html.Div([
                        html.H5('Select column value'),
                        dcc.Dropdown(id='column_value1',placeholder='Select Value', multi=True,value='select_all',
                                    options=[])         
                        ],className='create_container1 six columns'),   
                    ], className='row flex-display'),
                html.Br(),
                html.Div([
                    dcc.Graph(id='graph1242')]),   
            ],className='create_container2 six columns'),
        ], className='row flex-display'),            
    ])

query = """
WITH req_violations as 
(SELECT MINE_ID,CAL_YR,VIOLATION_ISSUE_TIME AS Violation_Issue_Time, VIOLATION_ISSUE_DT,PROPOSED_PENALTY, VIOLATION_OCCUR_DT, VIOLATOR_TYPE_CD, MINE_TYPE as Mining_type, COAL_METAL_IND as Mining_method, SECTION_OF_ACT, PART_SECTION, CIT_ORD_SAFE as Type_of_citation, LIKELIHOOD as Seriousness, INJ_ILLNESS as Gravity_of_injury, NEGLIGENCE from `peak-essence-367304.MSHA.VIOLATIONS`),
req_mines as 
(SELECT MINE_ID,CURRENT_MINE_TYPE as Mining_type, STATE as state FROM `peak-essence-367304.MSHA.MINES`)

SELECT 
* 
FROM req_violations
JOIN req_mines
USING (MINE_ID,Mining_type)  
 """
df = get_mysql_data(query)

@callback(
    Output('column_value1','options'),
    Input('column_name1','value')
)
def col_vale(column_name):
    return dropdown_options1[column_name] + [{'label': 'Select All', 'value': 'select_all'}]    

@callback(
    Output('graph1242','figure'),
    Input('column_name1','value'),
    Input('column_value1','value')
)
def col_val_plot(column_name,column_value):
    column_filter=select_all_check1(column_name,column_value)
    dff = df[df[column_name].isin(list(column_filter))] 
    # groupbycolumn = [column_name]
    # req_df = pd.DataFrame(dff.groupby(groupbycolumn)['DAYS_LOST', 'DAYS_RESTRICT'].sum()).reset_index()
    # req_df['DAYS_LOST + DAYS_RESTRICT']=req_df['DAYS_LOST']+req_df['DAYS_RESTRICT']
    print(dff.head())
    fig = px.bar(dff, x= column_name, y= "PROPOSED_PENALTY" , title=" Sample Plot")

    return fig       







@callback(
    Output('table_placeholder34','children'),
    Input('submit-val','n_clicks'),

    Input('Violation_Issue_Time','value'),
    Input('VIOLATION_ISSUE_DT','value'),
    Input('VIOLATION_OCCUR_DT','value'),
    Input('VIOLATOR_TYPE_CD','value'),
    Input('Mining_method','value'),
    Input('Mining_type','value'),
    Input('SECTION_OF_ACT','value'),
    Input('PART_SECTION','value'),
    Input('Type_of_citation','value'),
    Input('Seriousness','value'),
    Input('Gravity_of_injury','value'),
    Input('NEGLIGENCE','value'),
    Input('state','value')
    
)
def update_output(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    # fetch your data here with all 11 columns 
    # save the data in  df
    # year_filter=select_all_check('year',year)
    # time_filter=select_all_check('time',time)
    # operator_contractor_filter=select_all_check('operator_contractor',operator_contractor)
    # accident_date_filter=select_all_check('accident_date',accident_date)
    # state_filter=select_all_check('state',state)
    # mining_method_filter=select_all_check('mining_method',mining_method)
    # mining_type_filter=select_all_check('mining_type',mining_type)
    # occupation_category_filter=select_all_check('occupation_category',occupation_category)
    # activity_category_filter=select_all_check('activity_category',activity_category)
    # nature_of_injury_filter=select_all_check('nature_of_injury',nature_of_injury)
    # injury_body_part_filter=select_all_check('injury_body_part',injury_body_part)
    # df=df[df['CAL_YR'].isin(year_filter) & df['CAL_YR'].isin(time_filter) & df['CAL_YR'].isin(year_filter) & df['CAL_YR'].isin(year_filter) & df['CAL_YR'].isin(year_filter) & df['CAL_YR'].isin(year_filter) & df['CAL_YR'].isin(year_filter) ]
    dff=df#[["MINE_ID","DAYS_LOST","DAYS_RESTRICT","NO_AFFECTED"]]
    my_table = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in dff.columns],
        data=dff.head(20).to_dict('records'),
        virtualization=True,
        style_cell={'textAlign': 'left',
                    'min-width': '100px',
                    'backgroundColor': '#1f2c56',
                    'color': '#FEFEFE',
                    'border-bottom': '0.01rem solid #19AAE1'},
        style_header={'backgroundColor': '#1f2c56',
                    'fontWeight': 'bold',
                    'font': 'Lato, sans-serif',
                    'color': 'orange',
                    'border': '#1f2c56'},
        style_as_list_view=True,
        style_data={'styleOverflow': 'hidden', 'color': 'white'},
        fixed_rows={'headers': True},
        sort_action='native',
        sort_mode='multi'
    ) 
    return my_table
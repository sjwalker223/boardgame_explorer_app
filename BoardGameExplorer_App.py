import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

#Read necessary CSV files
Games_df = pd.read_csv("https://raw.githubusercontent.com/sjwalker223/board-games/main/Games_df.csv",index_col=0)
Game_Meta = pd.read_csv("https://raw.githubusercontent.com/sjwalker223/board-games/main/Game_Meta.csv",index_col=0)
knn_indices_df = pd.read_csv("https://raw.githubusercontent.com/sjwalker223/board-games/main/knn_indices_df.csv",index_col=0)

#Get index of board game from its name
def get_index_from_name(name):
    idx = Games_df[Games_df["handle"]==name].index.tolist()[0]
    return Games_df.index.get_loc(idx)

# Build app
app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Find new board games!"),
    html.Div([
        "Enter board game you already like: ",
        #Create a dropdown menu with the names of all board games in the database
        dcc.Dropdown(
            Games_df["handle"].values.tolist(), value='Root', id='my-input'),
        html.Div(id='dd-output-container')
    ]),
    html.Br(),
    html.Div(["We recommend: "]),
    #Return a table, each row with one recommendation
    #First column: game name and image; second column: game description
    html.Table([
            html.Tr([html.Div([html.Td(id='rec1',style={'font-weight':'bold'}),html.Img(id='img1',style={'height':'150px'})]),
                     html.Td(id='des1')]),
            html.Br(),
            html.Tr([html.Div([html.Td(id='rec2',style={'font-weight':'bold'}),html.Img(id='img2',style={'height':'150px'})]),
                     html.Td(id='des2')]),
            html.Br(),
            html.Tr([html.Div([html.Td(id='rec3',style={'font-weight':'bold'}),html.Img(id='img3',style={'height':'150px'})]),
                     html.Td(id='des3')]),
            html.Br(),
            html.Tr([html.Div([html.Td(id='rec4',style={'font-weight':'bold'}),html.Img(id='img4',style={'height':'150px'})]),
                     html.Td(id='des4')]),
            html.Br(),
            html.Tr([html.Div([html.Td(id='rec5',style={'font-weight':'bold'}),html.Img(id='img5',style={'height':'150px'})]),
                     html.Td(id='des5')]),
    ]),
])

# Define callback - 5 sets of outputs corresponding to the 5 recommendations
# Each set needs 3 outputs: the name, image URL and description of the recommended game
@app.callback(
    Output(component_id='rec1',component_property='children'),
    Output(component_id='img1',component_property='src'),
    Output(component_id='des1',component_property='children'),
    
    Output(component_id='rec2',component_property='children'),
    Output(component_id='img2',component_property='src'),
    Output(component_id='des2',component_property='children'),
    
    Output(component_id='rec3',component_property='children'),
    Output(component_id='img3',component_property='src'),
    Output(component_id='des3',component_property='children'),
    
    Output(component_id='rec4',component_property='children'),
    Output(component_id='img4',component_property='src'),
    Output(component_id='des4',component_property='children'),
    
    Output(component_id='rec5',component_property='children'),
    Output(component_id='img5',component_property='src'),
    Output(component_id='des5',component_property='children'),
    
    Input(component_id='my-input',component_property='value')
)

#for the output: gets the index of the input game, and present outputs from the recommendation system
#r = game name
#i = image URL
#u = game description
def update_output_div(input_game):
    game_id = get_index_from_name(input_game)
    # Exclude the first game (because this will be the game entered)
    # Get the ID of the recommended game, then return name, image URL and description of this game
    recID = Games_df.iloc[knn_indices_df['1'][game_id]].name
    r1 = Games_df.loc[recID]['handle']
    i1 = Game_Meta.loc[recID]['Image_URL']
    d1 = Game_Meta.loc[recID]['Description']
    
    recID = Games_df.iloc[knn_indices_df['2'][game_id]].name
    r2 = Games_df.loc[recID]['handle']
    i2 = Game_Meta.loc[recID]['Image_URL']
    d2 = Game_Meta.loc[recID]['Description']
    
    recID = Games_df.iloc[knn_indices_df['3'][game_id]].name
    r3 = Games_df.loc[recID]['handle']
    i3 = Game_Meta.loc[recID]['Image_URL']
    d3 = Game_Meta.loc[recID]['Description']
    
    recID = Games_df.iloc[knn_indices_df['4'][game_id]].name
    r4 = Games_df.loc[recID]['handle']
    i4 = Game_Meta.loc[recID]['Image_URL']
    d4 = Game_Meta.loc[recID]['Description']
    
    recID = Games_df.iloc[knn_indices_df['5'][game_id]].name
    r5 = Games_df.loc[recID]['handle']
    i5 = Game_Meta.loc[recID]['Image_URL']
    d5 = Game_Meta.loc[recID]['Description']
    
    return r1,i1,d1,r2,i2,d2,r3,i3,d3,r4,i4,d4,r5,i5,d5

if __name__ == "__main__":
    app.run_server(debug=False)

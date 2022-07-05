import streamlit as st
import pandas as pd

def load_data(year, gender):
    url = "https://en.volleyballworld.com/volleyball/competitions/vnl-" + str(year) + "/standings/" + gender + "/#round-p"
# https://images.volleyballworld.com/image/upload/f_png/t_flag/assets/flags/flag_ger
    html = pd.read_html(url, header=[0,1])
    df = html[0]
    df = df.rename(columns={"Unnamed: 1_level_0":"Teams"})
    df = df.rename(columns={"Unnamed: 0_level_1":"Number"})
    df = df.rename(columns={"Unnamed: 1_level_1":"Name"})
    return df

st.title("Volleyball Nations League")

year = st.sidebar.selectbox(
     'Ano da VNL', (2021, 2022))

gender = st.sidebar.selectbox(
     'Selecione o torneio', ('Masculino', 'Feminino'))

if gender == 'Masculino':
    standings = load_data(year, 'men')
else:
    standings = load_data(year, 'women')


teams = standings["Teams"]["Name"]

#mudando nome dos países
sigla3 = []
for name in teams:
    sigla=name[::-1]
    sigla2=slice(3)
    sigla3.append(sigla[sigla2][::-1])
    
    sliced_text = slice(-3)
    new_name = name[sliced_text]
    
    standings.replace(name, 
           new_name, 
           inplace=True)
standings.insert(2, "Abbreviation", sigla3)

standings.columns = ['rank', 'team_name', 'team_abbreviation', 'total_matches', 'matches_won', 'matches_lost', 'results_3-0', 'results_3-1', 'results_3-2', 'results_2-3', 'results_1-3', 'results_0-3', 'points', 'sets_won', 'sets_lost', 'set_ratio', 'points_won', 'points_lost', 'points_ratio']

col1, col2, col3, col4 = st.columns(4)

siglas = standings['team_abbreviation']

i = 1
coluna1 = []
coluna2 = []
coluna3 = []
coluna4 = []
for sigla in siglas:
    if i >= 1 and i <= 4: 
        link = 'https://images.volleyballworld.com/image/upload/f_png/t_flag/assets/flags/flag_' + sigla.lower()
        coluna1.append([link, sigla])
    elif i >= 5 and i <= 8: 
        link = 'https://images.volleyballworld.com/image/upload/f_png/t_flag/assets/flags/flag_' + sigla.lower()
        coluna2.append([link, sigla])
    elif i >= 9 and i <= 12: 
        link = 'https://images.volleyballworld.com/image/upload/f_png/t_flag/assets/flags/flag_' + sigla.lower()
        coluna3.append([link, sigla])
    else: 
        link = 'https://images.volleyballworld.com/image/upload/f_png/t_flag/assets/flags/flag_' + sigla.lower()
        coluna4.append([link, sigla])
    i = i + 1

with col1:
    for linha in coluna1:
        st.image(linha[0], caption=linha[1])
with col2:
    for linha in coluna2:
        st.image(linha[0], caption=linha[1])
with col3:
    for linha in coluna3:
        st.image(linha[0], caption=linha[1])
with col4:
    for linha in coluna4:
        st.image(linha[0], caption=linha[1])

st.dataframe(standings)
    
#display(standings)

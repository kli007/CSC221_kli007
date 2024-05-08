import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

from operator import itemgetter

url = "https://api.jikan.moe/v4/anime"

r = requests.get(url)
print(f'Status code: {r.status_code}')

animes_ids = r.json()
anime_dicts = []

for anime_id in animes_ids['data']:
    id = anime_id['mal_id']
    url = f'https://api.jikan.moe/v4/anime/{id}/full'
    anime_r = requests.get(url)
    print(anime_r.status_code)
    
    anime_dict = {
        'title': anime_id['title'],
        'score': anime_id['score'],
        'url': anime_id['url']
    }

    anime_dicts.append(anime_dict)

anime_dicts = sorted(anime_dicts, key=itemgetter('score'), reverse=True)
anime_links, scores= [], []

for anime in anime_dicts:
    anime_name = anime['title']
    anime_url = anime['url']
    anime_link = f"<a href='{anime_url}'>{anime_name}</a>"
    anime_links.append(anime_link)

    scores.append(anime['score'])

x_format = {"title": "Animes", 'titlefont': {'size': 24}, 'tickfont': {'size': 14}}
y_format = {"title": "Score", 'titlefont': {'size': 24}, 'tickfont': {'size': 14}}


color = {'color': 'rgb(60, 100, 150)', 'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}}
data = {'type': 'bar', 'x': anime_links, 'y': scores,  'marker': color, 'opacity': 0.6}
layout = Layout(title = "Highest Scored Anime on MyAnimeList.net", titlefont = {'size': 28}, xaxis = x_format, yaxis = y_format)

fig = {'data': data, 'layout': layout}

offline.plot(fig, filename='1.html')
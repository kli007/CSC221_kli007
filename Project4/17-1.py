import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline


url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v2+json"}
r = requests.get(url, headers = headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
print(f'Complete results: {not response_dict['incomplete_results']}')

repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)


x_format = {"title": "Repository", 'titlefont': {'size': 24}, 'tickfont': {'size': 14}}
y_format = {"title": "Stars", 'titlefont': {'size': 24}, 'tickfont': {'size': 14}}


color = {'color': 'rgb(60, 100, 150)', 'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}}
data = {'type': 'bar', 'x': repo_links, 'y': stars, 'hovertext': hover_texts,  'marker': color, 'opacity': 0.6}
layout = Layout(title = "Most-Starred Javascript Projects on Github", titlefont = {'size': 28}, xaxis = x_format, yaxis = y_format)

fig = {'data': data, 'layout': layout}

offline.plot(fig, filename='js_repos.html')
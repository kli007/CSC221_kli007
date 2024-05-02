from plotly.graph_objs import Bar, Layout
from plotly import offline


percentage_range = range(0, 101)

countries = {'Sweden': 82, 'South Korea': 81, 'U.S': 80, 'Canada': 76, 'Britain': 76, 'Germany': 76, 'Kuwait': 76, 'France': 73, 
             'Czech Rep.': 73, 'Slovakia': 73, 'Japan': 66, 'Ethiopoia': 27, 'Senegal': 27, 'Ukraine': 24, 'Morocco': 23, 'Ghana': 20,
             'Kenya': 12, 'Indoesia': 11, 'Uganda': 11, 'Pakistan': 9, 'Tanzania': 6, 'Bangladesh': 5}

x_values = []
y_values = []

for country, frequency in countries.items():
    x_values.append(country)
    y_values.append(frequency)

data = [Bar(x = x_values, y = y_values)]

x_axis_config = {'title': 'Countries', 'dtick': 1}
y_axis_config = {'title': 'Percentage'}
my_layout = Layout(title = 'Percentage of Countries that uses Computers in 2007', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='special.html')
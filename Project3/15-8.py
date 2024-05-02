from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die(8)

results = []
for roll_num in range(1_000):
    result = die_1.roll() * die_1.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_1.num_sides
poss_results = range(1, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(poss_results)
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling and multipling two D8 dice 1,000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='15-8.html')
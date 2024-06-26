from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(5_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D8 dice 5,000,000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='15-6-3.html')
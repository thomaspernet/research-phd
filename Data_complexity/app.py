import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask
import pandas as pd
import time
import os
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import ipywidgets as widgets
import plotly
from scipy.stats import chi2_contingency
from scipy.stats import chi2
plotly.offline.init_notebook_mode()
cwd = os.getcwd()
cwd

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
path_com = 'https://raw.githubusercontent.com/thomaspernet/research-phd/master/' \
'Data_complexity/complexity_world_ranking.csv'

path_ctry = 'https://raw.githubusercontent.com/thomaspernet/research-phd/' \
'master/Data_complexity/country_names.tsv'
df = pd.read_csv(path_com, sep=",", header=0)

name_ctry = pd.read_csv(path_ctry, sep="\t", header=0)
name_ctry = name_ctry.sort_values('name').reset_index()
list_countries = []
for i in name_ctry.index:
    list_countries.append({'label': name_ctry.iloc[i, 3],
	 'value': name_ctry.iloc[i, 2]})

#### functions
def dependency_test(df, ctry = 'fra'):

	df = df[df['origin'] == ctry]
	temp = pd.crosstab(index=df["q_rank_export_world"],
				   columns=df['quartile_pci'])
	# contingency table
	# interpret test-statistic
	stat, p, dof, expected = chi2_contingency(temp)
	print('dof=%d' % dof)
	prob = 0.95
	critical = chi2.ppf(prob, dof)
	# interpret p-value
	alpha = 1.0 - prob
	print('significance=%.3f, p=%.3f' % (alpha, p))
	if p <= alpha:
		result = 'Countries and Complexity raking are Dependent (reject H0).  '
	else:
		result = 'Countries and Complexity raking are ' \
		'Independent (fail to reject H0)'
	#table = temp.stack().reset_index()
	#table.columns = ['q_rank_export_world','quartile_pci','value']
	return result

def make_plot(df, ctry='fra'):
	test = df[df['origin'] == ctry]
	size = len(test)
	dimension = []

	name_p = []
	name_i = []
	size = len(test['details_description'])
	n = round(size / 10, 0)
	for i, name in enumerate(test['details_description']):
		name_i.append(i + 1)
		if i % n == 0:
			name_p.append(name)

		else:
			name_p.append(i)

	for x, name in enumerate(
		['rank_export_within_country', 'rank_pci', 'q_rank_export_world']):
		serie = "x_" + str(name)
		ticktest_n = test[name].unique().tolist()
		serie = test[name]
		#name_p = test['broad_description']
		if x == 0:
			dimension_temp = [
				dict(
					range=[1, size],
					constraintrange=[0, 10],
					tickvals=name_i,
					ticktext=name_p,
					label=name,
					values=serie)
			]
		elif np.issubdtype(serie, np.number):
			dimension_temp = [
				dict(
					range=[1, size],
					tickvals=ticktest_n,
					ticktext=ticktest_n,
					label=name,
					values=serie)
			]
		else:
			# Convert objet to int
			serie = serie.sort_values(ascending=True)
			serie_value = serie.rank(method='dense').astype(int)

			serie_vals = serie_value.unique().tolist()
			dimension_temp = [
				dict(
					tickvals=serie_vals,
					ticktext=ticktest_n,
					label=name,
					values=serie_value)
			]
		dimension.extend(dimension_temp)

		data = [
			go.Parcoords(
				line=dict(
					color=test['rank_pci'],
					colorscale='Jet',
					showscale=True,
					reversescale=True,
					cmin=0,
					cmax=size),
				dimensions=dimension)
		]
		layout = go.Layout(
    		plot_bgcolor = '#E5E5E5',
    		paper_bgcolor = '#FFFFFF'
				)
		fig = dict(data=data, layout=layout)
	return fig

figure_parallele = make_plot(df, ctry='fra')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
	html.Label('Dropdown'),
	dcc.Dropdown(
		id = 'ctry',
		options= list_countries,
		value='fra'
	),
	html.Div([
			dcc.Graph(id='plot-complexity',
			figure=figure_parallele),
			html.Div(id='my-div')
		])
	],
	 style={'columnCount': 1})


@app.callback(
	dash.dependencies.Output(component_id='my-div',
	 component_property='children'),
	[dash.dependencies.Input('ctry', 'value')])
def update_output_div(input_value):
	test = dependency_test(df, ctry = input_value)
	return 'Chi test "{}"'.format(test)

@app.callback(
	 dash.dependencies.Output('plot-complexity', 'figure'),
	[dash.dependencies.Input('ctry', 'value')])
def make_plotly(input_value):
	return make_plot(df, ctry = input_value)

if __name__ == '__main__':
	app.run_server(debug=True)

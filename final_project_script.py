import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.graph_objs as go

# Replace this with the path to your actual Excel file
# file_path = 'path_to_your_file.xlsx'

# Here, we'll simulate the DataFrame with data for n months for demonstration purposes.
n = 11  # Replace this with the actual number of months you have data for
months = pd.date_range('2021-01', periods=n, freq='M').strftime('%b')
categories = ['Groceries', 'Rent', 'Entertainment', 'Transport', 'Monthly Subscriptions', 'Pet Care', 'Out of Town Travel', 'Savings/Investments', 'Miscellaneous']

# Random data generation for demonstration purposes.
np.random.seed(0)  # For reproducibility
data = {category: np.random.randint(200, 2000, size=n) for category in categories}
data['Month'] = months
df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Amount')
df_melted['Month_Num'] = df_melted['Month'].astype('category').cat.codes + 1

# Perform linear regression and extrapolate the values for the next month (n+1).
extrapolated_values = []
for category in categories:
    category_data = df_melted[df_melted['Category'] == category]
    X = category_data[['Month_Num']]
    y = category_data['Amount']
    model = LinearRegression().fit(X, y)
    predicted_value = model.predict([[n+1]])[0]
    extrapolated_values.append((category, predicted_value))

# Add the extrapolated values to the original DataFrame for plotting
df_extrapolated = pd.DataFrame(extrapolated_values, columns=['Category', 'Amount'])
next_month = pd.date_range('2021-01', periods=n+1, freq='M').strftime('%b')[-1]
df_extrapolated['Month'] = f'{next_month} (Extrapolated)'
df_combined = pd.concat([df_melted, df_extrapolated])

area_fig = go.Figure()
# Add traces for each category
for category in categories:
    category_data = df_combined[df_combined['Category'] == category]
    area_fig.add_trace(go.Scatter(
        x=category_data['Month'], 
        y=category_data['Amount'], 
        name=category,
        mode='lines', 
        line=dict(width=0.5, color='blue'),
        stackgroup='one'  # define stack group
    ))
# Add a trace for the extrapolated values with a dashed line
for category in df_extrapolated['Category']:
    category_data = df_extrapolated[df_extrapolated['Category'] == category]
    area_fig.add_trace(go.Scatter(
        x=category_data['Month'], 
        y=category_data['Amount'], 
        name=f'{category} (Extrapolated)',
        mode='lines', 
        line=dict(width=2, dash='dash', color='red')
    ))
area_fig.update_layout(
    title='Monthly Expenses by Category with Extrapolated Values',
    xaxis=dict(title='Month'),
    yaxis=dict(title='Amount')
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='stacked-bar-chart',
        figure=px.bar(df_combined, x='Month', y='Amount', color='Category', title='Monthly Expenses by Category', barmode='stack')
    ),
    dcc.Graph(
        id='pie-chart',
        figure=px.pie(df_combined[df_combined['Month'] != f'{next_month} (Extrapolated)'], values='Amount', names='Category', title='Expense Distribution')
    ),
    dcc.Graph(
    id='area-chart',
    figure=area_fig
),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df_combined, x='Category', y='Amount', color='Month', size='Amount', hover_name='Category')
    ),
    dcc.Graph(
        id='extrapolated-values-bar-chart',
        figure=px.bar(
            df_extrapolated,
            x='Category',
            y='Amount',
            title=f'Extrapolated Expenses for {next_month}',
            pattern_shape='Category', pattern_shape_sequence=['x']
        )
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

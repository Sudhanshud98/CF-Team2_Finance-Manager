# CF-Team2_Finance-Manager

The Python package created by us is called  'FinanceManager'. It consists of a dash web app to manage your finances which is a Python web framework to run interactive applications. Dash is written on the top of Flask, Plotly. js and React. js. With Dash, you don't have to learn HTML, CSS, and Javascript to create interactive dashboards, you only need Python. This app will run on the localhost of your machine on port 8050. 
To install the package simply use the following command -
<br />
<br /> 
pip install -i https://test.pypi.org/simple/ FinanceManager
<br />
<br />
The FinanceManager package allows users to generate various data visualization plots of your data like - stacked bar chart, pie chart, area chart, scatter plots, and extrapolated bar chart. As you can see by the name, the extrapolated bar chart allows the user to see the future predicted values of the expenditure based on a simple linear regression algorithm that we have incorporated into the package while the other plots allow the users to see the data in a more visually understandable way. This allows the users to take a deep dive into their finances and see the extrapolated values to further manage their finances in a simple yet efficient way.
<br />
<br />
The package is deployed on [TestPyPi](https://test.pypi.org/) which is where you need to first create an account, set up 2-factor authentication and generate recovery codes to recover the account if needed. After that is set, you need to set a tree structure for your project working like we have where we created the package name folder called FinanceManager in the root of the repository, which houses the compressed files after they get generated and a setup.py file that's responsible for setting up the entry point in the application and versioning of the application. 
In this package name folder we need yet another folder called finance_manager_app where we have the python script and the __init_\_.py file which are responsible for generating the plots and essentially running the package.  
<br/>
Final set of Pre-requisites for the developer's machine are the twine and setuptools package. After that is done, you need to generate a distribution for the app and then upload it to [TestPyPi](https://test.pypi.org/). At this point, when we use the twine command to deploy the package we need a set of credentials prompted at CLI. The username is __token_\_(double underscores on either side) and password is the token that you generate from TestPyPi.
<br/>
<br/>
References - <br/>
https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4 <br />
https://pysteps.readthedocs.io/en/stable/developer_guide/pypi.html


from setuptools import setup, find_packages

setup(
    name='FinanceManager',
    version='0.5',
    packages=find_packages(),
    install_requires=[
        'dash',
        'plotly'
        ],
    url='https://test.pypi.org/project/FinanceManager/',
    entry_points={
        'console_scripts': [
            'finance_manager_app = FinanceManager.finance_manager_app.final_project_script:app.run_server',
        ],
    },
)

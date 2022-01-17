# dev10-census-api-assessment

An exploration of data from the Census Bureau's 2019 Annual Business Survey

### Data Source

Data on the 2019 ABS was obtained from an API call. Documentation on the APIs can be found [here](https://www.census.gov/data/developers/data-sets/abs.2019.html)

### Files Included

- All visualizations created for the final report can be found in the [visualizations](visualizations) folder, and the code to create those visualizations is found throughout the Jupyter notebook files (extension `.ipynb`)
- The project report is in [project_report.pdf](project_report.pdf) (note: the [project_report.docx](project_report.docx) file does not contain the most current version of the report)
- The ETL report is in [ETL_report.docx](ETL_report.docx) and the ETL is performed in [GeneralETL.ipynb](GeneralETL.ipynb)
- [GeneralETL_PyFile.py](GeneralETL_PyFile.py) and [TechImpactCensusData.xlsx](TechImpactCensusData.xlsx) both contain the data after ETL has been performed. Jupyter notebooks can obtain the clean data from either one

### How to Use

If you are only interested in reading our final report, read [](). If you want to run our ETL code and investigate the data yourself:
1. Download [GeneralETL.ipynb](GeneralETL.ipynb) (or [GeneralETL_PyFile.py](GeneralETL_PyFile.py), both will perform the ETL)
2. In the same folder, create a file named `config.py`
3. Obtain an API key by following the instructions [here](https://www.census.gov/data/developers/guidance/api-user-guide.Help_&_Contact_Us.html)
4. In `config.py`, write the line `api_key = "your_api_key_here"` and save it
5. The ETL file will now run without errors

### Project Contributors

- Scott Partacz
- Colin Beveridge
- Abbey Guilliat
- Lucas Stefanic

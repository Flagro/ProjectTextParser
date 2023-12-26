import pandas as pd
from projecttextexcel import get_df

from ..base_parser import TableParser


class ExcelParser(TableParser):
    def get_pandas_dataframe(self, path):
        output = get_df(path, prettify_output=False)
        result = []
        for sheet_name, dfs in output.items():
            for df in dfs:
                result.append((df, {'sheet_name': sheet_name}))
        return result

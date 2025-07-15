
import pandas as pd
import pytest

def test_dataframe_creation():
    """Test DataFrame creation from a dictionary."""
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pd.DataFrame(data)
    assert df.shape == (3, 2)

def test_series_creation():
    """Test Series creation from a list."""
    data = [1, 2, 3]
    series = pd.Series(data)
    assert len(series) == 3

def test_merge():
    """Test merging two DataFrames."""
    df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame({'col1': [1, 3], 'col3': [5, 6]})
    merged_df = pd.merge(df1, df2, on='col1', how='inner')
    assert merged_df.shape == (1, 3)

def test_groupby():
    """Test grouping a DataFrame."""
    df = pd.DataFrame({'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    grouped_df = df.groupby('col1').sum()
    assert grouped_df.shape == (2, 1)

def test_pivot_table():
    """Test creating a pivot table."""
    df = pd.DataFrame({'col1': [1, 1, 2], 'col2': ['A', 'B', 'A'], 'col3': [3, 4, 5]})
    pivot_table = pd.pivot_table(df, values='col3', index='col1', columns='col2')
    assert pivot_table.shape == (2, 2)

def test_read_csv():
    """Test reading from a CSV string."""
    csv_data = "col1,col2\n1,2\n3,4"
    df = pd.read_csv(csv_data)
    assert df.shape == (2, 2)

def test_to_datetime():
    """Test converting a string to datetime."""
    date_str = "2024-03-01"
    date_time = pd.to_datetime(date_str)
    assert date_time.year == 2024

def test_fillna():
    """Test filling NaN values."""
    df = pd.DataFrame({'col1': [1, None, 3]})
    df.fillna(2, inplace=True)
    assert df['col1'][1] == 2

def test_dropna():
    """Test dropping rows with NaN values."""
    df = pd.DataFrame({'col1': [1, None, 3]})
    df.dropna(inplace=True)
    assert df.shape == (2, 1)

def test_concat():
    """Test concatenating two DataFrames."""
    df1 = pd.DataFrame({'col1': [1, 2]})
    df2 = pd.DataFrame({'col1': [3, 4]})
    concatenated_df = pd.concat([df1, df2])
    assert concatenated_df.shape == (4, 1)
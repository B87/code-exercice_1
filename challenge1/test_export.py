from export import generate_urls_for_a_day, merge_into_df, request_files_mock
import datetime

def test_url_gen():
    result = generate_urls_for_a_day(datetime.datetime(2019,10,20))
    assert len(result) == 24
    assert result[0] == 'https://api.localytic.cm/v1/exports/analytics/logs/2019/10/20/00'
    assert result[23] == 'https://api.localytic.cm/v1/exports/analytics/logs/2019/10/20/23'

def test_merge_into_files():
    df = merge_into_df(request_files_mock(''))
    assert df.columns.all(['manu.id', 'manu.value', 'menu.menuitem'])
    assert len(df.columns) == 3
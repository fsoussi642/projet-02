import pandas as pd
from report_automation.processor import clean_data,kpis

def test_clean_data_filters_invalid_rows_and_duplicates():
    df=pd.DataFrame([{"customer_id":" A ","amount":"10","date":"2026-01-01"},{"customer_id":" A ","amount":"10","date":"2026-01-01"},{"customer_id":"","amount":"oops","date":"bad"}])
    out,stats=clean_data(df); assert len(out)==1 and out.iloc[0].customer_id=="A" and stats["valid_rows"]==1

def test_kpis():
    df=pd.DataFrame([{"customer_id":"A","amount":10},{"customer_id":"B","amount":20}])
    assert kpis(df)=={"transactions":2,"revenue":30.0,"customers":2,"average_order":15.0}

def test_empty_kpis():
    assert kpis(pd.DataFrame(columns=["customer_id","amount"]))["transactions"]==0

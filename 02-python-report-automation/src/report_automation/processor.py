from pathlib import Path
import pandas as pd

REQUIRED = {"customer_id", "amount", "date"}

def load_csv(path: str | Path) -> pd.DataFrame:
    """Charge le CSV et vérifie la présence des champs obligatoires."""
    p = Path(path)
    if not p.is_file(): raise FileNotFoundError(f"Fichier introuvable : {p}")
    df = pd.read_csv(p)
    missing = REQUIRED - set(df.columns)
    if missing: raise ValueError(f"Colonnes manquantes : {', '.join(sorted(missing))}")
    return df

def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Normalise les champs, élimine doublons et lignes invalides, puis trace les volumes."""
    before = len(df); out = df.copy()
    out["customer_id"] = out["customer_id"].astype("string").str.strip()
    out["amount"] = pd.to_numeric(out["amount"], errors="coerce")
    out["date"] = pd.to_datetime(out["date"], errors="coerce", utc=True)
    out = out.drop_duplicates()
    valid = out.customer_id.notna() & out.customer_id.ne("") & out.amount.notna() & out.amount.ge(0) & out.date.notna()
    out = out.loc[valid].reset_index(drop=True)
    return out, {"input_rows":before,"valid_rows":len(out),"rejected_rows":before-len(out)}

def kpis(df: pd.DataFrame) -> dict:
    """Calcule quelques indicateurs simples sur les lignes validées."""
    if df.empty: return {"transactions":0,"revenue":0.0,"customers":0,"average_order":0.0}
    return {"transactions":int(len(df)),"revenue":round(float(df.amount.sum()),2),"customers":int(df.customer_id.nunique()),"average_order":round(float(df.amount.mean()),2)}

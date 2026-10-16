import argparse, json
from pathlib import Path
from .processor import load_csv, clean_data, kpis

def main():
    """Commande : report-automation fichier.csv --output dossier."""
    parser=argparse.ArgumentParser(description="Nettoyage CSV et rapport KPI")
    parser.add_argument("input"); parser.add_argument("--output",default="output"); args=parser.parse_args()
    cleaned,quality=clean_data(load_csv(args.input)); summary={"quality":quality,"kpis":kpis(cleaned)}
    dest=Path(args.output); dest.mkdir(parents=True,exist_ok=True)
    cleaned.to_csv(dest/"cleaned_data.csv",index=False)
    (dest/"report.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding="utf-8")
    print(f"Rapport écrit dans {dest}")
if __name__=="__main__": main()

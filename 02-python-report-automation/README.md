# Report Automation — Python
CLI de traitement CSV : validation des colonnes, normalisation, suppression des doublons exacts, rejet des lignes invalides et export de KPI JSON.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
report-automation sample_data.csv --output output
pytest
```
Résultats dans `output/cleaned_data.csv` et `output/report.json`. Règles attendues : `customer_id`, `amount`, `date`. Les données d'exemple sont fictives. Améliorations : schéma configurable, SQLite, export Excel, planification cron et alertes.

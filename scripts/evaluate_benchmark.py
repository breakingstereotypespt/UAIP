"""Basic benchmark evaluator for markdown case files and CSV output."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
RESULTS_FILE = ROOT / "benchmarks" / "results" / "sample-results.csv"

def read_results():
    with RESULTS_FILE.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def summarize(results):
    baseline = sum(int(r["baseline_score"]) for r in results) / len(results)
    uaip = sum(int(r["uaip_score"]) for r in results) / len(results)
    print(f"Average baseline score: {baseline:.2f}")
    print(f"Average UAIP score: {uaip:.2f}")
    print(f"Average improvement: {uaip - baseline:.2f}")

if __name__ == "__main__":
    summarize(read_results())

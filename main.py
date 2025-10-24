import argparse
import pandas as pd
from analyzer import analyze_excel
from summarizer import generate_summary

def main():
    parser = argparse.ArgumentParser(description="KI-Auswertung für Excel-Dateien")
    parser.add_argument("--file", required=True, help="Pfad zur Excel-Datei")
    args = parser.parse_args()

    # Excel-Datei laden
    df = pd.read_excel(args.file)
    print(f"✅ Datei geladen: {args.file}")

    # Daten analysieren
    analysis = analyze_excel(df)
    print("📊 Analyse abgeschlossen.")

    # KI-Zusammenfassung generieren
    summary = generate_summary(analysis)
    print("\n🧠 KI-Zusammenfassung:\n")
    print(summary)

if __name__ == "__main__":
    main()

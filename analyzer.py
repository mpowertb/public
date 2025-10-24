def analyze_excel(df):
    numeric_cols = df.select_dtypes(include="number").columns
    analysis = {}

    for col in numeric_cols:
        stats = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "std": df[col].std(),
            "min": df[col].min(),
            "max": df[col].max(),
        }
        analysis[col] = stats

    return analysis

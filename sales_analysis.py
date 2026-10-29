
import pandas as pd

# Load dataset
df = pd.read_csv("amazon_transformed.csv")

print("AMAZON SALES ANALYSIS")
print("--------------------")

# Total products
print("\nTotal Products:", len(df))

# Average rating
if "rating" in df.columns:
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    print("Average Rating:", round(df["rating"].mean(), 2))

# Category analysis
if "category" in df.columns:
    print("\nTop 10 Categories:")
    print(df["category"].value_counts().head(10))

# Discount analysis
if "discount_percentage" in df.columns:
    df["discount_percentage"] = pd.to_numeric(
        df["discount_percentage"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip(),
        errors="coerce"
    )

    avg_discount = df["discount_percentage"].mean()

    if pd.notna(avg_discount):
        print("\nAverage Discount (%):", round(avg_discount, 2))
    else:
        print("\nAverage Discount: No valid numeric values found")

# Price analysis
if "discounted_price" in df.columns:
    df["discounted_price"] = pd.to_numeric(
        df["discounted_price"].astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.replace("Rs.", "", regex=False)
        .str.strip(),
        errors="coerce"
    )

    print("\nAverage Discounted Price:",
          round(df["discounted_price"].mean(), 2))

# Top-rated products
if "rating" in df.columns and "product_name" in df.columns:
    print("\nTop 10 Rated Products:")
    print(
        df[["product_name", "rating"]]
        .dropna()
        .sort_values("rating", ascending=False)
        .head(10)
        .to_string(index=False)
    )

# Save analysis report
df.describe(include="all").to_csv("sales_analysis_report.csv")

print("\nAnalysis completed successfully!")
print("Report saved as sales_analysis_report.csv")

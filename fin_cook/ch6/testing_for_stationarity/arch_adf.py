from arch.unitroot import ADF
import nasdaqdatalink

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

# Download the monthly US unemployment rate from the years 2010 to 2019:
df = (
    nasdaqdatalink.get(dataset="FRED/UNRATENSA",
                       start_date="2010-01-01",
                       end_date="2019-12-31")
        .rename(columns={"Value": "unemp_rate"})
)

adf = ADF(df["unemp_rate"])
print(adf.summary().as_text())

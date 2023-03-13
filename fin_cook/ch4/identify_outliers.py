def identify_outliers(df, column, window_size, n_sigmas):
    """identifying outliers using rolling statistics
    returns pd.Series containing boolean flags indicating whether a given observation is an outlier or not
    """

    df = df[[column]].copy()
    df_rolling = df.rolling(window=window_size) \
        .agg(["mean", "std"])
    df_rolling.columns = df_rolling.columns.droplevel()
    df = df.join(df_rolling)
    df["upper"] = df["mean"] + n_sigmas * df["std"]
    df["lower"] = df["mean"] - n_sigmas * df["std"]
    return (df[column] > df["upper"]) | (df[column] < df["lower"])

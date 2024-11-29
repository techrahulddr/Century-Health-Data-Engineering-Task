def merge_datasets(datasets):
    """Merge all datasets into a master table."""
    master_table = datasets["patients"].merge(
        datasets["encounters"], on="id", how="inner"
    ).merge(
        datasets["symptoms"], on="id", how="inner"
    )
    return master_table


from great_tables import GT, html


def beau_tableau(df, titre):
    """
    Transforme une base de données en beau tableau.
    """
    tableau = (
        GT(df)
        .tab_header(title=html(f"<b>{titre}</b>"))
    )

    cols_numeriques = df.select_dtypes(include=['number']).columns.tolist()

    if cols_numeriques:
        tableau = tableau.fmt_number(
            columns=cols_numeriques,
            decimals=2,
            sep_mark=" "
        )

    tableau = (
        tableau.tab_options(
            table_font_size="14px",
            column_labels_font_weight="bold",
            table_border_top_style="solid",
            table_border_top_width="3px",
            table_border_top_color="#444444"
        )
        .cols_align(align="center")
    )
    return tableau

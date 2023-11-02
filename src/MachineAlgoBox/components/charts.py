#Authot github.com/tushar2704
##############################################################################################################
#Importing required library
##############################################################################################################
import random
# import duckdb
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import streamlit as st
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
########################################################################################################

def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": prefix,
                "suffix": suffix,
                "font.size": 28,
            },
            title={
                "text": label,
                "font": {"size": 24},
            },
        )
    )

    if show_graph:
        fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor=color_graph,
                line={
                    "color": color_graph,
                },
            )
        )

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        margin=dict(t=30, b=0),
        showlegend=False,
        plot_bgcolor="white",
        height=100,
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_gauge(
    indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound
):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={
                "suffix": indicator_suffix,
                "font.size": 26,
            },
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1},
                "bar": {"color": indicator_color},
            },
            title={
                "text": indicator_title,
                "font": {"size": 28},
            },
        )
    )
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        height=200,
        margin=dict(l=10, r=10, t=50, b=10, pad=8),
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_top_right():
    sales_data = duckdb.sql(
        f"""
        WITH sales_data AS (
            UNPIVOT ( 
                SELECT 
                    Scenario,
                    business_unit,
                    {','.join(all_months)} 
                    FROM df 
                    WHERE Year='2023' 
                    AND Account='Sales' 
                ) 
            ON {','.join(all_months)}
            INTO
                NAME month
                VALUE sales
        ),

        aggregated_sales AS (
            SELECT
                Scenario,
                business_unit,
                SUM(sales) AS sales
            FROM sales_data
            GROUP BY Scenario, business_unit
        )
        
        SELECT * FROM aggregated_sales
        """
    ).df()

    fig = px.bar(
        sales_data,
        x="business_unit",
        y="sales",
        color="Scenario",
        barmode="group",
        text_auto=".2s",
        title="Sales for Year 2023",
        height=400,
    )
    fig.update_traces(
        textfont_size=12, textangle=0, textposition="outside", cliponaxis=False
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_bottom_left():
    sales_data = duckdb.sql(
        f"""
        WITH sales_data AS (
            SELECT 
            Scenario,{','.join(all_months)} 
            FROM df 
            WHERE Year='2023' 
            AND Account='Sales'
            AND business_unit='Software'
        )

        UNPIVOT sales_data 
        ON {','.join(all_months)}
        INTO
            NAME month
            VALUE sales
    """
    ).df()

    fig = px.line(
        sales_data,
        x="month",
        y="sales",
        color="Scenario",
        markers=True,
        text="sales",
        title="Monthly Budget vs Forecast 2023",
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)


def plot_bottom_right():
    sales_data = duckdb.sql(
        f"""
        WITH sales_data AS (
            UNPIVOT ( 
                SELECT 
                    Account,Year,{','.join([f'ABS({month}) AS {month}' for month in all_months])}
                    FROM df 
                    WHERE Scenario='Actuals'
                    AND Account!='Sales'
                ) 
            ON {','.join(all_months)}
            INTO
                NAME year
                VALUE sales
        ),

        aggregated_sales AS (
            SELECT
                Account,
                Year,
                SUM(sales) AS sales
            FROM sales_data
            GROUP BY Account, Year
        )
        
        SELECT * FROM aggregated_sales
    """
    ).df()

    fig = px.bar(
        sales_data,
        x="Year",
        y="sales",
        color="Account",
        title="Actual Yearly Sales Per Account",
    )
    st.plotly_chart(fig, use_container_width=True)






















































































































































































































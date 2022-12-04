import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
def plot_sankey_chart(expenses,incomes):
    # Create sankey chart
    label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
    source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
    target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
    value = list(incomes.values()) + list(expenses.values())

    # Data to dict, dict to sankey
    link = dict(source=source, target=target, value=value)
    node = dict(label=label, pad=20, thickness=30, color="#E694FF")
    data = go.Sankey(link=link, node=node)

    # Plot it!
    fig = go.Figure(data)
    fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
    st.plotly_chart(fig, use_container_width=True)

def plot_pie_chart(expenses,remaining_budget):
    label = list(expenses.keys()) + ["Remaining Budget"]
    values = list(expenses.values()) + [remaining_budget]

    #Create pie chart
    fig = px.pie(names = label, values=values)
    st.plotly_chart(fig,use_container_width=True)


def plot_bar_chart(expenses):
    label = list(expenses.keys())
    values = list(expenses.values())
    fig, ax = plt.subplots()
    ax.bar(label, values,color='#e694ff')
    ax.set_facecolor("#0e1117")
    plt.xticks(rotation='vertical')
    st.pyplot(fig)


    

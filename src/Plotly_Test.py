import plotly.graph_objects as go
import plotly.express as px


def QuickTable():

    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'

    fig = go.Figure(data=[go.Table(
      header=dict(
        values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'],
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left','center'],
        font=dict(color='white', size=12)
      ),
      cells=dict(
        values=[
          ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
          [1200000, 20000, 80000, 2000, 12120000],
          [1300000, 20000, 70000, 2000, 130902000],
          [1300000, 20000, 120000, 2000, 131222000],
          [1400000, 20000, 90000, 2000, 14102000]],
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
        align = ['left', 'center'],
        font = dict(color = 'darkslategray', size = 11)
        ))
    ])

    # #fig.show()
    # x= fig.write_image("images/fig1.png")

    return fig.to_image(format="png")


if __name__ == "__main__":
    from IPython.display import Image

    Image(QuickTable())
    

    # pic = QuickTable()
    # pic.show()

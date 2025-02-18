"""Criando pipelines."""
from datetime import date
from rocketry import Rocketry
from rocketry.args import Arg

app = Rocketry()


@app.param()
def data_de_hoje():
    return date.today()


@app.task('daily')
def tarefa(dia_corrente=Arg(data_de_hoje)):
    print(dia_corrente)


app.run()

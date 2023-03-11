# cli-todo

cli-todo em Python utilizando as bibliotecas rich e typer

Projeto adaptado de [Patrick Loeber](https://github.com/patrickloeber?tab=repositories)

#Instalação

```pip install -r requirements.txt```

#Exibir tabela

```python todocli.py show ```

#Adicionar tarefa

```python todocli.py add <tarefa> <categoria>```

```python todocli.py add "Fazer compras" "Casa"```

#Remover tarefa

```python todocli.py delete <id>```

```python todocli.py delete 1```

#Marcar como completa

```python todocli.py complete <id>```

```python todocli.py complete 1```

#Ver apenas uma categoria de tarefas

```python todocli.py show <categoria>```

```python todocli.py show "Casa"```

#Ajuda

```python todocli.py --help```

# desafio-load-balance

# Solução:
Criar um algoritmo guloso que à medida que apareça um usuário o aloque em um servidor, verificando qual servidor tem o máximo ttask em relação aos outros, caso não seja possível
alocar em um sevidor com outros usuários, cria-se um novo servidor e manda a tarefa do usuário ser processada por esse novo servidor.

## Requerimentos 
O projeto necessita de pip - gerencioador de pacotes e utilizar ubuntu.

# Rodando o Projeto
Clone esse projeto em sua máquina:
```bash
$ git clone https://github.com/Mario-Guilherme/desafio-load-balance.git
```

Entre na pasta do projeto usando o comando:
```bash
$ cd desafio-load-balance
```

Instale Pipenv:
```bash
$ pip install --user pipenv
```
Instale as dependências:
```bash
$ pipenv install Pipfile
```

Executando o projeto:
```bash
$ sh build.sh
```


# Rodando os Testes:
```bash
$ sh test.sh
```

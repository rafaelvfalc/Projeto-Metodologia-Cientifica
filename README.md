# Projeto Metodologia Cientifica 2017.1
Investigação empírica do problema de ordenação para grandes volumes de dados numéricos

# Equipe: 
	- Rafael Falcão
    - Catarina Silva

# Configuração

Descompacte o arquivo

Vá para o diretório principal do projeto

	$ cd Projeto-Metodologia-Cientifica

Crie um virtual environment (Opcional):

	$ virtualenv venv

Se conecte ao seu virtual environment (Opcional caso não tenha realizado o passo acima):

	$ source venv/bin/activate

Instale os requirements:

    $ pip install -r requirements.txt

# Como usar?

Entre no diretório do projeto (Projeto-Metodologia-Cientifica) e rode o comando seguinte:

    $ ./ordenar algorithm num_replications input.txt output.csv

Sendo:

- algortihm: O algoritmo que se quer utilizar na experimentação. (Opções: bubblesort, shellsort, mergesort, quicksort)

- num_replications: O número de replicações que o experimento deve conter dentro do output.txt

- input.txt: Arquivo com números desordenados que irá ser utilizado para a realização da experimentação

- output.txt: Arquivo com os resultados da experimentação. Estarão contido nesse file as seguintes informações:

    * total time: O tempo total para ser rodado o algoritmo escolhido usando o input file

    * algorithm: Algoritmo usado na experimentação

    * file size: Tamanho do input file usado na experimentação

    * memory usage: Memória usada na realização do algoritmo escolhido usando o input file

    Obs: O nome do arquivo que conterá o resultado dos experimentos deve ser único, ou seja, nenhum outro file no diretório 'results' deve conter o mesmo nome.

O resultado do seu experimento estará contido na pasta 'results' com o nome informado pela variável 'output.txt'
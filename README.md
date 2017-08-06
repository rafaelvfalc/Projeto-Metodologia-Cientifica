# Projeto Metodologia Cientifica 2017.1
Investigação empírica do problema de ordenação para grandes volumes de dados numéricos

# Equipe: 
	- Rafael Falcão
    - Catarina Silva

# Configuração

Crie um virtual environment (Opcional):

	$ virtualenv venv

Instale os requirements:

    $ pip install -r requirements.txt

# Como usar?

Entre no diretório do projeto (Projeto-Metodologia-Cientifica) e rode o comando seguinte:

    $ ./ordenar algorithm input.txt output.txt

Sendo:
	- algortihm: O algoritmo que se quer utilizar na experimentação. (Opções: bubblesort, shellsort, mergesort, quicksort)

	- input.txt: Arquivo com números desordenados que irá ser utilizado para a realização da experimentação

	- output.txt: Arquivo com os resultados da experimentação. Estarão contido nesse file as seguintes informações:

    	* total time: O tempo total para ser rodado o algoritmo escolhido usando o input file

    	* algorithm: Algoritmo usado na experimentação

    	* file size: Tamanho do input file usado na experimentação

    	* memory usage: Memória usada na realização do algoritmo escolhido usando o input file


Os exemplos de python vão ficar organizados em notebooks nessa pasta chamados exemplo_vinculos.ipynb, exemplo_funcoes.ipynb, etc.
o arquivo python_tutor_magic.py contém o módulo com comando mágico para converter os exemplos em URL para rodar no site python tutor
a primeira célula de cada notebook deve rodar o comando import python_tutor_magic para permitir o uso do comando mágico
então, usando o comando mágico %%pythontutor na primeira linha de qualquer celula,
o notebook vai gerar a URL para o site do python tutor em vez de rodar o código do exemplo localmente.

# Lights Out: Uma Perspectiva de Álgebra Linear

## Introdução

"Lights Out" é um quebra-cabeça matemático que se tornou popular devido à sua combinação única de simplicidade e complexidade. Aqui vamos explorar o jogo através de conceitos de álgebra linear, demonstrando como a matemática pode ser aplicada para resolver jogos de forma sistemática.

Jogue "Lights Out" online: [Lights Out](https://www.logicgamesonline.com/lightsout/).

## O que é o Lights Out?

"Lights Out" é um jogo baseado em um tabuleiro 5x5 onde cada célula possui uma luz que pode estar acesa (1) ou apagada (0). O objetivo é apagar todas as luzes.

## Regras do Jogo

1. Ao clicar em uma célula, essa célula e as adjacentes (acima, abaixo, esquerda, direita) alternam entre aceso e apagado.
2. O jogador deve usar essa mecânica para apagar todas as luzes do tabuleiro.

## Análise do Jogo

Representamos o tabuleiro como uma matriz 5x5 de zeros e uns. Aqui está um exemplo de um tabuleiro inicial e o efeito de um clique na célula (0,0):

Estado inicial:

$$
\begin{bmatrix}
1 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
\end{bmatrix}
$$

Após clicar em (0, 0):

$$
\begin{bmatrix}
0 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
\end{bmatrix}
$$

Clicar duas vezes em uma célula equivale a não clicar, simplificando as possíveis entradas de solução para 0s e 1s.

## Modelagem Matemática

Modelamos o problema como um sistema linear $Ax = b \mod 2$, onde $A$ é a matriz de cliques e $b$ o vetor estado das luzes. A ideia da modelagem é que dado um tabuleiro apagado uma sequencia de cliques foram feitas para chegar no tabuleiro atual.

### Construção da Matriz $A$

A matriz $A$ é construída considerando cada célula do tabuleiro como parte de um vetor de 25 entradas. Cada linha em $A$ representa o efeito de um clique em uma célula particular, ajustando seu estado e o das adjacências.

Exemplo de linha em $A$ para o clique em $b_0$:

$$
\begin{bmatrix}
1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \cdots & 0
\end{bmatrix}
$$

### Solubilidade do Tabuleiro

Para determinar se um tabuleiro é solucionável:

- **Determinante de $A$**: Se diferente de zero, o tabuleiro é solucionável.
- **Posto de $A$**: Se completo, todas as configurações de luz são alcançáveis.

### Propriedades da Matriz $A$

- **Simetria**: $A$ é simétrica ($A = A^T$).
- **Binariedade**: Aceita apenas 0s e 1s.
- **Diagonal Principal**: Sempre 1s, pois um clique afeta a célula clicada.

## Complexidade Algorítmica

- **Montagem de $A$**: $O(n^4)$.
- **Gauss-Jordan mod 2**: $O(n^6)$ para simplificar $A$.
- **Substituição Reversa**: $O(n^4)$ para encontrar a solução.

## Conclusão

Concluímos que o jogo pode ser resolvido de forma sistemática através de álgebra linear, o que permite encontrar soluções para qualquer tabuleiro de usando o menor número de cliques.

## Referências

- [Wikipedia sobre Lights Out](<https://en.wikipedia.org/wiki/Lights_Out_(game)>)
- [Análise Matemática do Jogo](https://web.archive.org/web/20140815155142/https://www.math.ksu.edu/math551/math551a.f06/lights_out.pdf)
- [Código e Discussões Técnicas](https://www.keithschwarz.com/interesting/code/?dir=lights-out)
- [Tutorial e Estratégias](https://www.logicgamesonline.com/lightsout/tutorial.html)

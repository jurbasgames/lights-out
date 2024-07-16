# Lights Out

Uma análise do jogo "Lights Out" utilizando algebra linear.

## O que é o Lights Out?

Lights Out é um jogo quebra cabeça que é formado por um tabuleiro 5x5 onde cada célula representa uma luz, cada luz pode ser acesa ou apagada e o objetivo do jogo é apagar todas as luzes do tabuleiro.

Podemos jogar Lights Out online no link: [Lights Out](https://www.logicgamesonline.com/lightsout/)

## Regras do jogo

O jogo tem as seguintes regras:

1. Cada célula do tabuleiro pode ser acesa ou apagada.
2. Ao clicar em uma célula, a célula clicada e as células adjacentes (acima, abaixo, esquerda e direita) mudam para o estado oposto, ou seja se estiver apagada ela acende e se estiver acesa ela apaga.
3. O objetivo do jogo é apagar todas as luzes do tabuleiro.

## Análise do jogo

Um tabuleiro pode ser representado como uma matriz 5x5 de 0s e 1s, onde 0 representa uma luz apagada e 1 representa uma luz acesa.

$$
\begin{bmatrix}
1 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
\end{bmatrix}
$$

Por exemplo, clicando na célula (0, 0) vamos ter o seguinte tabuleiro:

$$
\begin{bmatrix}
0 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
\end{bmatrix}
$$

Antes de resolver o jogo, podemos notar que clicar duas vezes na mesma célular é a mesma coisa que não clicar, portanto só assumimos valores 0 ou 1 nas entradas da matriz.

## Modelagem do problema

Podemos modelar o problema como um sistema linear na forma `Ax = b`, onde `A` é a matriz de cliques, `b` é a matriz de estados das luzes do tabuleiro inicial na forma de vetor e `x` é o matriz de cliques que devemos fazer para apagar todas as luzes do tabuleiro em forma de vetor.

Como a operação é binária (clicar ou não clicar), podemos representar como um sistema mod 2.

$$ Ax = b \mod 2 $$

### Construindo a matriz `A`

Para construi-la vamos considerar que o tabuleiro seja um vetor de 25 células e cada linha da matriz `A` representa um clique em uma célula.

Os índices do tabuleiro são:

$$
\begin{bmatrix}
b_0 & b_1 & b_2 & b_3 & b_4 \\
b_5 & b_6 & b_7 & b_8 & b_9 \\
b_{10} & b_{11} & b_{12} & b_{13} & b_{14} \\
b_{15} & b_{16} & b_{17} & b_{18} & b_{19} \\
b_{20} & b_{21} & b_{22} & b_{23} & b_{24} \\
\end{bmatrix}
$$

Vetor do tabuleiro vai ficar:

$$
\begin{bmatrix}
b_0 & b_1 & b_2 & b_3 & b_4 & b_5 & b_6 & b_7 & b_8 & b_9 & b_{10} & b_{11} & b_{12} & b_{13} & b_{14} & b_{15} & b_{16} & b_{17} & b_{18} & b_{19} & b_{20} & b_{21} & b_{22} & b_{23} & b_{24}
\end{bmatrix}^T
$$

Portanto, cada linha de `A` vai ser um vetor de 25 células inicialmente preenchidas com zeros no tabuleiro representando o efeito do clique naquela célula. Por exemplo a primeira linha de `A` representa o clique na célula $b_0$ do tabuleiro.
Então a primeira linha de `A` vai ser:

$$
\begin{bmatrix}
1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Montando `A` temos:

$$
A = \begin{bmatrix}
1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 \\
\end{bmatrix}
$$

### Simplificando a matriz `A`

Para resolver o jogo, precisamos de um vetor `x` que `Ax = b` mod 2,ou seja, `Ax - b = 0` mod 2. Mas antes podemos aplicar Gauss-Jordan mod 2 para simplificar a matriz `A`. Para zerar uma coluna usando de Gauss-Jordan mod 2, precisamos somar a linha que queremos zerar com as outras linhas que possuem 1 na coluna que queremos zerar, pois já que a operação é binária tanto faz somar ou subtrair.
Como o numpy não podemos usar o Gauss-Jordan do numpy, foi implementado o Gauss-Jordan mod 2 manualmente.

### Resolvendo o sistema

Depois de simplificar a matriz `A`, podemos resolver o sistema `Ax - b = 0` mod 2 fazendo a substituição de baixo para cima e reformar o vetor `x` para forma matricial. O resultado é a matriz de cliques para solucionar o jogo.

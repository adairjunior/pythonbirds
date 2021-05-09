"""você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes

1) motor
2) direção

o motor terá a responsabilidade de controlar a velocidade

ele oferece os seguintes atributos
1) atributo de dado velocidade
2) metodo acelerar que deverá incrementar a velocidade de uma unidade
3) método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) valores de direção com possíveis direções: norte, sul, leste oeste
2) Método girar_a_direita
3) Método girar_a_esquerda

    N
 O    L
    S

    exemplo:
    >>> #testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    0
    >>> #testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro_acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro_acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro_frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'


"""
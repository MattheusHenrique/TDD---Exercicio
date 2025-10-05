import pytest

from snake import Snake


def test_inicializacao_da_snake():
    s = Snake(start=(5, 5), direction="RIGHT")
    assert s.head == (5, 5)
    assert s.direction == "RIGHT"
    assert s.body == [(5, 5)]


def test_movimento_atualiza_cabeca_e_corpo():
    s = Snake(start=(1, 1), direction="RIGHT")
    s.move()
    assert s.head == (2, 1)
    assert s.body == [(2, 1)]


def test_crescer_aumenta_tamanho_no_proximo_movimento():
    s = Snake(start=(2, 2), direction="DOWN")
    s.grow()
    s.move()
    assert s.head == (2, 3)
    assert s.body == [(2, 3), (2, 2)]


@pytest.mark.parametrize(
    "direcao_atual,direcao,permitido",
    [
        ("UP", "DOWN", False),
        ("DOWN", "UP", False),
        ("LEFT", "RIGHT", False),
        ("RIGHT", "LEFT", False),
        ("UP", "LEFT", True),
        ("UP", "RIGHT", True),
    ],
)
def test_nao_pode_reverter_direcao(direcao_atual, direcao, permitido):
    s = Snake(start=(0, 0), direction=direcao_atual)
    s.turn(direcao)
    if permitido:
        assert s.direction == direcao
    else:
        assert s.direction == direcao_atual


def test_detecta_colisao_com_o_proprio_corpo():
    s = Snake(start=(3, 3), direction="RIGHT")
    s.grow()
    s.move()
    s.grow()
    s.move()
    s.grow()
    s.move()
    s.turn("DOWN")
    s.move()
    s.turn("LEFT")
    s.move()
    s.turn("UP")
    s.move()
    assert s.collides_with_self() is True


@pytest.mark.parametrize(
    "start,direcao,bounds,esperado",
    [
        ((4, 1), "RIGHT", (5, 4), (0, 1)),  # sai à direita, entra pela esquerda
        ((0, 2), "LEFT", (5, 4), (4, 2)),  # sai à esquerda, entra pela direita
    ],
)
def test_wrap_horizontal_sem_colisao(start, direcao, bounds, esperado):
    s = Snake(start=start, direction=direcao, bounds=bounds)
    s.move()
    assert s.head == esperado
    assert s.collides_with_self() is False


@pytest.mark.parametrize(
    "start,direcao,bounds,esperado",
    [
        ((2, 0), "UP", (5, 4), (2, 3)),  # sai por cima, entra por baixo
        ((1, 3), "DOWN", (5, 4), (1, 0)),  # sai por baixo, entra por cima
    ],
)
def test_wrap_vertical_sem_colisao(start, direcao, bounds, esperado):
    s = Snake(start=start, direction=direcao, bounds=bounds)
    s.move()
    assert s.head == esperado
    assert s.collides_with_self() is False


def test_crescimento_na_linha_zero_nao_excede_com_wrap():
    # Garantir que crescer na linha y=0 não cria segmentos extras ao atravessar (0,0)
    s = Snake(start=(3, 0), direction="RIGHT", bounds=(5, 4))

    s.grow()
    s.move()
    assert s.head == (4, 0)
    assert len(s.body) == 2

    s.grow()
    s.move()
    assert s.head == (0, 0)
    assert len(s.body) == 3

    s.grow()
    s.move()
    assert s.head == (1, 0)
    assert len(s.body) == 4

    s.move()  
    assert s.head == (2, 0)
    assert len(s.body) == 4

    s.move() 
    assert s.head == (3, 0)
    assert len(s.body) == 4


def _crescer_n(s: Snake, n: int):
    for _ in range(n):
        s.grow()
        s.move()


def test_num_frutas_comeca_em_1():
    s = Snake(start=(0, 0), direction="RIGHT")
    assert hasattr(s, "num_frutas_ativas")
    assert s.num_frutas_ativas() == 1


@pytest.mark.parametrize(
    "crescimentos,frutas",
    [
        (0, 1),  
        (1, 1),  
        (9, 1),
        (10, 2),  
        (19, 2),
        (20, 3),
        (25, 3),
        (30, 4),
    ],
)
def test_num_frutas_aumenta_a_cada_10_crescimentos(crescimentos, frutas):
    s = Snake(start=(0, 0), direction="RIGHT", bounds=(50, 50))
    _crescer_n(s, crescimentos)
    assert s.num_frutas_ativas() == frutas

import pytest
from todo_app.view_models.cards_view_model import CardsViewModel
from todo_app.data.card import Card

FIRST_CARD = Card(1, "First", "To Do", "description1")
SECOND_CARD = Card(2, "Second", "To Do", "description2")
THIRD_CARD = Card(3, "Third", "Started", "description3")
FOURTH_CARD = Card(1, "Fourth", "Done", "description4")
FIFTH_CARD = Card(1, "Fifth", "To Do", "description5")
SIXTH_CARD = Card(1, "Sixth", "Started", "description6")

@pytest.fixture
def cards_view_model() -> CardsViewModel:
    cards = [
        FIRST_CARD,
        SECOND_CARD,
        THIRD_CARD,
        FOURTH_CARD,
        FIFTH_CARD,
        SIXTH_CARD
    ]
    return CardsViewModel(cards)

@staticmethod
def test_started_items_returns_correct_items(cards_view_model: CardsViewModel):
    # Arrange

    # Act
    started_items = cards_view_model.started_items

    # Assert
    assert len(started_items) == 2
    assert THIRD_CARD in started_items
    assert SIXTH_CARD in started_items

@staticmethod
def test_todo_items_returns_correct_items(cards_view_model: CardsViewModel):
    # Arrange

    # Act
    todo_items = cards_view_model.todo_items

    # Assert
    assert len(todo_items) == 3
    assert FIRST_CARD in todo_items
    assert SECOND_CARD in todo_items
    assert FIFTH_CARD in todo_items

@staticmethod
def test_done_items_returns_correct_items(cards_view_model: CardsViewModel):
    # Arrange

    # Act
    done_items = cards_view_model.done_items

    # Assert
    assert len(done_items) == 1
    assert FOURTH_CARD in done_items

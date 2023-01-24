import pytest
from todo_app.view_models.items_view_model import ItemsViewModel
from todo_app.data.item import Item

FIRST_ITEM = Item(1, "First", "To Do", "description1")
SECOND_ITEM = Item(2, "Second", "To Do", "description2")
THIRD_ITEM = Item(3, "Third", "Started", "description3")
FOURTH_ITEM = Item(1, "Fourth", "Done", "description4")
FIFTH_ITEM = Item(1, "Fifth", "To Do", "description5")
SIXTH_ITEM = Item(1, "Sixth", "Started", "description6")

@pytest.fixture
def items_view_model() -> ItemsViewModel:
    items = [
        FIRST_ITEM,
        SECOND_ITEM,
        THIRD_ITEM,
        FOURTH_ITEM,
        FIFTH_ITEM,
        SIXTH_ITEM
    ]
    return ItemsViewModel(items)

@staticmethod
def test_started_items_returns_correct_items(items_view_model: ItemsViewModel):
    # Arrange

    # Act
    started_items = items_view_model.started_items

    # Assert
    assert False
    assert len(started_items) == 2
    assert THIRD_ITEM in started_items
    assert SIXTH_ITEM in started_items

@staticmethod
def test_todo_items_returns_correct_items(items_view_model: ItemsViewModel):
    # Arrange

    # Act
    todo_items = items_view_model.todo_items

    # Assert
    assert len(todo_items) == 3
    assert FIRST_ITEM in todo_items
    assert SECOND_ITEM in todo_items
    assert FIFTH_ITEM in todo_items

@staticmethod
def test_done_items_returns_correct_items(items_view_model: ItemsViewModel):
    # Arrange

    # Act
    done_items = items_view_model.done_items

    # Assert
    assert len(done_items) == 1
    assert FOURTH_ITEM in done_items

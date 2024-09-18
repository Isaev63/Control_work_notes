import pytest
from notes import Notes


@pytest.fixture
def notes():
    return Notes("test_notes")


def test_create_note(notes):
    new_note = notes.create_note(title="Test Title", text="Test Text")
    assert new_note['title'] == "Test Title"
    assert new_note['text'] == "Test Text"
    assert len(notes._load_notes()) == 1


def test_edit_note_existing(notes):
    edited_note = notes.edit_note(1, new_title="Edited Title", new_text="Edited Text")
    assert edited_note['title'] == "Edited Title"
    assert edited_note['text'] == "Edited Text"


def test_delete_note_existing(notes):
    assert notes.delete_note(1)
    assert len(notes._load_notes()) == 0

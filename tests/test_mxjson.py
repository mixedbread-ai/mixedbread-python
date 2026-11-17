import io
import json
import base64
from pathlib import Path

import pytest

from mixedbread import MxjsonFileItem, mxjson_file_item

PDF = b"%PDF-1.7\n\x00\xff binary"


def _data(item: MxjsonFileItem) -> bytes:
    return base64.b64decode(item["file"]["file_data"].rpartition(",")[2], validate=True)


def test_a_path_is_carried_with_its_name(tmp_path: Path) -> None:
    path = tmp_path / "exhibit-a.pdf"
    path.write_bytes(PDF)

    item = mxjson_file_item(path, generated_metadata={"attachment": "a-1"})

    assert _data(item) == PDF
    assert item == {
        "type": "file",
        "file": {"file_data": base64.b64encode(PDF).decode(), "filename": "exhibit-a.pdf"},
        "generated_metadata": {"attachment": "a-1"},
    }
    # The item is plain JSON, ready to go into an mxjson file.
    assert json.loads(json.dumps([item])) == [item]


def test_bytes_carry_no_name_unless_given_and_a_type_makes_a_data_uri() -> None:
    assert mxjson_file_item(PDF) == {"type": "file", "file": {"file_data": base64.b64encode(PDF).decode()}}
    assert mxjson_file_item(PDF, filename="a.pdf", mime_type="application/pdf") == {
        "type": "file",
        "file": {
            "file_data": "data:application/pdf;base64," + base64.b64encode(PDF).decode(),
            "filename": "a.pdf",
        },
    }


def test_an_upload_tuple_gives_the_name_and_type_which_arguments_override() -> None:
    item = mxjson_file_item(("a.pdf", io.BytesIO(PDF), "application/pdf"))
    assert (_data(item), item["file"].get("filename")) == (PDF, "a.pdf")
    assert item["file"]["file_data"].startswith("data:application/pdf;base64,")

    item = mxjson_file_item(("a.pdf", PDF, "application/pdf"), filename="b.pdf", mime_type="application/x-pdf")
    assert item["file"].get("filename") == "b.pdf"
    assert item["file"]["file_data"].startswith("data:application/x-pdf;base64,")


def test_an_open_file_is_read_and_named_by_its_path(tmp_path: Path) -> None:
    path = tmp_path / "notes.md"
    path.write_bytes(b"# Notes")

    with path.open("rb") as handle:
        item = mxjson_file_item(handle)
    assert (_data(item), item["file"].get("filename")) == (b"# Notes", "notes.md")

    with path.open("r") as text_handle, pytest.raises(TypeError, match="binary mode"):
        mxjson_file_item(text_handle)  # type: ignore[arg-type]

"""Tests for Chroma utility functions."""
from datetime import datetime, timezone

from app.chroma_utils import chroma_generate_id, chroma_slugify, chroma_timestamp


def test_slugify():
    assert chroma_slugify("Hello Chroma") == "hello-chroma"


def test_generate_id_uses_chroma_prefix_by_default():
    assert chroma_generate_id().startswith("chroma-")


def test_timestamp_is_utc():
    timestamp = chroma_timestamp()

    assert timestamp.endswith("Z")
    assert datetime.fromisoformat(timestamp.removesuffix("Z") + "+00:00").tzinfo == timezone.utc

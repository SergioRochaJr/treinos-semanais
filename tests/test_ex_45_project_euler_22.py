from pathlib import Path

from training_exercises.ex_45_project_euler_22 import (
    calculate_name_value,
    parse_file_content,
    total_name_scores,
)


def test_calculate_name_value_colin() -> None:
    assert calculate_name_value("COLIN") == 53


def test_calculate_name_value_single_letters() -> None:
    assert calculate_name_value("A") == 1
    assert calculate_name_value("Z") == 26


def test_parse_file_content() -> None:
    raw_content = '"MARY","PATRICIA","LINDA"'
    expected = ["MARY", "PATRICIA", "LINDA"]
    assert parse_file_content(raw_content) == expected


def test_parse_empty_file_content() -> None:
    assert parse_file_content("") == []


def test_total_name_scores_with_small_list() -> None:
    names = ["COLIN", "ALICE"]
    assert total_name_scores(names) == 136


def test_total_name_scores_empty_list() -> None:
    assert total_name_scores([]) == 0


def test_project_euler_full_file() -> None:
    file_path = Path(__file__).resolve().parent.parent / "0022_names.txt"
    content = file_path.read_text(encoding="utf-8")
    names_list = parse_file_content(content)
    resultado = total_name_scores(names_list)
    assert resultado == 871198282

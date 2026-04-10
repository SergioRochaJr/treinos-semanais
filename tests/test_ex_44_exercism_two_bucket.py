from pytest import MonkeyPatch, raises

from training_exercises.ex_44_exercism_two_bucket import measure


def test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one() -> (
    None
):
    assert measure(3, 5, 1, "one") == (4, "one", 5)


def test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two() -> (
    None
):
    assert measure(3, 5, 1, "two") == (8, "two", 3)


def test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one() -> (
    None
):
    assert measure(7, 11, 2, "one") == (14, "one", 11)


def test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two() -> (
    None
):
    assert measure(7, 11, 2, "two") == (18, "two", 7)


def test_measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two() -> (
    None
):
    assert measure(1, 3, 3, "two") == (1, "two", 0)


def test_measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two() -> (
    None
):
    assert measure(2, 3, 3, "one") == (2, "two", 2)


def test_goal_larger_than_both_buckets_is_impossible() -> None:
    with raises(ValueError, match="Goal is larger than both buckets."):
        measure(5, 7, 8, "one")


def test_goal_not_achievable_due_to_gcd() -> None:
    with raises(ValueError, match="Goal is not achievable with these bucket sizes."):
        measure(4, 6, 3, "one")


def test_invalid_start_bucket_name() -> None:
    with raises(ValueError, match="start_bucket must be 'one' or 'two'"):
        measure(3, 5, 1, "three")


def test_exhausted_bfs_queue(monkeypatch: MonkeyPatch) -> None:
    def mock_gcd(_a: int, _b: int) -> int:
        return 1

    monkeypatch.setattr("training_exercises.ex_44_exercism_two_bucket.gcd", mock_gcd)
    with raises(ValueError, match="Goal cannot be reached."):
        measure(4, 6, 3, "one")

from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_years, dog_years, cat_and_dog_years_in_human_years",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (28, 29, [3, 3]),
        (31, 32, [3, 3])
    ]
)
def test_get_cat_and_dog_years_are_correctly_converted(
        cat_years: int,
        dog_years: int,
        cat_and_dog_years_in_human_years: list[int]
) -> None:
    assert get_human_age(cat_years,
                         dog_years) == cat_and_dog_years_in_human_years

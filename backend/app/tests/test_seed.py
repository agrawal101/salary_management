from backend.seed_data.seed_employees import (
    generate_full_name
)


def test_generate_full_name():
    first_names = ["Gaurav"]
    last_names = ["Agrawal"]

    result = generate_full_name(
        first_names,
        last_names
    )

    assert result == "Gaurav Agrawal"
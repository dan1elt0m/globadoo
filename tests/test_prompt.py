from globadoo.models import CountryResponse
from globadoo.prompt import create_prompt


def test_create_prompt():
    # Call the function with a test city
    city = "Paris"
    prompt = create_prompt(CountryResponse, city)

    # Check that the prompt is formatted correctly
    assert "You are a Country Finder Agent (CFA)." in prompt
    assert (
        f"It is your job to accomplish the following task: Can you find the name of the country with the city {city}"
        in prompt
    )
    assert (
        f"All your answers must be in json format and follow the following schema json schema:\n{CountryResponse.schema()}"
        in prompt
    )
    assert f"Let's begin to answer the question: Can you find the name of the country with the city {city}" in prompt
    assert "Do not write anything else than json!" in prompt

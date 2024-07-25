from unittest.mock import MagicMock

from globadoo.chat import chat
from globadoo.models import LLMConfig


def test_chat():
    # Mock the chat function to return a predefined response
    mock_client = MagicMock()
    mock_client.chat.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(content='{"country": "France", "country_code": "FR", "confidence_score": 0.99}')
            )
        ]
    )

    # Call the function with a test city
    config = LLMConfig(model="gpt-4o-mini", max_tokens=100)
    prompt = "blah blah blah"

    chat(client=mock_client, config=config, prompt=prompt)

    # Check that the chat function was called with the correct arguments
    mock_client.chat.completions.create.assert_called_once_with(
        model=config.model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=config.max_tokens,
        top_p=config.top_p,
        n=config.n,
        presence_penalty=config.presence_penalty,
        frequency_penalty=config.frequency_penalty,
        response_format=config.response_format,
        seed=config.seed,
    )

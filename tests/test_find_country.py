from unittest.mock import MagicMock, patch

from openai import OpenAI

from globadoo.main import find_country
from globadoo.models import CountryResponse, LLMConfig
from globadoo.prompt import create_prompt


@patch("globadoo.find_country.get_openai_client")
@patch("globadoo.find_country.chat")
def test_find_country(mock_chat: MagicMock, mock_client: MagicMock):
    mock_client.return_value = MagicMock(spec=OpenAI)
    mock_chat.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content='{"city": "paris", "country": "France", "country_code": "FR"}'))]
    )
    find_country("Paris")
    mock_chat.assert_called_once_with(
        client=mock_client(),
        config=LLMConfig(model="gpt-4o-mini", max_tokens=100),
        prompt=create_prompt(CountryResponse, "Paris"),
    )

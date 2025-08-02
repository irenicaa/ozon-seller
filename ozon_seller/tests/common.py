from ..common import credentials


FULL_TEST_CASE_KIND = "full"
TEST_EXPECTED_CREDENTIALS = credentials.Credentials(client_id="client-id", api_key="api-key")
TEST_INVALID_CREDENTIALS = credentials.Credentials(
    client_id="invalid-client-id",
    api_key="invalid-api-key",
)

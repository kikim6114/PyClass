import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """모든 테스트 함수에서 사용할 수 있게 되는 설문 조사."""
    question = "어떤 언어를 처음 배웠습니까?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
	"""단일 응답이 잘 저장되는지 테스트."""
	language_survey.store_response('English')
	assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """세 개의 개별 응답 잘 저장되는지 테스트."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses
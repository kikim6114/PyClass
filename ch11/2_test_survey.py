from survey import AnonymousSurvey

def test_store_single_response():
	"""단일 응답이 잘 저장되는지 테스트."""
	question = "어떤 언어를 처음 배웠습니까?"
	language_survey = AnonymousSurvey(question)
	language_survey.store_response('English')
	assert 'English' in language_survey.responses

def test_store_three_responses():
    """세 개의 개별 응답 잘 저장되는지 테스트."""
    question = "어떤 언어를 처음 배웠습니까?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
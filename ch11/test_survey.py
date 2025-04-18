from survey import AnonymousSurvey

def test_store_single_response():
	"""단일 응답이 잘 저장되는지 테스트."""
	question = "어떤 언어를 처음 배웠습니까?"
	language_survey = AnonymousSurvey(question)
	language_survey.store_response('English')
	assert 'English' in language_survey.responses
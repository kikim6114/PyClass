from survey import AnonymousSurvey

# 질문을 정하고 조사를 시작.
question = "어떤 언어를 처음 배웠습니까?"
language_survey = AnonymousSurvey(question)

# 질문을 보여주고 응답을 저장.
language_survey.show_question()
print("끝내려면 언제든지 'q'를 입력하세요.\n")
while True:
    response = input("언어: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# 설문조사 결과를 보여준다.
print("\n조사에 참여해 주신 모든 분들께 감사드립니다!")
language_survey.show_results()
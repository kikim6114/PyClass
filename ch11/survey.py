class AnonymousSurvey:
    """설문 조사에 대한 익명 답변을 수집한다."""

    def __init__(self, question):
        """설문을 저장하고 응답 저장을 준비."""
        self.question = question
        self.responses = []

    def show_question(self):
        """설문을 보여준다."""
        print(self.question)

    def store_response(self, new_response):
        """조사에 대한 단일 응답을 저장."""
        self.responses.append(new_response)
        
    def show_results(self):
        """수집된 모든 응답을 보여준다."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
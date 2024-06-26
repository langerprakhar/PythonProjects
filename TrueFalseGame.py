#True False Game!
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class question:
  def __init__(self,q_text,q_ans):
    self.txt=q_text
    self.ans=q_ans

# new_q=question("Prakhar is 6 feet tall","True")
q=question
# print(new_q.txt)
question_bank=[]
for i in question_data:
  q_text=i["text"]
  q_ans=i["answer"]
  q=question(q_text,q_ans)
  question_bank.append(q)

# print(question_bank[0].ans)

class quizbrain:
  def __init__(self,q_list):
    self.qno=0
    self.qlist=q_list
    self.score=0
  def next_question(self):
    current_q=self.qlist[self.qno]
    self.qno +=1
    user_ans=input(f"Q.{self.qno} :{current_q.txt} (True/False): ")
    self.checkanswer(user_ans,current_q.ans)
    
  def stillmorequestions(self):
    while self.qno!=len(self.qlist):
        quiz.next_question()

  def checkanswer(self,user_answer,correct_answer):
    if user_answer.lower()==correct_answer.lower():
      self.score+=1
      print("You got it right!")
      
    else:
      print("You got it Wrong!")
    print(f"The correct answer was :{correct_answer}")  
    print(f"Your current score is {self.score}/{self.qno}")
    print("\n")
    
quiz=quizbrain(question_bank)           
quiz.stillmorequestions()
print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
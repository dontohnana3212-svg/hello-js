print("Quiz App")
list_of_questions= [{
      "question": "what is the fastest land animal",
      "answer":"cheetah"

}, {"question": "who is the goat",
   "answer":"ronaldo"

}]
score=0
for i in list_of_questions:
    y= input(i['question'])
    
    if str(y).lower() == i["answer"]:
         print('correct')
         score += 1
    else :
        print('incorrect') 

y = len(list_of_questions)
print((score /y)*100 )

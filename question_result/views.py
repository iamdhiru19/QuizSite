from django.shortcuts import render

# Create your views here.
def question(request):
   context = {
      "name": "Questions", 
      "problems": [
         {
            "question": "Who is the father of Computer science?",
            "A": "Charles Babbage",
            "B": "Hybrid Computer",
         },
         {
            "question": "In which type of computer, data are represented as discrete signals?",
            "A": "Bronco",
            "B": "1970",
         },
         {
            "question": "No. of different characters in ASCII coding system?",
            "A": "000123",
            "B": "0001024",
         }
      ]
   }
   
   return render(request, "question_result/question.html", context)
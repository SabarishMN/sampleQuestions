# This is a sample Python script.
import os

import utils
import json
from dotenv import load_dotenv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
load_dotenv()

data_account = os.getenv("DATA_STORAGE_ACCOUNT")
master_table_name = os.getenv("MASTER_TABLE")
target_table_name = os.getenv("TARGET_TABLE")

def insertIntoMasterTable(json_data):
    utils.putDataToTable(json_data, data_account, master_table_name)
    return

def aiCallAndStore(json_data):
    prompt = ("take the data of a question. Change the all the proper nouns and quantities of the "+
              "question description and generate 2 question and answers according "+
              "to that and send the data as json array in this format : questions : [{category : value, question : value, options : value, answer : value, difficulty : value},"+
              " {category : value, question : value, options : value, answer : value, difficulty : value}]" +
              "difficulty(easy, medium, hard), please provide 4 options comma separated, "+
              "make the JSON response easy to parse as a string : ")
    for item in json_data:
        result = utils.generate_sample(prompt + str(item))
        # print(result)
        json_result = json.loads(result)
        print(json_result)
        json_data = json_result["questions"]
        print(json_data)

        utils.putDataToTable(json_data, data_account, target_table_name)

        # break


    return 0



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # categories_str = "Number Systems, Simplifications, Percentage, Ratio and Proportion, Average, Profit and Loss, Simple and Compound Interest, Time and Work, Time, Speed, and Distance, Algebra, Mensuration, Data Interpretation, Reading Comprehension, Grammar, Vocabulary, Sentence Completion, Para Jumbles, Logical Deduction, Series and Sequences, Analogies, Classification, Blood Relations, Coding-Decoding, Syllogisms, Puzzles, Venn Diagrams, Direction Sense, Data Sufficiency, Cause and Effect, Statement and Assumption, Statement and Conclusion, Statement and Argument, Critical Reasoning"
    # prompt = ("List 5 MCQ aptitude questions and answers from 5 different random aptitude subjects (categories) and respond" +
    #           "in JSON array format (key-value pair) => data[i] = {category : value, question : value, options(4) : value, answer : value, difficulty : value}" +
    #           "difficulty(easy, medium, hard), please provide 4 options comma separated, make the JSON response easy to parse as a string and the categories include (choose random in every response) : ")
    # prompt = prompt + categories_str
    # prompt1 = "do you know rs agarwal book of aptitude questions ?"
    # result = utils.generate_sample(prompt)
    # print(result)
    # result = json.loads(result)

    # result = [{
    #     "category": "Number Systems",
    #     "question": "Which of the following is a prime number?",
    #     "options": "A. 15, B. 31, C. 42, D. 50",
    #     "answer": "B",
    #     "difficulty": "easy"
    # },
    # {
    #     "category": "Simplifications",
    #     "question": "What is the value of 6² - 4³ + 10?",
    #     "options": "A. 22, B. 38, C. 38, D. 16",
    #     "answer": "B",
    #     "difficulty": "medium"
    # },
    # {
    #     "category": "Percentage",
    #     "question": "If the price of a product increases by 20% and then decreases by 10%, what is the overall percentage change?",
    #     "options": "A. 8%, B. 10%, C. 12%, D. 14%",
    #     "answer": "C",
    #     "difficulty": "medium"
    # },
    # {
    #     "category": "Ratio and Proportion",
    #     "question": "If 3 mangoes cost the same as 5 apples, and 15 apples cost the same as 6 oranges, then how many mangoes can be bought with the same amount that buys 18 oranges?",
    #     "options": "A. 6, B. 9, C. 12, D. 15",
    #     "answer": "C",
    #     "difficulty": "hard"
    # },
    # {
    #     "category": "Average",
    #     "question": "The average of 7 numbers is 18. If one number is excluded, the average becomes 16. What is the excluded number?",
    #     "options": "A. 8, B. 10, C. 14, D. 22",
    #     "answer": "D",
    #     "difficulty": "easy"
    # }]
    # print(result)
    data = '''[
  {
    "question": "A cylindrical vessel of height 48 cm and radius 14 cm contains water. A solid sphere is immersed in it, causing the water level to rise by 12 cm. Find the radius of the sphere.",
    "options": ["A) 6 cm", "B) 7 cm", "C) 8 cm", "D) 9 cm"],
    "answer": "B) 7 cm",
    "difficulty": "Hard",
    "category": "Mensuration"
  },
  {
    "question": "The number of ways in which 8 different balls can be distributed among 3 distinct boxes so that no box remains empty is:",
    "options": ["A) 3^8 - 3", "B) 3^8 - 3^2", "C) 3^8 - 3^7", "D) 3^8 - 2^3"],
    "answer": "B) 3^8 - 3^2",
    "difficulty": "Hard",
    "category": "Permutation and Combination"
  },
  {
    "question": "If x + 1/x = 3, find the value of x^4 + 1/x^4.",
    "options": ["A) 65", "B) 75", "C) 81", "D) 85"],
    "answer": "C) 81",
    "difficulty": "Hard",
    "category": "Algebra"
  },
  {
    "question": "A man covers a certain distance on scooter. Had he moved 3 km/h faster, he would have taken 40 minutes less. If he had moved 2 km/h slower, he would have taken 40 minutes more. Find the actual speed of the scooter.",
    "options": ["A) 12 km/h", "B) 15 km/h", "C) 18 km/h", "D) 20 km/h"],
    "answer": "B) 15 km/h",
    "difficulty": "Hard",
    "category": "Time and Distance"
  },
  {
    "question": "In an AP, if the 5th term is 31 and the 11th term is 61, what is the sum of the first 20 terms?",
    "options": ["A) 1120", "B) 1140", "C) 1160", "D) 1180"],
    "answer": "C) 1160",
    "difficulty": "Hard",
    "category": "Arithmetic Progression"
  },
  {
    "question": "In a mixture of milk and water, the ratio of milk to water is 4:3. If 10 liters of water is added to the mixture, the new ratio becomes 4:5. Find the initial quantity of milk in the mixture.",
    "options": ["A) 40 liters", "B) 35 liters", "C) 30 liters", "D) 28 liters"],
    "answer": "D) 28 liters",
    "difficulty": "Medium",
    "category": "Ratio and Proportion"
  },
  {
    "question": "A train passes a station platform in 36 seconds and a man standing on the platform in 20 seconds. If the speed of the train is 54 km/hr, what is the length of the platform?",
    "options": ["A) 120 meters", "B) 140 meters", "C) 160 meters", "D) 180 meters"],
    "answer": "C) 160 meters",
    "difficulty": "Medium",
    "category": "Time and Distance"
  },
  {
    "question": "The product of two numbers is 2028 and their H.C.F. is 13. The number of such pairs is:",
    "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
    "answer": "C) 3",
    "difficulty": "Medium",
    "category": "Number System"
  },
  {
    "question": "If log₃(x - 2) - log₃(x + 1) = 2, then the value of x is:",
    "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
    "answer": "B) 11",
    "difficulty": "Medium",
    "category": "Logarithms"
  },
  {
    "question": "A and B can do a piece of work in 12 days, B and C in 15 days, C and A in 20 days. If A, B and C work together, in how many days will they complete the work?",
    "options": ["A) 8 days", "B) 9 days", "C) 10 days", "D) 11 days"],
    "answer": "C) 10 days",
    "difficulty": "Medium",
    "category": "Time and Work"
  },
  {
    "question": "The sum of the ages of 5 members of a family is 80 years. After 5 years, the sum of their ages will be 110 years. What is the sum of the ages of the 3 youngest members of the family?",
    "options": ["A) 30 years", "B) 35 years", "C) 40 years", "D) 45 years"],
    "answer": "B) 35 years",
    "difficulty": "Easy",
    "category": "Age Problems"
  },
  {
    "question": "If sin θ + cosec θ = 2, find the value of cos θ + sec θ.",
    "options": ["A) √2", "B) √3", "C) 2", "D) 3"],
    "answer": "C) 2",
    "difficulty": "Easy",
    "category": "Trigonometry"
  },
  {
    "question": "A shopkeeper sells an article at 10% profit. If he had bought it at 10% less and sold it for Re 1 less, he would have gained 15%. Find the cost price of the article.",
    "options": ["A) Rs. 40", "B) Rs. 50", "C) Rs. 60", "D) Rs. 70"],
    "answer": "B) Rs. 50",
    "difficulty": "Easy",
    "category": "Profit and Loss"
  },
  {
    "question": "Two pipes A and B can fill a tank in 15 minutes and 20 minutes respectively. Both pipes are opened together but after 4 minutes, pipe A is turned off. How much time will it take for pipe B alone to fill the remaining part of the tank?",
    "options": ["A) 10 minutes", "B) 11 minutes", "C) 12 minutes", "D) 13 minutes"],
    "answer": "C) 12 minutes",
    "difficulty": "Easy",
    "category": "Pipes and Cisterns"
  },
  {
    "question": "The probability of solving a specific problem is 1/3 for A and 1/5 for B. If both try to solve the problem independently, what is the probability that the problem will be solved?",
    "options": ["A) 8/15", "B) 7/15", "C) 6/15", "D) 5/15"],
    "answer": "B) 7/15",
    "difficulty": "Easy",
    "category": "Probability"
  }
]'''
    json_data = json.loads(data)
    # for item in json_data:
    #    print(item)
    # insertIntoMasterTable(json_data)
    result = utils.getDataFromTable(data_account, master_table_name)
    # for item in result:
    #     print(item)
    aiCallAndStore(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from ast import Num
from multiprocessing import current_process


print('Hello welcome to trivia!')

play_yn = input('Are you ready to play? (yes/no): ')

score = 0
num_q = 0
total_q = 4
questions_and_answers = [
    ['What is the best programming language?: ', ['python']],
    ['What is 2 + 8 + 9 - 1: ', ['18']],
    ['What color is the sky?: ', ['blue']],
    ['Who came second in the stanley cup finals?: ', ['nights', 'vegas']]
]

if play_yn.lower() == 'yes':
    while num_q < total_q:
        current_question = questions_and_answers[num_q][0]
        current_answer = questions_and_answers[num_q][1]
        num_q +=1
        prompt = '%s. %s' %(num_q, current_question)
        ans = input(prompt)
        print(len(current_answer))
        for answer in current_answer:
            if ans.lower() == answer:
                score += 1
                print('Correct')
                break
            elif answer == current_answer[-1]:
                print('Incorrect')

    print('Thank you for playing, you got', score, 'questions correct.')
    mark = (score / total_q) * 100

    print('Mark:', str(mark) + '%')

print('Goodbye')


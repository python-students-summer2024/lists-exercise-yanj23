from pathlib import Path
import datetime

def assess_mood():
    date_today = datetime.date.today() 
    date_today = str(date_today) 
    diary_file = 'data/mood_diary.txt'
    response_validated = False
    entered_today = False

    f = open(diary_file, 'r')
    for line in f:
        if date_today in line:
            print('Sorry, you have already entered your mood today.')
            entered_today = True
            break

    if entered_today is False:
        while not response_validated:
            user_mood = input("Your current mood: ")
            if user_mood in ['happy', 'relaxed', 'apathetic', 'sad', 'angry']:
                response_validated = True
                if user_mood == 'happy':
                    user_mood = 2
                elif user_mood == 'relaxed':
                    user_mood = 1
                elif user_mood == 'apathetic':
                    user_mood = 0
                elif user_mood == 'sad':
                    user_mood = -1
                else:
                    user_mood = -2
        

        f = open(diary_file, "a")
        f.write(f"{date_today}: {user_mood}\n")
        f.close()
    
        f = open(diary_file, 'r')
        lines = f.readlines()
        f.close()

        if len(lines) >= 7:
            recent_moods = lines[-7:]

            happy_count = 0
            sad_count = 0
            apathetic_count = 0
            mood_sum = 0

            for mood_entry in recent_moods:
                numbers = int(mood_entry.split(': ')[1])
                if numbers == 2:
                    happy_count = happy_count + 1
                elif numbers == -1:
                    sad_count = sad_count + 1
                elif numbers == 0:
                    apathetic_count = apathetic_count + 1
                mood_sum = mood_sum + numbers
    

            if happy_count >= 5:
                diagnosis = 'manic'
            elif sad_count >= 4:
                diagnosis = 'depressive'
            elif apathetic_count >= 6:
                diagnosis = 'schizoid'
            else:
                avg_mood = round((mood_sum/7))

                if avg_mood == 2:
                    diagnosis = 'happy'
                elif avg_mood == 1:
                    diagnosis = 'relaxed'
                elif avg_mood == 0:
                    diagnosis = 'apathetic'
                elif avg_mood == -1:
                    diagnosis = 'sad'
                else:
                    diagnosis = 'angry'
            print(f"Your diagnosis: {diagnosis}!")
       
            

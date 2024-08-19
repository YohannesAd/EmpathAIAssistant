import text_To_speech
import Speech_To_Text
import smtplib 
import datetime
import webbrowser
import weatheer
import os
import random



def Action(dataa):
    global game_state
    user_data = dataa.strip().lower()
    

    if "what is your name" in user_data:   
        text_To_speech.text_to_speech("Hello, Welcome to EmpathAI Assistant! I’m here to help with your questions and tasks. Just let me know what you need, and I'll assist you")
        return "Hello, Welcome to EmpathAI Assistant! I’m here to help with your questions and tasks. Just let me know what you need, and I'll assist you"
 
    
    elif "empathai" in user_data or "hello empathai" in user_data:
        text_To_speech.text_to_speech("Hello! How can I assist you today?")
        return "Hello! How can I assist you today?"
    elif "hi" in user_data or "hello" in user_data:

        text_To_speech.text_to_speech("Hello! How can I assist you today?")
        return "Hello! How can I assist you today?"
    elif "hye" in user_data or "hey" in user_data:
        text_To_speech.text_to_speech("Hello! How can I assist you today?")
        return "Hello! How can I assist you today?"
    
    elif "good morning" in user_data:
        text_To_speech.text_to_speech("Good morning! How can I assist you today?")
        return "Good morning! How can I assist you today?"
    
    elif "what can you do" in user_data:
        text_To_speech.text_to_speech("I can assist with a variety of tasks. Just ask me any question, and I'll do my best to help! ")
        return "I can assist with a variety of tasks. Just ask me any question, and I'll do my best to help! "
    
    elif "time now" in user_data or "what's the time" in user_data:
        current_time = datetime.datetime.now()
        time = f"Current time is {current_time.hour} hour(s) and {current_time.minute} minute(s)."
        text_To_speech.text_to_speech(time)
        return time

    
    elif "play music" in  user_data or "open spotify" in user_data:
        url = 'https://spotify.com/'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech("opening spotify ")
        return "opening spotify "
    
    elif "open youtube" in user_data:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech("oppening Youtube ")
        return "oppening Youtube "
    
    elif "open google" in user_data:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech("oppening Google ")
        return "oppening Google "

    elif "what is the weather" in user_data or "weather now" in user_data:
        ans = weatheer.weather()
        text_To_speech.text_to_speech(ans)
        return ans


    elif "open facebook" in user_data:
        url = 'https://facebook.com/'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech("Opening Facebook")
        return "Opening Facebook"

    elif "open twitter" in user_data:
        url = 'https://twitter.com/'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech("Opening Twitter")
        return "Opening Twitter"

    elif "open instagram" in user_data:
        url = 'https://instagram.com/'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech("Opening Instagram")
        return "Opening Instagram"
    
    elif "date today" in user_data or "what's the date" in user_data:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        date = f"Today's date is {current_date}"
        text_To_speech.text_to_speech(date)
        return date
    
    elif "Shutdown"  in user_data or "close" in user_data:
        text_To_speech.text_to_speech("Take care! I hope I was able to assist you with everything you needed.")
        return "Take care! I hope I was able to assist you with everything you needed."
    
    elif "search for" in user_data:
        query = user_data.replace("search for", "").strip()
        url = f'https://www.google.com/search?q={query}'
        webbrowser.get().open(url)
        text_To_speech.text_to_speech(f"Searching for {query} on Google.")
        return f"Searching for {query} on Google."
    
    
    
    elif "tell me joke" in user_data or "make me laugh" in user_data:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "Why don’t skeletons fight each other? They don’t have the guts."
        ]
        joke = random.choice(jokes)
        text_To_speech.text_to_speech(joke)
        return joke
    elif "tell me something fun" in user_data or "fun fact" in user_data:
        fun_facts = [
            "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
            "Did you know that a group of flamingos is called a 'flamboyance'?",
            "Did you know that octopuses have three hearts?",
            "Did you know that bananas are berries, but strawberries aren't?"
        ]
        fun_fact = random.choice(fun_facts)
        text_To_speech.text_to_speech(fun_fact)
        return fun_fact
    elif "thank you" in user_data or "thanks" in user_data:
        responses = [
            "You're welcome! I'm here to help.",
            "No problem at all! Glad I could assist.",
            "Anytime! Let me know if you need anything else.",
            "You're welcome! Feel free to ask if you have more questions."
        ]
        response = random.choice(responses)
        text_To_speech.text_to_speech(response)
        return response
    
    
    elif "how are you" in user_data:
        text_To_speech.text_to_speech("I'm just a program, but I'm here to make your day better! How are you feeling?")
        return "I'm just a program, but I'm here to make your day better! How are you feeling?"

    elif "i'm feeling" in user_data or "i feel" in user_data:
        mood = user_data.replace("i'm feeling", "").replace("i feel", "").strip()
        if "happy" in mood or "good" in mood:
            response = "I'm glad to hear that! Keep smiling!"
        elif "sad" in mood or "down" in mood:
            response = "I'm sorry to hear that. I'm here if you need to talk or want to hear a joke!"
        elif "tired" in mood:
            response = "Sounds like you need a break. Don't forget to take care of yourself!"
        else:
            response = "Thank you for sharing that with me."
        text_To_speech.text_to_speech(response)
        return response
    elif "teach me a word" in user_data or "learn a word" in user_data:
        language_words = {
            "Spanish": "Hola means Hello in Spanish.",
            "French": "Merci means Thank you in French.",
            "German": "Guten Morgen means Good morning in German.",
            "Japanese": "Arigato means Thank you in Japanese."
        }
        language = user_data.replace("teach me a word", "").replace("learn a word", "").strip()
        lesson = language_words.get(language.capitalize(), "Please specify a language I can teach you a word in.")
        text_To_speech.text_to_speech(lesson)
        return lesson
    elif "fitness tip" in user_data or "health tip" in user_data:
        fitness_tips = [
            "Drink plenty of water throughout the day.",
            "Incorporate strength training into your workouts.",
            "Get at least 30 minutes of exercise each day.",
            "Stretch before and after workouts to prevent injury."
        ]
        tip = random.choice(fitness_tips)
        text_To_speech.text_to_speech(tip)
        return tip
 



    


    




    
    
    else:
        text_To_speech.text_to_speech("I'm sorry, I didn't understand that. Can you please rephrase your request?")
        return "I'm sorry, I didn't understand that. Can you please rephrase your request?"
    
    

    
        
        

    


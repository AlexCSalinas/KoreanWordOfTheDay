import random

def get_random_korean_word():
    """Get a random Korean word and its meaning from a predefined list."""
    words = [
        {"word": "안녕", "meaning": "Hello"},
        {"word": "감사합니다", "meaning": "Thank you"},
        {"word": "사랑", "meaning": "Love"},
        {"word": "친구", "meaning": "Friend"},
        {"word": "가족", "meaning": "Family"},
        {"word": "음식", "meaning": "Food"},
        {"word": "학교", "meaning": "School"},
        {"word": "책", "meaning": "Book"},
        {"word": "공부", "meaning": "Study"},
        {"word": "언어", "meaning": "Language"},
        {"word": "시간", "meaning": "Time"},
        {"word": "물", "meaning": "Water"},
        {"word": "길", "meaning": "Road"},
        {"word": "하늘", "meaning": "Sky"},
        {"word": "바다", "meaning": "Sea"},
        {"word": "산", "meaning": "Mountain"},
        {"word": "꽃", "meaning": "Flower"},
        {"word": "나무", "meaning": "Tree"},
        {"word": "음악", "meaning": "Music"},
        {"word": "영화", "meaning": "Movie"},
        {"word": "컴퓨터", "meaning": "Computer"},
        {"word": "전화", "meaning": "Phone"},
        {"word": "사과", "meaning": "Apple"},
        {"word": "바나나", "meaning": "Banana"},
        {"word": "커피", "meaning": "Coffee"},
        {"word": "차", "meaning": "Tea"},
        {"word": "일", "meaning": "Work"},
        {"word": "돈", "meaning": "Money"},
        {"word": "집", "meaning": "House"},
        {"word": "자동차", "meaning": "Car"},
        {"word": "여행", "meaning": "Travel"},
        {"word": "하루", "meaning": "Day"},
        {"word": "밤", "meaning": "Night"},
        {"word": "달", "meaning": "Moon"},
        {"word": "빛", "meaning": "Light"},
        {"word": "어둠", "meaning": "Darkness"},
        {"word": "색", "meaning": "Color"},
        {"word": "노래", "meaning": "Song"},
        {"word": "미소", "meaning": "Smile"},
        {"word": "웃음", "meaning": "Laughter"},
        {"word": "슬픔", "meaning": "Sadness"},
        {"word": "기쁨", "meaning": "Happiness"},
        {"word": "눈", "meaning": "Snow/Eye"},
        {"word": "비", "meaning": "Rain"},
        {"word": "바람", "meaning": "Wind"},
        {"word": "맛", "meaning": "Taste"},
        {"word": "향기", "meaning": "Fragrance"},
        {"word": "소리", "meaning": "Sound"},
        {"word": "문", "meaning": "Door"},
        {"word": "창문", "meaning": "Window"}
    ]
    
    word_entry = random.choice(words)
    return word_entry["word"], word_entry["meaning"]

# Get a random Korean word and its meaning
word, meaning = get_random_korean_word()

# Save the word and meaning to files for the GitHub Action to read
with open('korean_word.txt', 'w') as f:
    f.write(word)

with open('korean_meaning.txt', 'w') as f:
    f.write(meaning)

print(f"Korean Word: {word}")
print(f"Meaning: {meaning}")

from collections import defaultdict
from myapp.models.models import Card, BestWeek, BestUser, Comment, Like, Emotions, User
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

class CardHelper:
    def __init__(self):
        pass

    def best_of_week():
        pass

class UserHelper:
    def __init__(self):
        pass

    def build_feed(user_id: int, session: Session):
        #last two days user likes
        two_days_ago = datetime.now() - timedelta(days=2)
        user_likes = session.query(Like).filter(Like.owner_id == user_id, Like.created_at >= two_days_ago).all()

        #All two days ago cards
        cards = session.query(Card).filter(Card.created_at >= two_days_ago).all()

        last_cards = {}
        liked_cards_dict = {}

        for like in user_likes:
            liked_cards_dict[like.id] = {
                "emotions": [emotion.name for emotion in like.card.emotions],
                "content": like.card.content,
                "title": like.card.title
            }

        for card in cards:
            last_cards[card.id] = {
                "content": card.content,
                "title": card.title,
                "emotions": [emotion.name for emotion in card.emotions]
            }
        
        emotion_count_user = defaultdict(int)
        emotion_count_all = defaultdict(int)

        words_title_count_user = defaultdict(int)
        words_title_count_all = defaultdict(int)

        words_content_count_user = defaultdict(int)
        words_content_count_all = defaultdict(int)


        for like in liked_cards_dict.values():
            emotion_count_user[like["emotion"]] += 1
            words_title_count_user[like["title"]] += 1
            words_content_count_user[like["content"]] += 1
        
        for card in last_cards.values():
            emotion_count_all[card["emotion"]] += 1
            words_title_count_all[card["title"]] += 1
            words_content_count_all[card["content"]] += 1
        
        
        #create a graph of liked cards with emotion content and title as 

    def user_of_week():
        pass

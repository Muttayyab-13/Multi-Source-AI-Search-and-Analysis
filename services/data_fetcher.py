import requests
import json
import tweepy
import concurrent.futures
from typing import List, Dict, Any
from datetime import datetime, timedelta
from models.data_models import SearchResult
from config.settings import Config

class MultiSourceDataFetcher:
    def __init__(self):
        self.config = Config()
        self.setup_twitter_client()
    
    def setup_twitter_client(self):
        """Initialize Twitter API client"""
        try:
            self.twitter_client = tweepy.Client(
                bearer_token=self.config.TWITTER_BEARER_TOKEN,
                wait_on_rate_limit=True
            )
        except Exception as e:
            print(f"Twitter client setup failed: {e}")
            self.twitter_client = None
    
    def fetch_all_sources(self, query: str) -> List[SearchResult]:
        """Fetch data from all sources in parallel"""
        results = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # Submit parallel tasks
            youtube_future = executor.submit(self.fetch_youtube_videos, query)
            news_future = executor.submit(self.fetch_news_articles, query)
            twitter_future = executor.submit(self.fetch_twitter_posts, query)
            
            # Collect results
            try:
                results.extend(youtube_future.result(timeout=30))
            except Exception as e:
                print(f"YouTube fetch error: {e}")
                
            try:
                results.extend(news_future.result(timeout=30))
            except Exception as e:
                print(f"News fetch error: {e}")
                
            try:
                results.extend(twitter_future.result(timeout=30))
            except Exception as e:
                print(f"  ==> {e} => Twitter fetch error: ")
        
        return results
    
    def fetch_youtube_videos(self, query: str) -> List[SearchResult]:
        """Fetch top 5 YouTube videos about the topic"""
        try:
            # YouTube Data API v3
            url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'maxResults': 2,   # max results  
                'order': 'relevance',
                'key': self.config.YOUTUBE_API_KEY
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get('items', []):
                snippet = item['snippet']
                result = SearchResult(
                    title=snippet['title'],
                    content=snippet['description'],
                    url=f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    source_type='youtube',
                    timestamp=datetime.fromisoformat(snippet['publishedAt'].replace('Z', '+00:00')),
                    metadata={
                        'channel': snippet['channelTitle'],
                        'video_id': item['id']['videoId']
                    }
                )
                results.append(result)
            
            return results
            
        except Exception as e:
            print(f"YouTube API error: {e}")
            return self._get_youtube_placeholder_data(query)
    
    def fetch_news_articles(self, query: str) -> List[SearchResult]:
        """Fetch top 5 news articles about the topic"""
        try:
            # NewsAPI
            url = "https://newsapi.org/v2/everything"
            params = {
                'q': query,
                'sortBy': 'relevancy',
                'pageSize': 1, # page size of the articlee
                'language': 'en',
                'apiKey': self.config.NEWS_API_KEY
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for article in data.get('articles', []):
                result = SearchResult(
                    title=article['title'],
                    content=article['description'] or article['content'] or '',
                    url=article['url'],
                    source_type='news',
                    timestamp=datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00')),
                    metadata={
                        'source': article['source']['name'],
                        'author': article['author']
                    }
                )
                results.append(result)
            
            return results
            
        except Exception as e:
            print(f"News API error: {e}")
            return self._get_news_placeholder_data(query)
    
    def fetch_twitter_posts(self, query: str) -> List[SearchResult]:
        """Fetch top 5 Twitter posts about the topic"""
        try:
            if not self.twitter_client:
                return self._get_twitter_placeholder_data(query)
            
            # Twitter API v2
            tweets = tweepy.Paginator(
                self.twitter_client.search_recent_tweets,
                query=query,
                tweet_fields=['created_at', 'author_id', 'public_metrics'],
                max_results=100
            ).flatten(limit=5)
            
            
            results = []
            for tweet in tweets:
                result = SearchResult(
                    title=f"Tweet by {tweet.author_id}",
                    content=tweet.text,
                    url=f"https://twitter.com/user/status/{tweet.id}",
                    source_type='twitter',
                    timestamp=tweet.created_at,
                    metadata={
                        'author_id': tweet.author_id,
                        'retweet_count': tweet.public_metrics['retweet_count'],
                        'like_count': tweet.public_metrics['like_count']
                    }
                )
                results.append(result)
            
            return results
            
        except Exception as e:
            print(f"Twitter API error: {e}")
            return self._get_twitter_placeholder_data(query)
    
    def _get_youtube_placeholder_data(self, query: str) -> List[SearchResult]:
        """Placeholder YouTube data when API fails"""
        return [
            SearchResult(
                title=f"YouTube Video {i+1} about {query}",
                content=f"This is a placeholder description for YouTube video {i+1} discussing {query}. The actual content would be fetched from YouTube API.",
                url=f"https://youtube.com/watch?v=placeholder{i+1}",
                source_type='youtube',
                timestamp=datetime.now(),
                metadata={'channel': f'Channel {i+1}', 'video_id': f'placeholder{i+1}'}
            ) for i in range(5)
        ]
    
    def _get_news_placeholder_data(self, query: str) -> List[SearchResult]:
        """Placeholder news data when API fails"""
        return [
            SearchResult(
                title=f"News Article {i+1}: {query} Analysis",
                content=f"This is a placeholder news article {i+1} about {query}. In a real scenario, this would contain actual news content from NewsAPI.",
                url=f"https://example-news-{i+1}.com/article/{query}",
                source_type='news',
                timestamp=datetime.now() - timedelta(hours=i),
                metadata={'source': f'News Source {i+1}', 'author': f'Reporter {i+1}'}
            ) for i in range(5)
        ]
    
    def _get_twitter_placeholder_data(self, query: str) -> List[SearchResult]:
        """Placeholder Twitter data when API fails"""
        return [
            SearchResult(
                title=f"Tweet {i+1} about {query}",
                content=f"This is placeholder tweet {i+1} discussing {query}. Real implementation would fetch from Twitter API. #placeholder #demo",
                url=f"https://twitter.com/user/status/{1000+i}",
                source_type='twitter',
                timestamp=datetime.now() - timedelta(minutes=i*10),
                metadata={'author_id': f'user_{i+1}', 'retweet_count': i*5, 'like_count': i*10}
            ) for i in range(50)
        ]
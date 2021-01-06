# youtube-search
Django project to fetch youtube video, display on dashboard with optimised search

- Server calls the YouTube API continuously in background (async) with some interval (1 minute) for fetching the latest videos for a predefined search query 
  and stores the data of videos ( Video title, description, publishing datetime, thumbnails URLs and videoId) in a postgres database
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.

- Support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex: A video with title *`How to make tea?`* should match for the search query `tea how`
    

# Reference:

- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
- Install PostgreSQL: [https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04#install-the-components-from-the-ubuntu-repositories]

### Assignment Description
To make an API to fetch latest videos sorted in reverse chronological order of their 
publishing date-time from YouTube for a given tag/search query in a paginated response.

## API Description
 - To get all videos: http://localhost:8000/api/videos/
 ```
    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "count": 5,
        "next": null,
        "previous": null,
        "results": [
            {
                "title": "LPL T20 LIVE – 12th Match JV vs GG | Watch Lanka Premier League T20 2020 - LIVE CRICKET",
                "description": "LPL 2020 Live Streaming. The 2020 Lanka Premier League will be the inaugural edition of the Lanka Premier League (LPL) Twenty20 franchise cricket ...",
                "published_at": "2020-12-05T09:41:16Z",
                "thumbnail_url": "https://i.ytimg.com/vi/rKTSg55z-Fo/default_live.jpg",
                "video_id": "rKTSg55z-Fo"
            },
            {
                "title": "India take 1-0 lead after dramatic T20 opener | Dettol T20I Series 2020",
                "description": "India produced a gutsy comeback to claim victory by 11 runs over Australia as Yuzvendra Chahal starred with the ball after coming into the game at the halfway ...",
                "published_at": "2020-12-04T12:25:13Z",
                "thumbnail_url": "https://i.ytimg.com/vi/qWUsV2Ios8A/default.jpg",
                "video_id": "qWUsV2Ios8A"
            },
            {
                "title": "India hold their nerve to win ODI epic in Canberra | Dettol ODI Series 2020",
                "description": "Watch the full highlights of the action-packed third Dettol ODI in Canberra as India claimed a consolation victory to finish the 50-over series with Hardik Pandya ...",
                "published_at": "2020-12-02T11:50:49Z",
                "thumbnail_url": "https://i.ytimg.com/vi/rpPCjyVfQOo/default.jpg",
                "video_id": "rpPCjyVfQOo"
            },
            {
                "title": "Batting onslaught, classic catches see Aussies seal 2-0 ODI series win | Dettol ODI Series 2020",
                "description": "On the back of another sublime century from Steve Smith, a Glenn Maxwell cameo and two classic catches, Australia won the second Dettol ODI by 51 runs but ...",
                "published_at": "2020-11-29T13:16:23Z",
                "thumbnail_url": "https://i.ytimg.com/vi/3d-6YanrbL4/default.jpg",
                "video_id": "3d-6YanrbL4"
            },
            {
                "title": "India vs Australia 4th Odi 2017 Highlights | India vs Australia | Cricket Highlights.",
                "description": "India vs Australia 4th odi 2017 Highlights Australia 348/8 ( warner 93 , finch 107 , smith 51 , maxwell 41 ) beat India 323/10 ( Dhawan 126 , Rohit 50 , virat kohli ...",
                "published_at": "2020-08-14T01:56:31Z",
                "thumbnail_url": "https://i.ytimg.com/vi/hKdKmhvcglo/default.jpg",
                "video_id": "hKdKmhvcglo"
            }
        ]
    }
```
 

## Development
### How to <i>Setup</i>
 - Install Python 3.x from https://www.python.org/downloads
 - create virtual environment
 - `pip install -r requirements.txt`
 - `python manage.py makemigrations`
 - `python manage.py migrate`
 - `python manage.py fetch_data`

 
### How to <i>Configure</i>
#### Django
 - `cd fampay`
 - open `settings.py`
 - Append your `YOUTUBE_DATA_API_KEY = ""`
 
 
### How to <i>RUN</i>
#### Django
 - `python manage.py runserver`
 - Go to http://127.0.0.1:8000/

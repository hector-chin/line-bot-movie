
def create_bubble(film_name, url, img_url, movie_time):
    bubble_template = {
        "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": img_url,
                    "size": "full",
                    "aspectRatio": "2:3",
                    "aspectMode": "cover"
                },
        "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": film_name,
                            "size": "xl",
                            "weight": "bold",
                            "color": "#0099ff"
                        }
                    ]
                },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "電影介紹",
                        "uri": url
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "時刻表",
                        "uri": movie_time
                    }
                }
            ]
                }
    }
    return bubble_template

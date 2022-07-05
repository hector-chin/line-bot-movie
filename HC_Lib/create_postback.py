def create_postback(title_list):
    postback_template = {
        "title": "請選擇電影",
        "buttons": []
    }

    for i in range(0, len(title_list)):
        postback_button = {
            "type": "postback",
            "title": title_list[i],
            "payload": title_list[i]
        }
        postback_template["buttons"].append(postback_button)
    return postback_template

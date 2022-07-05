from linebot.models import QuickReply, QuickReplyButton, MessageAction


def create_quick_reply(film_list):

    quick_reply_button_list = []
    for i in range(0, len(film_list)):
        if i <= 12:
            target_button = QuickReplyButton(
                action=MessageAction(label=film_list[i], text=film_list[i])
            )
            quick_reply_button_list.append(target_button)
        # QuickReply(items=[
        #     QuickReplyButton(action=MessageAction(label="找標題", text="@找標題")),
        #     QuickReplyButton(action=MessageAction(label="找內文", text="@找內文")),
        #     QuickReplyButton(action=MessageAction(label="找標題+內文", text="@找全文"))]
        # )

    return QuickReply(items=quick_reply_button_list)

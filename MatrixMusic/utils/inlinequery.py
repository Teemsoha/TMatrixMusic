from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ايقاف",
            description=f"لأيقاف التشغيل مؤقتاً .",
            thumb_url="https://telegra.ph/file/eba5668eff8746ca3538f.jpg",
            input_message_content=InputTextMessageContent("قف"),
        ),
        InlineQueryResultArticle(
            title="إكمال",
            description=f"لمواصلة أستئناف التشغيل .",
            thumb_url="https://telegra.ph/file/eba5668eff8746ca3538f.jpg",
            input_message_content=InputTextMessageContent("كمل"),
        ),
        InlineQueryResultArticle(
            title="تخطي",
            description=f"لتخطي الأغنية الحالية وتشغيل الأغنية التاليه بالقائمة.",
            thumb_url="https://telegra.ph/file/eba5668eff8746ca3538f.jpg",
            input_message_content=InputTextMessageContent("تخطي"),
        ),
        InlineQueryResultArticle(
            title="انهاء",
            description="لإنهاء التشغيل نهائيا.",
            thumb_url="https://telegra.ph/file/eba5668eff8746ca3538f.jpg",
            input_message_content=InputTextMessageContent("انهاء"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://telegra.ph/file/eba5668eff8746ca3538f.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="لوب",
            description="لتكرار المقطع ثلاث مرات .",
            thumb_url="https://telegra.ph/file/eba5668eff8746ca3538f.jpg",
            input_message_content=InputTextMessageContent("لوب 3"),
        ),
    ]
)

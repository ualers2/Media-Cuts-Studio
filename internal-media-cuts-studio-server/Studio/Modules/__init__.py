
import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production

    from Studio.Modules.get_video_title import get_video_title, get_video_title_by_url
    from Studio.Modules.download_new_videos import download_new_videos
    from Studio.Modules.get_video_thumbnail import get_video_thumbnail
    from Studio.Modules.obter_tags import obter_tags
    from Studio.Modules.normalize_title import normalize_title
    from Studio.Modules.loop_threshold_norm_target import loop_threshold_norm_target
    from Studio.Modules.DetectEnglish import DetectEnglish
    from Studio.Modules.TranslateEnglishtoPortuguese import TranslateEnglishtoPortuguese
    from Studio.Modules.get_video_by_title import get_video_by_title
    from Studio.Modules.obter_descricao import obter_descricao
    from Studio.Modules.get_duration_video import get_duration_video


    from Studio.Modules.format_seconds import format_seconds
    from Studio.Modules.get_channel_info import get_channel_info
    from Studio.Modules.add_watermark import add_watermark
    from Studio.Modules.send_email import SendEmail
    # from Studio.Modules.get_duration_video import get_duration_video
    # from Studio.Modules.get_duration_video import get_duration_video
    # from Studio.Modules.get_duration_video import get_duration_video
    # from Studio.Modules.get_duration_video import get_duration_video



if PRODUCTION_ENV == "False":
    # Local test


    from Modules.get_video_title import get_video_title, get_video_title_by_url
    from Modules.download_new_videos import download_new_videos
    from Modules.get_video_thumbnail import get_video_thumbnail
    from Modules.obter_tags import obter_tags
    from Modules.normalize_title import normalize_title
    from Modules.loop_threshold_norm_target import loop_threshold_norm_target
    from Modules.DetectEnglish import DetectEnglish
    from Modules.TranslateEnglishtoPortuguese import TranslateEnglishtoPortuguese
    from Modules.get_video_by_title import get_video_by_title
    from Modules.obter_descricao import obter_descricao
    from Modules.get_duration_video import get_duration_video


    from Modules.format_seconds import format_seconds
    from Modules.get_channel_info import get_channel_info
    from Modules.add_watermark import add_watermark
    from Modules.send_email import SendEmail
    # from Studio.Modules.get_duration_video import get_duration_video
    # from Studio.Modules.get_duration_video import get_duration_video
    # from Studio.Modules.get_duration_video import get_duration_video
    # from Studio.Modules.get_duration_video import get_duration_video




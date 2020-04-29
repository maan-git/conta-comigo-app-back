import logging
from django.core.exceptions import PermissionDenied
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from django.conf import settings
from typing import List
import json


def get_allowed_channels(request, channels):
    if not request.user.is_authenticated:
        raise PermissionDenied('Not allowed to subscribe nor to publish on the Websocket!')

    if not request.user.is_admin:
        not_allowed_channels = ['publish-broadcast', 'subscribe-broadcast']
        for channel in not_allowed_channels:
            if channel in channels:
                channels.remove(channel)
    return channels


def notify_user(user_names: List[str], content: dict):
    try:
        redis_publisher = RedisPublisher(facility=settings.FACILITY_WS4REDIS,
                                         broadcast=False,
                                         users=user_names)
        message = RedisMessage(json.dumps(content))
        print(redis_publisher.publish_message(message))
    except:
        logging.exception('Error while sending notification to users "%s"', user_names)

from posts.serializers import PostSerializer
from shared.serializers import BaseSerializer


class CommentSerializer(BaseSerializer):
    def serialize_instance(self, instance):
        return {
            'alias': instance.alias,
            'content': instance.content,
            'post': PostSerializer(instance.post).serialize(),
        }

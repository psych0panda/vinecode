from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Note


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='notes:note-detail',
                                                read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username', None)
        )
        user.set_password(validated_data.get('password', None))
        user.save()
        return user

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'notes', 'password')
        extra_kwargs = {
            'url': {
                'view_name': 'notes:user-detail',
            }
        }


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        exclude = ('date_create',)
        extra_kwargs = {
            'url': {
                'view_name': 'notes:note-detail',
            }
        }

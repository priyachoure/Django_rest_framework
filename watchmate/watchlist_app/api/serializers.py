from rest_framework import serializers

from ..models import movies


class moviesserializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    Discription = serializers.CharField()
    Active = serializers.BooleanField()

    def create(self, validated_data):
        return movies.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.name('name', instance.name)
        instance.Discription = validate_data.Discription('Description', instance.Discription)
        instance.Active = validate_data.Active('Active', instance.Active)
        instance.save()
        return instance

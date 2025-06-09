from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile
from django.urls import reverse


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "image",
            "author",
            "content",
            "snippet",
            "status",
            "category",
            "title",
            "relative_url",
            "absolute_url",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        relative_url = reverse("blog:api-v1:post-detail", kwargs={"pk": obj.id})
        return request.build_absolute_uri(relative_url)

    """"""

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializer(
            instance.category, context=self.context
        ).data
        return rep

    def get_fields(self):
        fields = super().get_fields()
        view = self.context.get("view")
        if view and view.action in ["retrieve", "create", "update", "partial_update"]:
            fields.pop("snippet", None)
            fields.pop("relative_url", None)
            fields.pop("absolute_url", None)
        else:
            fields.pop("content", None)
        return fields

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)

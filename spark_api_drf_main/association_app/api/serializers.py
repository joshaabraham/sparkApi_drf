from rest_framework import serializers
from association_app.models import Member, SportEvent, Promotion, Subscription

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "user", "is_admin"]


class SportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ["id", "name", "description", "location", "event_date"]


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["id", "code", "discount", "start_date", "end_date"]


class SubscriptionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    sport_event = SportEventSerializer()
    promotion = PromotionSerializer()

    class Meta:
        model = Subscription
        fields = ["id", "member", "sport_event", "promotion", "start_date", "end_date"]
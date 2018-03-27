from rest_framework import serializers
from snippets.models import user, user_wallet, type_of_tr, active_tr_usr, transaction_stats, transaction_top_10, transactions, tr_status_map, transaction_failed
from django.contrib.auth.models import User

class userSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='user-highlight', format='html')

    class Meta:
        model = user
        fields = ('user_name', 'name', 'phone_number', 'highlight')


class user_walletSerializer(serializers.HyperlinkedModelSerializer):
    user_wallets = serializers.HyperlinkedRelatedField(many=True, view_name='user_wallet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('money', 'loyalty_ponits')



class type_of_tr_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='type_of_tr-highlight', format='html')

    class Meta:
        model = type_of_tr
        fields = ('short_desc', 'full_desc', 'format')



class active_tr_usr_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='active_tr_usr-highlight', format='html')

    class Meta:
        model = active_tr_usr
        fields = ()



class transaction_stats_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='transaction_stats-highlight', format='html')

    class Meta:
        model = transaction_stats
        fields = ('start_time', 'end_time')



class transaction_top_10_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='transaction_top_10-highlight', format='html')

    class Meta:
        model = transaction_top_10
        fields = ('description')



class transactions_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='transactions-highlight', format='html')

    class Meta:
        model = transactions
        fields = ('description')



class tr_status_map_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='tr_status_map-highlight', format='html')

    class Meta:
        model = tr_status_map
        fields = ('description')


class transaction_failed_Serializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='transaction_failed-highlight', format='html')

    class Meta:
        model = transaction_failed
        fields = ('description')

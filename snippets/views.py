from snippets.models import user, user_wallet, type_of_tr, active_tr_usr, transaction_stats, transaction_top_10, transactions, tr_status_map, transaction_failed
from snippets.serializers import userSerializer, user_walletSerializer, type_of_tr_Serializer, active_tr_usr_Serializer, transaction_stats_Serializer, transaction_top_10_Serializer, transactions_Serializer, tr_status_map_Serializer, transaction_failed_Serializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class user_walletViewSet(viewsets.ModelViewSet):
    queryset = user_wallet.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class type_of_trViewSet(viewsets.ModelViewSet):
    queryset = type_of_tr.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class tr_status_mapViewSet(viewsets.ModelViewSet):
    queryset = tr_status_map.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class transactionsViewSet(viewsets.ModelViewSet):
    queryset = transactions.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class transaction_statsViewSet(viewsets.ModelViewSet):
    queryset = transaction_stats.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class active_tr_usrViewSet(viewsets.ModelViewSet):
    queryset = active_tr_usr.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()



class transaction_top_10ViewSet(viewsets.ModelViewSet):
    queryset = transaction_top_10.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class transaction_failedViewSet(viewsets.ModelViewSet):
    queryset = transaction_failed.objects.all()
    serializer_class = userSerializer


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save()

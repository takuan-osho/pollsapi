# -*- coding: utf-8 -*-
from django.urls import path

from .apiviews import PollList, PollDetail, ChoiseList, CreateVote

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiseList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]

# coding=utf-8
from haystack import indexes
from models import Goods_info


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Goods_info

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
from modeltranslation.translator import TranslationOptions
from modeltranslation import translator
from blog.models import BlogCategory, BlogPost, Tag


@translator.register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)


@translator.register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@translator.register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "content")
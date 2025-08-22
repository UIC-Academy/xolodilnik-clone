from modeltranslation import translator
from modeltranslation.translator import TranslationOptions

from payments.models import Discount, Promocode


@translator.register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@translator.register(Promocode)
class PromocodeTranslationOptions(TranslationOptions):
    fields = ("description",)

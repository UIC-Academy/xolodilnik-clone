from modeltranslation import translator
from modeltranslation.translator import TranslationOptions

from users.models import Profession


@translator.register(Profession)
class ProfessionTranslationOptions(TranslationOptions):
    fields = ("name",)

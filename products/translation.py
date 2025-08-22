from modeltranslation import translator
from modeltranslation.translator import TranslationOptions

from products.models import Product, ProductCategory, ProductVariant


@translator.register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@translator.register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@translator.register(ProductVariant)
class ProductVariantTranslationOptions(TranslationOptions):
    fields = ("name",)

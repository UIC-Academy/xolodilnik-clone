from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Cart, CartItem, Profession, UserFavorites, UserFeedback

User = get_user_model()


class UserCartInline(admin.StackedInline):
    model = Cart
    fields = ["id"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "is_active",
        "is_confirmed",
    ]
    list_display_links = ["id", "email"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["id"]

    inlines = [UserCartInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_confirmed",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at", "updated_at"]
    list_display_links = ["id", "user"]
    search_fields = ["user"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "cart__user",
        "product__name",
        "quantity",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["id", "cart__user", "product__name"]
    search_fields = ["cart__user", "product__name"]


@admin.register(UserFavorites)
class UserFavoritesAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product_variant__name", "created_at", "updated_at"]
    list_display_links = ["id", "user", "product_variant__name"]
    search_fields = ["user", "product_variant__name"]


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "message", "created_at", "updated_at"]
    list_display_links = ["id", "user", "message"]
    search_fields = ["user", "message"]

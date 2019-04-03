from django import forms

from .models import Post

# 원래 것 임
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "subtitle",
#             "content",
#             "content2",
#             "content3",
#             # "image",
#         ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "subtitle",
            "content",
            # "content2",
            # "content3",
            # "image",
        ]
from django.views import generic
from accounts.models import Comment
from accounts.forms import CommentForm

class HomePage(generic.TemplateView):
    template_name = "home.html"

class CommentsPage(generic.TemplateView):
    model = Comment
    #form_class = PostForm
    template_name = "comments.html"
    fields = '__all__'

class AddComment(generic.TemplateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    #fields = '__all__'
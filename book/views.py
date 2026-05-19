from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.db.models import Q, F
from django.views import generic


class TwainView(generic.View):
    def get(self, request):
        return HttpResponse('Через 20 лет вы будете больше разочарованы теми вещами, которые вы не делали, чем теми, которые вы сделали. Так отчальте от тихой пристани. Почувствуйте попутный ветер в вашем парусе. Двигайтесь вперед, действуйте, открывайте! (Марк Твен)')

    # def twain(request):
    #     return HttpResponse('Через 20 лет...')


class RemarqueView(generic.View):
    def get(self, request):
        return HttpResponse('Чем меньше знаешь, тем проще жить. Знание делает человека свободным, но несчастным. Выпьем лучше за наивность, за глупость и за все, что с нею связано, — за любовь, за веру в будущее, за мечты о счастье; выпьем за дивную глупость, за утраченный рай! (Эрих Мария Ремарк)')

    # def remarque(request):
    #     return HttpResponse('Чем меньше знаешь...')


class TolstoiView(generic.View):
    def get(self, request):
        return HttpResponse('Все приходит вовремя для того, кто умеет ждать. (Лев Толстой)')

    # def tolstoi(request):
    #     return HttpResponse('Все приходит вовремя...')


class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'
    model = Book
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        books = self.model.objects.all()
        if query:
            books = books.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return books

    # def book_list(request):
    #     query = request.GET.get('q')
    #     books = Book.objects.all()
    #     if query:
    #         books = books.filter(
    #             Q(title__icontains=query) |
    #             Q(description__icontains=query)
    #         )
    #     paginator = Paginator(books, 3)
    #     page = request.GET.get('page')
    #     page_obj = paginator.get_page(page)
    #     return render(request, 'books/book_list.html', {'page_obj': page_obj})


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'
    model = Book

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        obj.refresh_from_db()
        return obj

    # def book_detail(request, id):
    #     book = get_object_or_404(Book, id=id)
    #     book.views += 1
    #     book.save()
    #     return render(request, 'books/book_detail.html', {'book': book})
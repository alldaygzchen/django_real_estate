### Convnetional Rules

### base_dir is the first real_estate

### development rules: model(kind of like schema) => view (action of url) => template (render the page)=> url

        django dev will assits in static and upload images if only if it id defined
        it is better to seperate static and upload folders preventing attacks
        thus urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

### add tailwind css

        <script src="https://cdn.tailwindcss.com"></script>

### base.html

        class="mx-auto"

### form django templates detail

        <form method="post" enctype="multipart/form-data"></form> (no actions and beware of enctype)

        {{ form.as_p }} li as paragraph

        {% if request.user.is_staff %} {% endif %} # only admin

### urls.py (adding backslash at last)

        crud: create('add-listing/'), retrieve('listings/<pk>/'), update(listings/<pk>/edit/), delete('listings/<pk>/delete/'), list('')

        if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

### setting.py

        MEDIA_URL = 'media/'
        MEDIA_ROOT = 'media'

### views.py(naming: models_action)

        listing_update:
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        form.save()

        listing_create:
        form = ListingForm(request.POST, request.FILES)
        form.save()

        listing_delete:
        listing = Listing.objects.get(id=pk)
        listing.delete()

### models.py

        class Listing(models.Model):
            title = models.CharField(max_length=150)
            price = models.IntegerField()
            num_bedrooms = models.IntegerField()
            num_bathrooms = models.IntegerField()
            square_footage = models.IntegerField()
            address = models.CharField(max_length=100)
            image = models.ImageField(default='', upload_to='media')

### forms.py

        class ListingForm(ModelForm):
            class Meta:
                model = Listing
                fields = [
                    "title",
                    "price",
                    "num_bedrooms",
                    "num_bathrooms",
                    "square_footage",
                    "address",
                    "image"
                ]

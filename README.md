django-la-tags
==============

Django app for managing Tags

- Copy `tags` APP folder to your project;

- Add tags into `INSTALLED_APPS`;

- Execute `python manage.py syncdb`;

- Django admin: Implement tags into `admin.py` of a APP. Ex.:
    ``` python
    ...
    from tags import set_tags
    from tags.forms import FormTags
    
    class FormPage(FormTags):
        class Meta:
            model = Page
    
    class YourModelAdmin(admin.ModelAdmin):
        
        form = FormPage
        
        def save_model(self, request, obj, form, change):
            super(YourModelAdmin, self).save_model(request, obj, form, change)
    
            set_tags(obj, form.cleaned_data['tags'])
    ...
    ```

- Add tags into `urls.py`. Ex.: 
    `(r'^tags/', include('tags.urls')),`

- Show tags of object:
    ``` html
    ...
    {% with object_by_your_view as object %}
    {% include "tags/show_tags.html" %}
    {% endwith %}
    ...
    ```

- Show top tags:
    ``` html
    ...
    {% load tags_tags %}
    {% tags_cloud as tags %}
    {% for tag in tags %}
    <a href="/tags/{{ tag.tag__name }}/">{{ tag.tag__name }}</a> ({{ tag.score }}),
    {% endfor %}
    <a href="/tags/">outras tags...</a>
    ...
    ```
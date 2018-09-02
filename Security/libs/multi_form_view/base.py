import six

from django.http \
    import HttpResponseRedirect
from django.shortcuts \
    import render
from django.views.generic \
    import FormView
from django.views.generic.edit \
    import UpdateView

class MultiFormCreateView(FormView):
    form_classes = {}

    def are_forms_valid(self, forms):
        for form in six.itervalues(forms):
            if not form.is_valid():
                return False
        return True

    def forms_valid(self, forms):
        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, forms):
        context = self.get_context_data(forms=forms)
        return render(self.request, self.template_name, context)

    def get(self, request, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = {}
        if 'forms' not in kwargs:
            context['forms'] = self.get_forms()
        else:
            context['forms'] = kwargs['forms']
        return context

    def get_forms(self):
        forms = {}
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(
                initial=initial[key], 
                **form_kwargs[key]
            )
        return forms

    def get_form_kwargs(self):
        kwargs = {}
        for key in six.iterkeys(self.form_classes):
            if self.request.method in ('POST', 'PUT'):
                kwargs[key] = {
                    'data': self.request.POST,
                    'files': self.request.FILES,
                }
            else:
                kwargs[key] = {}
        return kwargs

    def get_initial(self):
        initial = super(MultiFormCreateView, self).get_initial()
        for key in six.iterkeys(self.form_classes):
            initial[key] = {}
        return initial

    def post(self, request, **kwargs):
        forms = self.get_forms()
        if self.are_forms_valid(forms):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)

class MultiModelFormCreateView(MultiFormCreateView):

    def forms_valid(self, forms):
        for form in six.itervalues(forms):
            form.save()
        return super(MultiModelFormCreateView, self).forms_valid(forms)

    def get_forms(self):
        forms = {}
        objects = self.get_objects()
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(
                instance=objects[key], 
                initial=initial[key], 
                prefix=key,
                **form_kwargs[key]
            )
        return forms

    def get_objects(self):
        objects = {}
        for key in six.iterkeys(self.form_classes):
            objects[key] = None
        return objects

class MultiFormUpdateView(FormView):
    form_classes = {}    

    def are_forms_valid(self, forms):
        for form in six.itervalues(forms):
            if not form.is_valid():
                return False
        return True

    def forms_valid(self, forms): 
        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, forms):
        context = self.get_context_data(forms=forms)
        return render(self.request, self.template_name, context)

    def get(self, request, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = {}
        if 'forms' not in kwargs:
            context['forms'] = self.get_forms()
        else:
            context['forms'] = kwargs['forms']
        return context

    def get_forms(self):
        forms = {}
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(
                initial=initial[key], 
                **form_kwargs[key]
            )
        return forms

    def get_form_kwargs(self):
        kwargs = {}
        for key in six.iterkeys(self.form_classes):
            if self.request.method in ('POST', 'PUT'):
                kwargs[key] = {
                    'data': self.request.POST,
                    'files': self.request.FILES,
                }
            else:
                kwargs[key] = {}
        return kwargs

    def get_initial(self):
        initial = super(MultiFormUpdateView, self).get_initial()
        for key in six.iterkeys(self.form_classes):
            initial[key] = {}
        return initial

    def post(self, request, **kwargs):
        forms = self.get_forms()
        if self.are_forms_valid(forms):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)

class MultiModelFormUpdateView(MultiFormUpdateView):

    def forms_valid(self, forms):
        for form in six.itervalues(forms):
            form.save()
        return super(MultiModelFormUpdateView, self).forms_valid(forms)

    def get_forms(self):
        forms = {}
        objects = self.get_objects()
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(
                instance=objects[key], 
                initial=initial[key], 
                prefix=key,
                **form_kwargs[key]
            )
        return forms

    def get_objects(self):
        objects = {}
        for key in six.iterkeys(self.form_classes):
            objects[key] = None
        return objects

class MultiFormFilterView(FormView):
     
    form_classes = {}    

    def get(self, request, **kwargs):
         
        context = self.get_context_data()
        return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
         
        context = {}
        if 'forms' not in kwargs:
            context['forms'] = self.get_forms()
        else:
            context['forms'] = kwargs['forms']
        return context

    def get_forms(self):
         
        forms = {}
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(
                initial=initial[key], 
                **form_kwargs[key]
            )
        return forms

    def get_form_kwargs(self):

        kwargs = {}
        for key in six.iterkeys(self.form_classes):
            if self.request.method in ('GET'):
                kwargs[key] = {
                    'data': self.request.GET,
                    'files': self.request.FILES,
                }
            else:
                kwargs[key] = {}
        return kwargs

    def get_initial(self):

        initial = super(MultiFormFilterView, self).get_initial()
        for key in six.iterkeys(self.form_classes):
            initial[key] = {}
        return initial

    def post(self, request, **kwargs):

        forms = self.get_forms()
        if self.are_forms_valid(forms):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)

class MultiModelFormFilterView(MultiFormFilterView):

    def forms_valid(self, forms):
        for form in six.itervalues(forms):
            form.save()
        return super(MultiModelFormFilterView, self).forms_valid(forms)

    def get_forms(self):
        forms = {}
        objects = self.get_objects()
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(
                instance=objects[key], 
                initial=initial[key], 
                prefix=key,
                **form_kwargs[key]
            )
        return forms

    def get_objects(self):
        objects = {}
        for key in six.iterkeys(self.form_classes):
            objects[key] = None
        return objects

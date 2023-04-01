from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View



from ads.forms import  CreateForm
from ads.models import Ad
from ads.owner import (OwnerCreateView, OwnerDeleteView, OwnerDetailView,
                       OwnerListView, OwnerUpdateView)


class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name= "ads/ad_detail.html"

    def get(self, request, pk) :
        x = Ad.objects.get(id=pk)
        context = { 'ad' : x }
        return render(request, self.template_name, context)



class AdDeleteView(OwnerDeleteView):
    model = Ad


class AdCreateView( View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        inst = form.save(commit=False)
        inst.owner = self.request.user
        inst.save()
        form.save_m2m()

        return redirect(self.success_url)


class AdUpdateView(View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        inst = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=inst)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        inst = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=inst)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        inst = form.save(commit=False)
        inst.save()
        inst.save_m2m()
        return redirect(self.success_url)







from django.shortcuts import render, redirect, reverse
from .forms import DocumentForm, PhotoForm

from django.http import HttpResponseRedirect

def upload_document(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()  # Save the document instance
            file_metadata = {
                'name': document.file.name,  # Assuming your model has a `file` field
                'size': document.file.size,
            }
            request.session['file_metadata'] = file_metadata  # Store metadata in the session
            return redirect('document_success')
    return render(request, 'upload_document.html', {'form': form})


def document_success(request):
    file_metadata = request.session.pop('file_metadata', None)  # Retrieve and remove metadata
    if not file_metadata:
        return render(request, 'error.html', {'message': 'No file metadata available.'})
    return render(request, 'document_success.html', {'file_metadata': file_metadata})


def upload_photo(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()  # Save the photo instance
            file_metadata = {
                'name': photo.image.name,
                'size': photo.image.size,
            }
            request.session['file_metadata'] = file_metadata  # Store metadata in the session
            return redirect('photo_success')
    return render(request, 'upload_photo.html', {'form': form})



def photo_success(request):
    file_metadata = request.session.pop('file_metadata', None)  # Retrieve and remove metadata
    if not file_metadata:
        return render(request, 'error.html', {'message': 'No file metadata available.'})
    return render(request, 'photo_success.html', {'file_metadata': file_metadata})


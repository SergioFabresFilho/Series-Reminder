from django.shortcuts import render


def generic_message(request, message):
    """ Renders a window with the message inside a jumbotron """
    return render(request, 'message.html', context={
        'message': message,
    })

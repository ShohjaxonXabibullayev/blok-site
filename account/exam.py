from django.contrib.messages.context_processors import messages
from django.shortcuts import redirect

from account.forms import ChangePassForm
from account.utils import send_to_mail, generate_code


def change_pass(request):
    if request.method == "GET":
        code = generate_code()
        request.session['verification_code'] = code
        send_to_mail(request.user.email, code)
        messages.info(request, 'Emailingizga kod yuborildi')
        form = ChangePassForm()
        return render(request, 'account/change_pass.html', {'form':form})
    else:
        form = ChangePassForm()
        if form.is_valid():
            old_pass = form.cleaned_data['old_pass']
            new_pass = form.cleaned_data['new_pass']
            code = form.cleaned_data['code']
            session_code = form.cleaned_data.get('verfication_code')
            if not request.user.check_password(old_pass):
                messages.error(request, 'Siz eski parolingizni xato kiritdingiz!')
                return redirect('change-pass')
            



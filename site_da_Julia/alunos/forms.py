from django import forms

class cadastrado_forms(forms.Form):
    nome_do_aluno = forms.CharField(
        label='Nome do aluno',
        max_length=100,
        required=True
    )
    
    email_do_aluno = forms.EmailField(
        label='Email do aluno',
        max_length=100,
        required=True
    )
    
    senha_do_aluno = forms.CharField(
        label='Senha do aluno', 
        max_length=100, 
        widget=forms.PasswordInput,
        required=True
    )

    confirmacao_da_senha = forms.CharField(
        label='Confirmação da senha', 
        max_length=100, 
        widget=forms.PasswordInput,
        required=True
    ) 

class login_forms(forms.Form):
    username = forms.CharField(
        label='Nome do aluno',
        max_length=100,
        required=True
    )
    
    senha_do_aluno = forms.CharField(
        label='Senha do aluno', 
        max_length=100, 
        widget=forms.PasswordInput,
        required=True
    )
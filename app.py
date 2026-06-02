from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'senha_super_secreta_dunder_mifflin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intranet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False) 
    cargo = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    # 👉 NOVO: Adicionamos a coluna do Ramal
    ramal = db.Column(db.String(10), nullable=False)
    nivel_acesso = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_digitado = request.form['email']
        senha_digitada = request.form['senha']

        usuario = Usuario.query.filter_by(email=email_digitado).first()

        if usuario and check_password_hash(usuario.senha, senha_digitada):
            session['usuario_id'] = usuario.id
            return redirect(url_for('painel'))
        else:
            flash('Credenciais incorretas. Verifique seu e-mail e senha.')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/painel')
def painel():
    if 'usuario_id' not in session:
        flash('Acesso restrito. Por favor, faça login primeiro.')
        return redirect(url_for('login'))
    
    usuario_logado = db.session.get(Usuario, session['usuario_id'])
    todos_funcionarios = Usuario.query.all()
    
    return render_template('index.html', usuario=usuario_logado, funcionarios=todos_funcionarios)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'usuario_id' not in session:
        flash('Acesso restrito. Faça login primeiro.')
        return redirect(url_for('login'))
    
    usuario_logado = db.session.get(Usuario, session['usuario_id'])
    
    if usuario_logado.nivel_acesso < 2:
        flash('Acesso negado. Apenas Gerência e RH podem cadastrar funcionários.')
        return redirect(url_for('painel'))

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha']) 
        cargo = request.form['cargo']
        departamento = request.form['departamento']
        ramal = request.form['ramal']
        nivel = int(request.form['nivel'])

        if Usuario.query.filter_by(email=email).first():
            flash('Erro: Este e-mail já está cadastrado no sistema.')
            return redirect(url_for('cadastro'))

        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cargo=cargo, departamento=departamento, ramal=ramal, nivel_acesso=nivel)
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash(f'Sucesso! {nome} foi cadastrado(a) no sistema.')
        return redirect(url_for('painel'))

    return render_template('cadastro.html', usuario=usuario_logado)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
   
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    usuario_logado = db.session.get(Usuario, session['usuario_id'])
    
    if usuario_logado.nivel_acesso < 2:
        flash('Acesso negado. Apenas Gerência e RH podem editar funcionários.')
        return redirect(url_for('painel'))

   
    funcionario_alvo = db.session.get(Usuario, id)

    if request.method == 'POST':

        funcionario_alvo.nome = request.form['nome']
        funcionario_alvo.cargo = request.form['cargo']
        funcionario_alvo.departamento = request.form['departamento']
        funcionario_alvo.ramal = request.form['ramal']
        
        db.session.commit()
        flash(f'Sucesso! Os dados de {funcionario_alvo.nome} foram atualizados.')
        return redirect(url_for('painel'))


    return render_template('editar.html', usuario=usuario_logado, f=funcionario_alvo)


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    usuario_logado = db.session.get(Usuario, session['usuario_id'])
    
    if usuario_logado.nivel_acesso < 2:
        flash('Acesso negado.')
        return redirect(url_for('painel'))

    funcionario_alvo = db.session.get(Usuario, id)


    if funcionario_alvo.id == usuario_logado.id:
        flash('Erro de operação: Você não pode deletar a sua própria conta.')
        return redirect(url_for('painel'))

   
    db.session.delete(funcionario_alvo)
    db.session.commit()
    
    flash(f'O funcionário foi desligado do sistema com sucesso.')
    return redirect(url_for('painel'))
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash('Você saiu do sistema com segurança.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True) 